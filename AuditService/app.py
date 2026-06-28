from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

AUDIT_FILE = "audit.json"


def load_events():

    if not os.path.exists(AUDIT_FILE):
        return []

    with open(AUDIT_FILE, "r") as f:
        return json.load(f)


def save_events(events):

    with open(AUDIT_FILE, "w") as f:
        json.dump(events, f, indent=2)


@app.route("/audit/events", methods=["POST"])
def create_event():

    request_data = request.json

    events = load_events()

    event_id = f"A{len(events) + 1001}"

    event = {
        "eventId": event_id,
        "eventType": request_data["eventType"],
        "patientId": request_data["patientId"],
        "timestamp": datetime.now().isoformat()
    }

    events.append(event)

    save_events(events)

    return jsonify(event), 201


@app.route("/audit/events", methods=["GET"])
def get_all_events():

    return jsonify(load_events())


@app.route("/audit/events/<event_id>", methods=["GET"])
def get_event(event_id):

    events = load_events()

    for event in events:

        if event["eventId"] == event_id:
            return jsonify(event)

    return jsonify({
        "error": "Event not found"
    }), 404


@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "UP",
        "service": "audit-service"
    }, 200


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5003,
        debug=True
    )