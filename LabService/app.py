from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

RESULT_FILE = "results.json"


def load_results():

    if not os.path.exists(RESULT_FILE):
        return []

    with open(RESULT_FILE, "r") as f:
        return json.load(f)


def save_results(results):

    with open(RESULT_FILE, "w") as f:
        json.dump(results, f, indent=2)


@app.route("/lab/results", methods=["POST"])
def create_result():

    request_data = request.json

    results = load_results()

    result_id = f"R{len(results) + 1001}"

    result = {
        "resultId": result_id,
        "patientId": request_data["patientId"],
        "testType": request_data["testType"],
        "result": "NORMAL",
        "status": "COMPLETED",
        "createdTime": datetime.now().isoformat()
    }

    results.append(result)

    save_results(results)

    return jsonify(result), 201


@app.route("/lab/results", methods=["GET"])
def get_all_results():

    return jsonify(load_results())


@app.route("/lab/results/<result_id>", methods=["GET"])
def get_result(result_id):

    results = load_results()

    for result in results:

        if result["resultId"] == result_id:
            return jsonify(result)

    return jsonify({
        "error": "Result not found"
    }), 404


@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "UP",
        "service": "lab-service"
    }, 200

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5002,
        debug=True
    )