import subprocess
import re
import json

QMGR = "HCQM"

QUEUES = [
    "REQUEST.Q",
    "RESPONSE.Q",
    "BOQ.REQUEST.Q",
    "HCQM.DLQ"
]

def get_status(depth):
    if depth > 50:
        return "CRITICAL"
    elif depth > 10:
        return "WARNING"
    else:
        return "HEALTHY"

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

print(json.dumps(result, indent=2))