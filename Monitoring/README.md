# Monitoring Service

## Overview

Monitoring Service provides operational visibility into IBM MQ resources.

Port:

```text
5000
```

## Features

* Queue Monitoring
* Queue History
* Trend Analysis
* Incident Detection
* Alert Generation

## APIs

```http
GET /monitor/queues
GET /monitor/history
GET /monitor/trends
GET /monitor/incidents
```

## Monitored Queues

```text
REQUEST.Q
RESPONSE.Q
BOQ.REQUEST.Q
HCQM.DLQ
```

## Components

```text
monitor_api.py
mq_monitor.py
queue_monitor.py
```

## Purpose

Provides observability and monitoring capabilities for the platform.
