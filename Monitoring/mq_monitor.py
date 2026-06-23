import subprocess
import re
from datetime import datetime

QMGR = "HCQM"

QUEUES = [
    "REQUEST.Q",
    "RESPONSE.Q",
    "BOQ.REQUEST.Q",
    "HCQM.DLQ"
]

WARNING_THRESHOLD = 20
CRITICAL_THRESHOLD = 100


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

    return result