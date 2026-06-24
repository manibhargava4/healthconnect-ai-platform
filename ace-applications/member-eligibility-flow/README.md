# Member Eligibility Flow

## Purpose

Receives member eligibility requests and publishes validated requests to IBM MQ for downstream processing.

## Components

- HTTP Input Node
- Compute Node
- MQ Output Node
- HTTP Reply Node

## Sample Request

{
  "memberId": "123456",
  "firstName": "John",
  "lastName": "Doe",
  "dob": "1990-01-01"
}

## Sample Response

{
  "status": "SUCCESS",
  "message": "Eligibility request accepted",
  "requestId": "REQ123456"
}