# HealthConnect AI Platform - Release Notes

## Version: v1.4

**Release Date:** June 2026

---

# Overview

Version **v1.4** introduces persistent storage for the HealthConnect AI Platform, enabling stateful microservices to retain application data across pod restarts, recreations, and rolling updates.

This release transitions the platform from ephemeral container storage to Kubernetes-managed persistent storage using Persistent Volume Claims (PVCs), providing a more production-oriented architecture.

---

# Highlights

* Persistent storage for stateful microservices
* Kubernetes Persistent Volume Claims (PVC)
* Configurable data paths using ConfigMaps
* Pod recovery validation
* Dynamic storage provisioning
* Improved application portability
* Production-ready storage architecture

---

# New Features

## Persistent Storage

Implemented persistent storage for:

* Patient Service
* Lab Service
* Audit Service

Application data now survives:

* Pod deletion
* Pod recreation
* Rolling updates
* Kubernetes self-healing

---

## Kubernetes Persistent Volume Claims

Added Persistent Volume Claims for stateful services.

Benefits include:

* Decoupling application lifecycle from data lifecycle
* Simplified storage management
* Production-style Kubernetes architecture
* Foundation for cloud-native deployments

---

## Configurable Data Paths

Updated application configuration to use environment variables for data storage locations.

Example:

```python
PATIENT_FILE = os.getenv(
    "PATIENT_FILE",
    "/app/data/patients.json"
)
```

Benefits:

* Environment-specific configuration
* Kubernetes compatibility
* Docker compatibility
* Future OpenShift compatibility

---

## Automatic Directory Initialization

Applications now automatically create required storage directories during startup when necessary.

This improves deployment reliability across new environments.

---

## Kubernetes Deployment Enhancements

Updated deployments with:

* Persistent Volume mounts
* Environment-driven configuration
* ConfigMap integration for storage paths

Mounted storage location:

```text
/app/data
```

---

## Storage Architecture

Stateful services now follow the Kubernetes storage model:

```text
Application
      │
      ▼
Persistent Volume Claim (PVC)
      │
      ▼
Persistent Volume
```

This separates application execution from persistent data storage.

---

## Dynamic Storage Provisioning

The Kubernetes cluster dynamically provisions storage using the default StorageClass.

Advantages:

* Automatic volume provisioning
* Reduced operational overhead
* Production-aligned architecture
* Simplified deployments

---

# Validation

Successfully validated:

* Data persistence after pod deletion
* Automatic pod recreation
* PVC binding
* Volume mounting
* Persistent application data
* Kubernetes self-healing with retained state

---

# Documentation

Updated project documentation to include:

* Persistent storage architecture
* Kubernetes storage concepts
* PVC implementation
* Application configuration improvements

---

# Project Status

| Component                     | Status     |
| ----------------------------- | ---------- |
| IBM MQ                        | ✅ Complete |
| IBM ACE                       | ✅ Complete |
| Patient Service               | ✅ Complete |
| Lab Service                   | ✅ Complete |
| Audit Service                 | ✅ Complete |
| Monitoring Service            | ✅ Complete |
| AI Service                    | ✅ Complete |
| Docker                        | ✅ Complete |
| Docker Compose                | ✅ Complete |
| Kubernetes Deployments        | ✅ Complete |
| Kubernetes Persistent Storage | ✅ Complete |

---

# Architecture Progress

The platform now supports:

* Stateless application containers
* Persistent application data
* Kubernetes self-healing
* Rolling deployments
* Configurable runtime configuration
* Production-oriented storage design

---

# Known Limitations

Current architecture intentionally keeps:

* IBM ACE running outside the Kubernetes cluster
* IBM MQ running outside the Kubernetes cluster

Communication between IBM ACE and Kubernetes services continues through externally accessible endpoints.

Ingress-based routing will be introduced in the next release.

---

# Next Milestone (v1.5)

Planned enhancements:

* NGINX Ingress Controller
* Kubernetes Ingress
* Path-based routing
* Single external endpoint
* Internal service routing
* Production-style networking
* API Gateway architecture foundation

---

# Repository

GitHub Repository:

https://github.com/manibhargava4/healthconnect-ai-platform

---

# Summary

Version **v1.4** represents the successful implementation of persistent storage within the HealthConnect AI Platform. Stateful services now retain application data independently of pod lifecycle events, demonstrating a core cloud-native design principle. This release establishes a strong foundation for advanced Kubernetes networking, ingress, observability, CI/CD automation, and future OpenShift deployment.
