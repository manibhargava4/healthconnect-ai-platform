import json
from mq_monitor import get_queue_metrics

result = get_queue_metrics()

print(
    json.dumps(
        result,
        indent=2
    )
)