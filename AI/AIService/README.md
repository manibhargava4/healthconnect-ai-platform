# AI Service

## Overview

AI Service provides AI-powered healthcare and operational analysis capabilities.

Framework:

```text
FastAPI
```

Port:

```text
5004
```

## AI Provider

```text
Ollama
```

## Model

```text
Qwen3:8b
```

## Features

### Clinical Summary Generation

Generates AI-powered summaries from laboratory results.

### Incident Analysis

Generates AI-powered operational incident analysis.

### Monitoring Analysis

Analyzes monitoring metrics and generates recommendations.

## APIs

```http
GET /health

POST /ai/clinical-summary

POST /ai/incident-analysis

GET /ai/analyze-monitoring

GET /ai/incidents
```

## Storage

```text
clinical_summaries.json
incident_reports.json
```

## Dependencies

* FastAPI
* Requests
* Pydantic
* Ollama
