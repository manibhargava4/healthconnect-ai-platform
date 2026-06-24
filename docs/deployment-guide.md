# HealthConnect – Deployment Guide

## 1. Overview

This guide describes how to deploy and run the HealthConnect AI-Powered Healthcare Integration & AIOps Platform in a local development environment.

---

# 2. Prerequisites

Install the following software:

## IBM App Connect Enterprise

Version:

```text id="2mtnz8"
IBM ACE 13
```

---

## IBM MQ

Version:

```text id="rw6k1i"
IBM MQ Developer Edition
```

---

## Python

Version:

```text id="fdbjxz"
Python 3.10+
```

Verify:

```bash id="xfxe41"
python --version
```

---

## Git

Verify:

```bash id="2of3b2"
git --version
```

---

## Ollama

Verify:

```bash id="4n7jdm"
ollama --version
```

---

## Qwen Model

Install:

```bash id="e5chlw"
ollama pull qwen3:8b
```

Verify:

```bash id="5g4pj5"
ollama list
```

Expected:

```text id="jv4y5x"
qwen3:8b
```

---

# 3. Clone Repository

```bash id="rn16a4"
git clone https://github.com/manibhargava4/healthconnect-ai-platform.git
```

```bash id="x6hgtm"
cd healthconnect-ai-platform
```

---

# 4. IBM MQ Setup

## Create Queue Manager

```bash id="5m0kl0"
crtmqm HCQM
```

Start:

```bash id="h8x83u"
strmqm HCQM
```

---

## Required Queues

```text id="9aw9xj"
REQUEST.Q
RESPONSE.Q
ERROR.Q

BOQ.REQUEST.Q
HCQM.DLQ

LAB.REQUEST.Q
LAB.RESPONSE.Q

ALERT.Q
```

Verify:

```bash id="jgmnvo"
runmqsc HCQM
DISPLAY QLOCAL(*)
```

---

# 5. Start ACE Integration Server

Integration Server:

```text id="d5m3my"
HC_DEV_SERVER
```

Start:

```bash id="3w3u8e"
Integration Server → Start
```

or

```bash id="7e1pq6"
mqsistart HC_DEV_SERVER
```

Verify:

```bash id="1c0xot"
http://localhost:7600/apiv2
```

---

# 6. Deploy ACE Applications

Deploy the following applications:

```text id="9k9yui"
HealthConnectPatientAPI

HealthConnectLabIntegration

HealthConnectAlerting

HealthConnectMemberEligibility

HealthConnectAIAPI
```

Verify deployment status from Toolkit.

---

# 7. Start Python Services

---

## Patient Service

Location:

```text id="yrpz9h"
PatientService
```

Install dependencies:

```bash id="v39ibf"
pip install -r requirements.txt
```

Start:

```bash id="lm5uoa"
python app.py
```

Port:

```text id="5hzw9e"
5001
```

---

## Lab Service

Location:

```text id="72ks3q"
LabService
```

Start:

```bash id="6xwuy7"
python app.py
```

Port:

```text id="olhr46"
5002
```

---

## Audit Service

Location:

```text id="z7lm2q"
AuditService
```

Start:

```bash id="z2squ2"
python app.py
```

Port:

```text id="8mns3j"
5003
```

---

## Monitoring Service

Location:

```text id="m8lm8d"
Monitoring
```

Start:

```bash id="ndgr17"
python monitor_api.py
```

Port:

```text id="f95wzv"
5000
```

Verify:

```http id="u4axrn"
GET http://localhost:5000/monitor/queues
```

---

# 8. Start Ollama

Start Ollama service.

Verify:

```bash id="5bzf8e"
ollama list
```

Verify model response:

```bash id="s7ymx8"
ollama run qwen3:8b
```

---

# 9. Start AI Service

Location:

```text id="5u6s7k"
ai/AIService
```

Install dependencies:

```bash id="u0v4mw"
pip install -r requirements.txt
```

Start:

```bash id="kz58oz"
uvicorn app:app --host 0.0.0.0 --port 5004 --reload
```

Verify:

```http id="mqabn3"
GET http://localhost:5004/health
```

Expected:

```json id="i7mwm8"
{
  "status": "UP"
}
```

---

# 10. Startup Sequence

Services must be started in the following order:

```text id="uvg4z0"
1. IBM MQ
2. Queue Manager HCQM
3. ACE Integration Server
4. Patient Service
5. Lab Service
6. Audit Service
7. Monitoring Service
8. Ollama
9. AI Service
```

---

# 11. Smoke Tests

## Patient API

```http id="u8q3ko"
GET /api/patients?patientId=P1001
```

Expected:

```text id="50t82t"
Patient returned successfully
```

---

## Lab Workflow

```http id="cymms0"
POST /api/lab/request
```

Expected:

```text id="gnsy0r"
Message published to LAB.REQUEST.Q
```

---

## Audit Workflow

Expected:

```text id="epq9qa"
Audit event created automatically
```

---

## Monitoring API

```http id="3sh6zb"
GET /monitor/queues
```

Expected:

```text id="ttndwo"
Queue metrics returned
```

---

## AI Clinical Summary

```http id="26u8zm"
POST /ai/clinical-summary
```

Expected:

```text id="2kr5i4"
AI-generated summary returned
```

---

## AI Incident Analysis

```http id="4w7r9e"
POST /ai/incident-analysis
```

Expected:

```text id="ee3jzq"
AI-generated incident analysis returned
```

---

## Monitoring Analysis

```http id="pbq5e4"
GET /ai/analyze-monitoring
```

Expected:

```text id="u0frzh"
AI-generated operational analysis returned
```

---

# 12. Troubleshooting

## MQ Not Running

Verify:

```bash id="bxefqf"
dspmq
```

---

## ACE Not Running

Verify:

```bash id="wgs9ia"
mqsilist
```

---

## Monitoring API Unavailable

Verify:

```http id="71xjpb"
GET http://localhost:5000/monitor/queues
```

---

## AI Service Unavailable

Verify:

```http id="yj4es9"
GET http://localhost:5004/health
```

---

## Ollama Not Responding

Verify:

```bash id="k6d2vq"
ollama list
```

and

```bash id="4i1nkk"
ollama run qwen3:8b
```

---

# 13. Future Deployment Enhancements

* Docker Compose
* Kubernetes
* GitHub Actions CI/CD
* Container Registry
* Cloud Deployment
* Automated Monitoring
