# 🏥 HealthConnect

## AI-Powered Healthcare Integration & AIOps Platform

Enterprise-grade healthcare integration platform built using IBM App Connect Enterprise (ACE), IBM MQ, Python Microservices, FastAPI, Ollama, and Qwen3.

---

## 🚀 Project Overview

HealthConnect simulates a real-world healthcare integration ecosystem with:

✅ REST APIs

✅ IBM MQ Messaging

✅ Event-Driven Architecture

✅ Audit Processing

✅ Monitoring & Alerting

✅ AI-Powered Clinical Summaries

✅ AI-Powered Incident Analysis

✅ ACE + AI Integration

✅ AIOps Monitoring Intelligence

---

## 🏗 Architecture

```text
                    ┌────────────────────┐
                    │   Patient Service  │
                    │       :5001        │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │ HealthConnect      │
                    │ Patient API        │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │   LAB.REQUEST.Q    │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │    Lab Service     │
                    │       :5002        │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │  LAB.RESPONSE.Q    │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │   Audit Service    │
                    │       :5003        │
                    └────────────────────┘



                    ┌────────────────────┐
                    │ Monitoring Service │
                    │       :5000        │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │     AI Service     │
                    │       :5004        │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │      Ollama        │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │     Qwen3:8b       │
                    └────────────────────┘
```

---

## 🧩 Technology Stack

### Integration

* IBM App Connect Enterprise (ACE) 13
* IBM MQ

### Microservices

* Python
* Flask
* FastAPI

### AI

* Ollama
* Qwen3:8b

### Monitoring

* Queue Monitoring
* Alerting
* Incident Detection

### DevOps

* Git
* GitHub

---

## 📂 Repository Structure

```text
healthconnect-ai-platform/

├── ace-applications/
├── PatientService/
├── LabService/
├── AuditService/
├── Monitoring/
├── AI/
│   └── AIService/
├── docs/
└── README.md
```

---

## 🎯 Core Features

### Patient Integration

* Patient CRUD APIs
* ACE API Integration

### Lab Processing

* REST → MQ → REST → MQ

### Audit Processing

* Automated audit event generation

### Monitoring

* Queue depth monitoring
* Queue manager monitoring
* Trend analysis
* Incident tracking

### AI Clinical Summary

Generate AI-powered summaries from lab results.

### AI Incident Analysis

Generate:

* Severity Assessment
* Root Cause Analysis
* Operational Recommendations

### AIOps Monitoring Analysis

Automatically analyze monitoring metrics using AI.

---

## 📊 Current Status

| Sprint              | Status |
| ------------------- | ------ |
| Foundation Setup    | ✅      |
| Patient Service     | ✅      |
| ACE Integration     | ✅      |
| IBM MQ Messaging    | ✅      |
| Lab Service         | ✅      |
| Audit Service       | ✅      |
| Monitoring Platform | ✅      |
| AI Platform         | ✅      |
| Docker              | ⏳      |
| Kubernetes          | ⏳      |
| CI/CD               | ⏳      |

---

## 📚 Documentation

* docs/architecture.md
* docs/requirements.md
* docs/api-reference.md
* docs/deployment-guide.md
* docs/interview-notes.md

---

## 🔮 Roadmap

### Sprint 8

* Docker
* Docker Compose

### Sprint 9

* Kubernetes

### Sprint 10

* GitHub Actions CI/CD

### Sprint 11

* Enhanced Observability

---

## 👨‍💻 Author

Banka Mani Bhargava

IBM ACE Developer | Middleware Engineer | DevOps Engineer

---

## ⭐ Key Highlights

* IBM ACE + IBM MQ Integration
* Event-Driven Architecture
* AI-Powered Clinical Intelligence
* AI-Powered Operations Intelligence
* Local LLM Integration
* AIOps Concepts
* Enterprise Integration Patterns
