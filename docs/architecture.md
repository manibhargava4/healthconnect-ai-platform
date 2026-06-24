# HealthConnect – AI-Powered Healthcare Integration & AIOps Platform

## 1. Project Overview

HealthConnect is an enterprise-style healthcare integration platform built to demonstrate IBM App Connect Enterprise (ACE), IBM MQ, Microservices, Observability, AIOps, and Local LLM Integration.

The platform simulates real-world healthcare workflows including patient retrieval, lab processing, audit logging, monitoring, alerting, and AI-powered incident analysis.

---

## 2. Technology Stack

### Integration Layer

* IBM App Connect Enterprise (ACE) 13
* IBM MQ

### Microservices

* Python Flask
* Python FastAPI

### AI Layer

* Ollama
* Qwen3:8b

### Monitoring & Observability

* Custom Queue Monitoring Platform
* Alert Generation Engine

### Version Control

* Git
* GitHub

---

## 3. High-Level Architecture

```text
Patient Service (5001)
        ↑
        │
HealthConnectPatientAPI
        │
        ▼

Lab Request API
        │
        ▼

LAB.REQUEST.Q
        │
        ▼

Lab Request Consumer
        │
        ▼

Lab Service (5002)
        │
        ▼

LAB.RESPONSE.Q
        │
        ▼

LabResponseAuditFlow
        │
        ▼

Audit Service (5003)



Monitoring Service (5000)
        │
        ▼

AI Service (5004)
        │
        ▼

Ollama
        │
        ▼

Qwen3:8b



HealthConnectAIAPI
        │
        ▼

AI Service
        │
        ▼

Ollama
```

---

## 4. IBM MQ Architecture

### Queue Manager

```text
HCQM
```

### Queues

| Queue          | Purpose             |
| -------------- | ------------------- |
| REQUEST.Q      | Request Processing  |
| RESPONSE.Q     | Response Processing |
| ERROR.Q        | Error Handling      |
| BOQ.REQUEST.Q  | Backout Queue       |
| HCQM.DLQ       | Dead Letter Queue   |
| LAB.REQUEST.Q  | Lab Request Queue   |
| LAB.RESPONSE.Q | Lab Response Queue  |
| ALERT.Q        | Alert Notifications |

---

## 5. ACE Application Inventory

### HealthConnectPatientAPI

#### Flow

```text
GetPatient.msgflow
```

#### Purpose

Retrieves patient information from Patient Service.

#### Route

```text
Client
   ↓
ACE
   ↓
Patient Service
```

---

### HealthConnectLabIntegration

#### LabRequestProducer.msgflow

```text
REST → MQ
```

Publishes lab requests to LAB.REQUEST.Q.

#### LabRequestConsumer.msgflow

```text
MQ → REST → MQ
```

Consumes LAB.REQUEST.Q, invokes Lab Service, publishes LAB.RESPONSE.Q.

#### LabResponseAuditFlow.msgflow

Consumes LAB.RESPONSE.Q and creates audit events.

---

### HealthConnectAlerting

#### PublishAlerts.msgflow

Creates operational alert messages.

#### AlertConsumer.msgflow

Processes generated alerts.

---

### HealthConnectMemberEligibility

#### MemberEligibility.msgflow

Original ACE HTTP integration flow.

#### MQConsumer.msgflow

Processes MQ requests.

#### MQResponseConsumer.msgflow

Processes MQ responses.

#### QueueMonitoringDashboard.msgflow

Provides monitoring dashboard integration.

---

### HealthConnectAIAPI

#### AIIncidentAnalysisFlow.msgflow

```text
HTTP Input
      ↓
Compute
      ↓
HTTP Request
      ↓
HTTP Reply
```

Invokes AI Service for incident analysis.

---

## 6. Microservice Inventory

### Patient Service

Port: 5001

Responsibilities:

* Create Patient
* Get Patient
* Update Patient
* Delete Patient

Storage:

* patients.json

---

### Lab Service

Port: 5002

Responsibilities:

* Create Lab Results
* Retrieve Lab Results

Storage:

* results.json

---

### Audit Service

Port: 5003

Responsibilities:

* Create Audit Events
* Retrieve Audit Events

Storage:

* audit.json

---

### Monitoring Service

Port: 5000

Endpoints:

```text
GET /monitor/queues
GET /monitor/history
GET /monitor/trends
GET /monitor/incidents
```

Responsibilities:

* Queue Depth Monitoring
* Queue Manager Monitoring
* Alert Generation
* Trend Analysis
* Incident Tracking

Storage:

* queue_metrics.json
* queue_history.json

---

### AI Service

Port: 5004

Framework:

* FastAPI

Endpoints:

```text
POST /ai/clinical-summary
POST /ai/incident-analysis
GET  /ai/analyze-monitoring
GET  /ai/incidents
GET  /health
```

Responsibilities:

* Clinical Summary Generation
* Incident Analysis
* Monitoring Analysis
* Incident Repository

Storage:

* clinical_summaries.json
* incident_reports.json

AI Model:

* Ollama
* Qwen3:8b

---

## 7. Business Workflow – Lab Processing

```text
Client
   ↓
ACE LabRequestProducer
   ↓
LAB.REQUEST.Q
   ↓
ACE LabRequestConsumer
   ↓
Lab Service
   ↓
LAB.RESPONSE.Q
   ↓
ACE LabResponseAuditFlow
   ↓
Audit Service
```

---

## 8. AIOps Workflow

```text
Monitoring Service
      ↓
Queue Metrics
      ↓
AI Service
      ↓
Ollama
      ↓
Qwen3
      ↓
Incident Analysis
      ↓
Incident Repository
```

---

## 9. ACE + AI Workflow

```text
Client
      ↓
HealthConnectAIAPI
      ↓
AI Service
      ↓
Ollama
      ↓
Qwen3
      ↓
AI Analysis
      ↓
Client
```

---

## 10. Future Roadmap

### Sprint 8

* Docker

### Sprint 9

* Kubernetes

### Sprint 10

* GitHub Actions CI/CD

### Sprint 11

* Enhanced Observability

### Sprint 12

* Performance Testing

### Sprint 13

* Documentation

### Sprint 14

* Interview Preparation

---

## 11. Key Learning Outcomes

* IBM App Connect Enterprise (ACE)
* IBM MQ Messaging Patterns
* REST and MQ Integration
* Event-Driven Architecture
* Observability and Monitoring
* Alerting Systems
* FastAPI Development
* AI Integration using Ollama
* Local LLM Deployment
* AIOps Concepts
* Enterprise Integration Design
