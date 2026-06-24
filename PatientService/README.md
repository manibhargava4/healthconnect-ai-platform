# Patient Service

## Overview

Patient Service is a Flask-based microservice responsible for managing patient information.

Port:

```text
5001
```

## Features

* Create Patient
* Get Patient
* Get All Patients
* Update Patient
* Delete Patient

## Storage

```text
patients.json
```

## APIs

```http
GET /patients
GET /patients/{patientId}
POST /patients
PUT /patients/{patientId}
DELETE /patients/{patientId}
```

## Dependencies

* Flask

## Used By

```text
HealthConnectPatientAPI
```
