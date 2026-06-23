import subprocess
import re
from datetime import datetime
import json
import os

HISTORY_FILE = "queue_history.json"
MAX_HISTORY = 100
QMGR = "HCQM"

QUEUES = [
    "REQUEST.Q",
    "RESPONSE.Q",
    "BOQ.REQUEST.Q",
    "HCQM.DLQ"
]

WARNING_THRESHOLD = 20
CRITICAL_THRESHOLD = 100

def get_trends():

    history = get_history()

    if len(history) < 2:
        return {
            "message": "Not enough history available"
        }

    latest = history[-1]
    previous = history[-2]

    trends = {}

    for queue in latest["queues"]:

        current_depth = latest["queues"][queue]

        previous_depth = previous["queues"].get(
            queue,
            0
        )

        growth = current_depth - previous_depth

        if growth > 0:
            trend = "INCREASING"
        elif growth < 0:
            trend = "DECREASING"
        else:
            trend = "STABLE"

        trends[queue] = {
            "currentDepth": current_depth,
            "previousDepth": previous_depth,
            "growth": growth,
            "trend": trend
        }

    return trends

def get_incidents():

    incidents = []

    metrics = get_queue_metrics()

    trends = get_trends()

    # Rule 1 - Consumer Down
    if metrics["consumerStatus"] != "RUNNING":

        incidents.append({
            "type": "CONSUMER_DOWN",
            "severity": "CRITICAL",
            "message": "MQ Consumer is not running"
        })

    # Rule 2 - DLQ Activity
    dlq_depth = metrics["queues"]["HCQM.DLQ"]["depth"]

    if dlq_depth > 0:

        incidents.append({
            "type": "DLQ_ACTIVITY",
            "severity": "CRITICAL",
            "queue": "HCQM.DLQ",
            "depth": dlq_depth,
            "message": f"{dlq_depth} messages found in DLQ"
        })

    # Rule 3 - BOQ Activity
    boq_depth = metrics["queues"]["BOQ.REQUEST.Q"]["depth"]

    if boq_depth > 0:

        incidents.append({
            "type": "BACKOUT_ACTIVITY",
            "severity": "CRITICAL",
            "queue": "BOQ.REQUEST.Q",
            "depth": boq_depth,
            "message": f"{boq_depth} messages found in Backout Queue"
        })

    # Rule 4 - Queue Growth
    if "message" not in trends:

        for queue, data in trends.items():

            if (
                data["trend"] == "INCREASING"
                and data["growth"] > 5
            ):

                incidents.append({
                    "type": "QUEUE_BACKLOG",
                    "severity": "WARNING",
                    "queue": queue,
                    "currentDepth": data["currentDepth"],
                    "growth": data["growth"],
                    "message": f"{queue} increased by {data['growth']} messages"
                })

    return {
        "incidentCount": len(incidents),
        "incidents": incidents
    }


def save_history(metrics):

    snapshot = {
        "timestamp": metrics["timestamp"],
        "queues": {}
    }

    for queue, data in metrics["queues"].items():

        snapshot["queues"][queue] = data["depth"]

    try:

        if os.path.exists(HISTORY_FILE):

            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)

        else:
            history = []

        history.append(snapshot)

        # Keep only latest 100 records
        history = history[-MAX_HISTORY:]

        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)

    except Exception as e:

        print(f"History save failed: {e}")


def get_history():

    try:

        if os.path.exists(HISTORY_FILE):

            with open(HISTORY_FILE, "r") as f:
                return json.load(f)

        return []

    except Exception:

        return []

def check_consumer_status():

    try:

        output = subprocess.check_output(
            'tasklist',
            shell=True,
            text=True
        )

        if "IntegrationServer.exe" in output:
            return "RUNNING"

        return "STOPPED"

    except Exception:
        return "UNKNOWN"

def get_queue_status(queue_name, depth):

    # Special handling for BOQ and DLQ
    if queue_name in ["BOQ.REQUEST.Q", "HCQM.DLQ"]:
        if depth > 0:
            return "CRITICAL", True
        else:
            return "HEALTHY", False

    # Normal queues
    if depth > CRITICAL_THRESHOLD:
        return "CRITICAL", True

    elif depth > WARNING_THRESHOLD:
        return "WARNING", False

    else:
        return "HEALTHY", False


def get_queue_depth(queue):

    cmd = f'echo DISPLAY QSTATUS({queue}) CURDEPTH | runmqsc {QMGR}'

    try:

        output = subprocess.check_output(
            cmd,
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )

        match = re.search(r'CURDEPTH\((\d+)\)', output)

        if match:
            return int(match.group(1))

        return -1

    except Exception:
        return -1


def check_qmgr_status():

    cmd = f'echo DISPLAY QMGR | runmqsc {QMGR}'

    try:

        subprocess.check_output(
            cmd,
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )

        return "RUNNING"

    except Exception:

        return "DOWN"


def get_queue_metrics():

    qmgr_status = check_qmgr_status()

    result = {
        "queueManager": QMGR,
        "status": qmgr_status,
        "consumerStatus": check_consumer_status(),
        "timestamp": datetime.now().isoformat(),
        "queues": {}
    }

    # If MQ is down
    if qmgr_status == "DOWN":

        result["error"] = "Queue Manager not available"

        return result

    for queue in QUEUES:

        depth = get_queue_depth(queue)

        status, alert = get_queue_status(
            queue,
            depth
        )

        result["queues"][queue] = {
            "depth": depth,
            "status": status,
            "alert": alert
        }

    save_history(result)
    return result