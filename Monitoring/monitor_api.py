from flask import Flask, jsonify
from mq_monitor import get_queue_metrics

app = Flask(__name__)

@app.route("/monitor/queues")
def monitor():

    return jsonify(
        get_queue_metrics()
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )