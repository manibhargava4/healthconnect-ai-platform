# Release Notes - Version 1.5

## Release Date

June 2026

---

# Sprint 12.5 – Production Polish

This release enhances the Kubernetes deployment by introducing production-oriented networking improvements and API consistency before adding observability.

## New Features

### Standardized Health Endpoints

All services now expose service-specific health endpoints.

| Service            | Health Endpoint    |
| ------------------ | ------------------ |
| Patient Service    | `/patients/health` |
| Lab Service        | `/lab/health`      |
| Audit Service      | `/audit/health`    |
| Monitoring Service | `/monitor/health`  |
| AI Service         | `/ai/health`       |

---

### Kubernetes Health Probes

Updated readiness and liveness probes to use the new service-specific health endpoints.

---

### NGINX Ingress Improvements

Added production-oriented ingress annotations including:

* Increased proxy timeout
* Increased request body size limit

---

### Image Version Updates

| Service            | Version |
| ------------------ | ------- |
| Patient Service    | v1.0.3  |
| Lab Service        | v1.0.3  |
| Audit Service      | v1.0.3  |
| Monitoring Service | v1.0.1  |
| AI Service         | v1.0.1  |

---

### Documentation

Updated:

* README
* Architecture documentation
* Kubernetes networking documentation

---

## Validation Completed

* All services running successfully
* ClusterIP networking verified
* NGINX Ingress operational
* Path-based routing verified
* Kubernetes probes validated
* Persistent storage verified
* End-to-end API testing completed

---

## Current Project Status

Completed:

* IBM MQ
* IBM ACE
* Python Microservices
* Docker
* Docker Compose
* Kubernetes
* Persistent Storage
* NGINX Ingress
* Production Networking

Next Sprint:

* Prometheus
* Grafana
* Metrics Collection
* Kubernetes Observability
