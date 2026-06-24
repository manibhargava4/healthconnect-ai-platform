# HealthConnect – API Reference

## Overview

This document describes all APIs exposed by the HealthConnect platform.

Base Services:

| Service            | Port               |
| ------------------ | ------------------ |
| Patient Service    | 5001               |
| Lab Service        | 5002               |
| Audit Service      | 5003               |
| Monitoring Service | 5000               |
| AI Service         | 5004               |
| IBM ACE APIs       | Integration Server |

---

# 1. Patient Service APIs

## Get Patient

### Request

```http
GET /patients/{patientId}
```

### Example

```http
GET /patients/P1001
```

### Response

```json
{
  "patientId": "P1001",
  "name": "John Doe",
  "age": 35
}
```

---

## Get All Patients

### Request

```http
GET /patients
```

### Response

```json
[
  {
    "patientId": "P1001",
    "name": "John Doe"
  }
]
```

---

## Create Patient

### Request

```http
POST /patients
```

### Payload

```json
{
  "patientId": "P1001",
  "name": "John Doe",
  "age": 35
}
```

---

## Update Patient

### Request

```http
PUT /patients/{patientId}
```

---

## Delete Patient

### Request

```http
DELETE /patients/{patientId}
```

---

# 2. Lab Service APIs

## Create Lab Result

### Request

```http
POST /lab/results
```

### Payload

```json
{
  "patientId": "P1001",
  "testName": "HbA1c",
  "result": "8.4"
}
```

### Response

```json
{
  "resultId": "LAB001",
  "status": "CREATED"
}
```

---

## Get Lab Results

### Request

```http
GET /lab/results
```

---

## Get Lab Result By ID

### Request

```http
GET /lab/results/{resultId}
```

---

# 3. Audit Service APIs

## Create Audit Event

### Request

```http
POST /audit/events
```

### Payload

```json
{
  "eventType": "LAB_RESULT_CREATED",
  "patientId": "P1001"
}
```

---

## Get Audit Events

### Request

```http
GET /audit/events
```

---

## Get Audit Event By ID

### Request

```http
GET /audit/events/{eventId}
```

---

# 4. Monitoring APIs

## Queue Metrics

### Request

```http
GET /monitor/queues
```

### Sample Response

```json
{
  "consumerStatus": "RUNNING",
  "queueManager": "HCQM",
  "status": "RUNNING"
}
```

---

## Queue History

### Request

```http
GET /monitor/history
```

---

## Queue Trends

### Request

```http
GET /monitor/trends
```

---

## Incidents

### Request

```http
GET /monitor/incidents
```

---

# 5. AI Service APIs

## Health Check

### Request

```http
GET /health
```

### Response

```json
{
  "status": "UP",
  "service": "AIService",
  "provider": "Ollama",
  "model": "qwen3:8b"
}
```

---

## Clinical Summary Generation

### Request

```http
POST /ai/clinical-summary
```

### Payload

```json
{
  "patientId": "P1001",
  "testName": "HbA1c",
  "result": "8.4",
  "unit": "%",
  "referenceRange": "4.0-5.6"
}
```

### Response

```json
{
  "patientId": "P1001",
  "summary": "Generated clinical summary"
}
```

---

## Incident Analysis

### Request

```http
POST /ai/incident-analysis
```

### Payload

```json
{
  "queue": "LAB.REQUEST.Q",
  "depth": 125,
  "consumerStatus": "STOPPED",
  "dlqDepth": 0,
  "boqDepth": 15
}
```

### Response

```json
{
  "analysis": "AI generated operational analysis"
}
```

---

## Monitoring Analysis

### Request

```http
GET /ai/analyze-monitoring
```

### Response

```json
{
  "monitoring": {},
  "analysis": "AI generated monitoring analysis"
}
```

---

## Incident Repository

### Request

```http
GET /ai/incidents
```

### Response

```json
[
  {
    "generatedAt": "2026-06-24T18:00:00",
    "analysis": "..."
  }
]
```

---

# 6. IBM ACE APIs

## Get Patient API

### ACE Application

```text
HealthConnectPatientAPI
```

### Route

```http
GET /api/patients?patientId=P1001
```

---

## Lab Request API

### ACE Application

```text
HealthConnectLabIntegration
```

### Route

```http
POST /api/lab/request
```

### Purpose

Publishes message to:

```text
LAB.REQUEST.Q
```

---

## Queue Monitoring Dashboard

### ACE Application

```text
HealthConnectMemberEligibility
```

### Route

```http
GET /monitor/dashboard
```

### Purpose

Returns monitoring metrics through ACE.

---

## AI Incident Analysis API

### ACE Application

```text
HealthConnectAIAPI
```

### Route

```http
POST /ai/incident-analysis
```

### Flow

```text
Client
   ↓
ACE
   ↓
AI Service
   ↓
Ollama
   ↓
Qwen3
```

---

# 7. Queue Reference

| Queue          | Purpose                 |
| -------------- | ----------------------- |
| REQUEST.Q      | MQ Request Processing   |
| RESPONSE.Q     | MQ Response Processing  |
| ERROR.Q        | Error Handling          |
| BOQ.REQUEST.Q  | Backout Queue           |
| HCQM.DLQ       | Dead Letter Queue       |
| LAB.REQUEST.Q  | Lab Request Processing  |
| LAB.RESPONSE.Q | Lab Response Processing |
| ALERT.Q        | Alert Notifications     |

---

# 8. Service Dependencies

```text
Patient Service
     ↑
     │
HealthConnectPatientAPI


Lab Service
     ↑
     │
HealthConnectLabIntegration


Audit Service
     ↑
     │
LabResponseAuditFlow


Monitoring Service
     ↑
     │
QueueMonitoringDashboard


AI Service
     ↑
     │
HealthConnectAIAPI
```
