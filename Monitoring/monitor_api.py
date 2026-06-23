from flask import Flask, jsonify
from mq_monitor import get_queue_metrics, get_history, get_trends, get_incidents

app = Flask(__name__)

@app.route("/monitor/queues")
def monitor():

    return jsonify(
        get_queue_metrics()
    )

@app.route("/monitor/history")
def monitor_history():
    return jsonify(
        get_history()
    )

@app.route("/monitor/trends")
def trends():

    return jsonify(
        get_trends()
    )

@app.route("/monitor/incidents")
def incidents():

    return jsonify(
        get_incidents()
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )