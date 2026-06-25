# 🏥 HealthConnect

# AI-Powered Healthcare Integration & AIOps Platform

Enterprise-grade healthcare integration and AIOps platform built using IBM App Connect Enterprise (ACE), IBM MQ, Python Microservices, FastAPI, Docker, Docker Compose, Ollama, and Qwen3.

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

✅ Dockerized Microservices

✅ Docker Compose Orchestration

---

## 🐳 Dockerized Microservices Platform

The complete Python platform has been containerized using Docker and Docker Compose.

### Containerized Services

| Service            | Port |
| ------------------ | ---- |
| Patient Service    | 5001 |
| Lab Service        | 5002 |
| Audit Service      | 5003 |
| Monitoring Service | 5000 |
| AI Service         | 5004 |

### External Components

The following components remain on the host machine:

* IBM App Connect Enterprise (ACE)
* IBM MQ
* Ollama (Qwen3:8b)

### Start Entire Platform

```bash
docker compose up --build
```

### Docker Compose Deployment

![Docker Compose Running](docs/images/docker-compose-running.png)

All services were successfully tested both individually and through Docker Compose.

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
                    │ Host Machine       │
                    └─────────┬──────────┘
                              │
                              ▼

                    ┌────────────────────┐
                    │     Qwen3:8b       │
                    └────────────────────┘
```

---

## 📸 Platform Screenshots

### Docker Containers Running

![Docker Containers](docs/images/docker-ps.png)

All microservices running as independent Docker containers.

### Docker Images

![Docker Images](docs/images/docker-images.png)

Docker images successfully built for all services.

### AI Clinical Summary

![Clinical Summary](docs/images/ai-clinical-summary.png)

AI-generated clinical summaries using Ollama and Qwen3:8b.

### AI Service Health Check

![AI Health](docs/images/ai-health.png)

AI Service running successfully inside Docker while communicating with Ollama on the host machine.

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
* Trend Analysis

### Containerization

* Docker
* Docker Compose

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
│   ├── images/
│   ├── architecture.md
│   ├── requirements.md
│   ├── api-reference.md
│   ├── deployment-guide.md
│   ├── docker-guide.md
│   └── interview-notes.md
├── docker-compose.yml
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

### Monitoring Platform

* Queue Depth Monitoring
* Queue Manager Monitoring
* Trend Analysis
* Incident Detection
* Alert Generation

### AI Clinical Summary

Generate AI-powered summaries from healthcare laboratory results.

### AI Incident Analysis

Generate:

* Severity Assessment
* Root Cause Analysis
* Operational Recommendations

### AIOps Monitoring Analysis

Automatically analyze monitoring metrics using local LLMs.

---

## 🎯 Key Achievements

* Built 5 independent healthcare microservices
* Implemented IBM ACE and IBM MQ integration
* Implemented Request/Reply messaging patterns
* Implemented Audit Processing architecture
* Built Monitoring and Alerting platform
* Integrated Local LLMs using Ollama and Qwen3
* Built AI-powered Incident Analysis
* Built AI-powered Clinical Summary Generation
* Containerized complete platform using Docker
* Orchestrated services using Docker Compose
* Implemented container-to-host communication using host.docker.internal

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
| Docker              | ✅      |
| Docker Compose      | ✅      |
| Kubernetes          | ⏳      |
| CI/CD               | ⏳      |

---

## 📚 Documentation

* docs/architecture.md
* docs/requirements.md
* docs/api-reference.md
* docs/deployment-guide.md
* docs/docker-guide.md
* docs/interview-notes.md

---

## 🔮 Roadmap

### Completed

* IBM MQ Messaging
* IBM ACE Integration
* Audit Service
* Monitoring Platform
* AI Platform
* Docker
* Docker Compose

### In Progress

* Kubernetes Deployments
* Kubernetes Services
* ConfigMaps
* Secrets

### Planned

* GitHub Actions CI/CD
* Prometheus
* Grafana
* OpenShift Deployment

---

## 👨‍💻 Author

**Banka Mani Bhargava**

IBM ACE Developer | Middleware Engineer | DevOps Engineer

GitHub: https://github.com/manibhargava4

LinkedIn: https://linkedin.com/in/bankamanibhargava

---

## ⭐ Key Highlights

* IBM ACE + IBM MQ Integration
* Event-Driven Architecture
* AI-Powered Clinical Intelligence
* AI-Powered Operations Intelligence
* Local LLM Integration
* AIOps Concepts
* Dockerized Microservices
* Docker Compose Orchestration
* Enterprise Integration Patterns
* Healthcare Integration Platform
