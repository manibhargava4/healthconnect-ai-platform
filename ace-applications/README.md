# ACE Applications

## Overview

This directory contains all IBM App Connect Enterprise (ACE) applications used by the HealthConnect platform.

Integration Server:

```text
HC_DEV_SERVER
```

## Applications

### HealthConnectPatientAPI

Provides patient API integration.

Main Flow:

```text
GetPatient.msgflow
```

---

### HealthConnectLabIntegration

Handles laboratory request and response processing.

Flows:

```text
LabRequestProducer.msgflow

LabRequestConsumer.msgflow

LabResponseAuditFlow.msgflow
```

---

### HealthConnectAlerting

Handles operational alert generation and processing.

Flows:

```text
PublishAlerts.msgflow

AlertConsumer.msgflow
```

---

### HealthConnectMemberEligibility

Contains monitoring and MQ processing flows.

Flows:

```text
MemberEligibility.msgflow

MQConsumer.msgflow

MQResponseConsumer.msgflow

QueueMonitoringDashboard.msgflow
```

---

### HealthConnectAIAPI

Provides ACE integration with AI Service.

Flows:

```text
AIIncidentAnalysisFlow.msgflow
```

## Technologies

* IBM ACE 13
* ESQL
* HTTP Integration
* IBM MQ Integration
* REST APIs
