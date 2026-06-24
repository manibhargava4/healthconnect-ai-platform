# Audit Service

## Overview

Audit Service records audit events generated during healthcare processing workflows.

Port:

```text
5003
```

## Features

* Create Audit Events
* Retrieve Audit Events
* Retrieve Audit Event By ID

## Storage

```text
audit.json
```

## APIs

```http
POST /audit/events
GET /audit/events
GET /audit/events/{eventId}
```

## Dependencies

* Flask

## Used By

```text
LabResponseAuditFlow
```
