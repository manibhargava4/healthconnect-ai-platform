# Member Eligibility Flow

## Objective

Receive a member eligibility request and publish a validated message to IBM MQ for downstream processing.

## Flow

HTTP Input
↓
Validation
↓
Transformation
↓
MQ Output
↓
Response

## Validation Rules

1. memberId must be present
2. firstName must be present
3. lastName must be present
4. dob must be present

## Error Handling

Invalid payload:
HTTP 400

Backend issue:
HTTP 500

## Logging

Log Request ID

Log Member ID

Log Processing Time
