from flask import Flask, jsonify
import subprocess
import re

app = Flask(__name__)

QMGR = "HCQM"

QUEUES = [
    "REQUEST.Q",
    "RESPONSE.Q",
    "BOQ.REQUEST.Q",
    "HCQM.DLQ"
]

def get_status(depth):
    if depth > 100:
        return "CRITICAL"
    elif depth > 20:
        return "WARNING"
    else:
        return "HEALTHY"

@app.route("/monitor/queues")
def monitor():

    result = {}

    for queue in QUEUES:

        cmd = f'echo DISPLAY QSTATUS({queue}) CURDEPTH | runmqsc {QMGR}'

        output = subprocess.check_output(
            cmd,
            shell=True,
            text=True
        )

        match = re.search(r'CURDEPTH\((\d+)\)', output)

        depth = int(match.group(1)) if match else -1

        result[queue] = {
            "depth": depth,
            "status": get_status(depth)
        }

    return jsonify(result)

app.run(host="0.0.0.0", port=5000)