# Lab Service

## Overview

Lab Service processes laboratory requests and manages laboratory results.

Port:

```text
5002
```

## Features

* Create Lab Results
* Retrieve Lab Results
* Retrieve Lab Result By ID

## Storage

```text
results.json
```

## APIs

```http
POST /lab/results
GET /lab/results
GET /lab/results/{resultId}
```

## Dependencies

* Flask

## Used By

```text
HealthConnectLabIntegration
```
