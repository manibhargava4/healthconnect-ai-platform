from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

PATIENT_FILE = os.getenv( "PATIENT_FILE", "/app/data/patients.json")
os.makedirs(os.path.dirname(PATIENT_FILE), exist_ok=True)

def load_patients():

    if not os.path.exists(PATIENT_FILE):
        return []

    with open(PATIENT_FILE, "r") as f:
        return json.load(f)


def save_patients(patients):

    with open(PATIENT_FILE, "w") as f:
        json.dump(
            patients,
            f,
            indent=2
        )


@app.route("/patients", methods=["POST"])
def create_patient():

    patient = request.json

    patients = load_patients()

    patient_id = patient.get("patientId")

    for p in patients:
        if p["patientId"] == patient_id:
            return jsonify({
                "error": "Patient already exists"
            }), 409

    patients.append(patient)

    save_patients(patients)

    return jsonify({
        "message": "Patient created successfully",
        "patient": patient
    }), 201


@app.route("/patients", methods=["GET"])
def get_all_patients():

    return jsonify(
        load_patients()
    )


@app.route("/patients/<patient_id>", methods=["GET"])
def get_patient(patient_id):

    patients = load_patients()

    for patient in patients:

        if patient["patientId"] == patient_id:

            return jsonify(patient)

    return jsonify({
        "error": "Patient not found"
    }), 404


@app.route("/patients/<patient_id>", methods=["PUT"])
def update_patient(patient_id):

    updated_patient = request.json

    patients = load_patients()

    for index, patient in enumerate(patients):

        if patient["patientId"] == patient_id:

            patients[index] = updated_patient

            save_patients(patients)

            return jsonify({
                "message": "Patient updated successfully",
                "patient": updated_patient
            })

    return jsonify({
        "error": "Patient not found"
    }), 404


@app.route("/patients/<patient_id>", methods=["DELETE"])
def delete_patient(patient_id):

    patients = load_patients()

    for patient in patients:

        if patient["patientId"] == patient_id:

            patients.remove(patient)

            save_patients(patients)

            return jsonify({
                "message": "Patient deleted successfully"
            })

    return jsonify({
        "error": "Patient not found"
    }), 404

@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "UP",
        "service": "patient-service"
    }, 200


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )