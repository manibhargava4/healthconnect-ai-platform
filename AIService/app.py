from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from datetime import datetime

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:8b"

app = FastAPI(
    title="HealthConnect AI Service",
    description="AI-powered Clinical Summary and Incident Analysis",
    version="1.0.0"
)


class ClinicalSummaryRequest(BaseModel):
    patientId: str
    testName: str
    result: str
    unit: str
    referenceRange: str


class IncidentAnalysisRequest(BaseModel):
    queue: str
    depth: int
    consumerStatus: str
    dlqDepth: int
    boqDepth: int



def generate_clinical_summary(payload):

    prompt = f"""
You are a healthcare documentation assistant.

Provide a factual summary of the laboratory result.

Rules:
- Do not diagnose any condition.
- Do not suggest specific diseases.
- Do not prescribe treatment.
- Do not provide medical advice.
- Only compare the result to the reference range and describe whether it is within, below, or above the range.

Lab Result:

Patient ID: {payload.patientId}
Test Name: {payload.testName}
Result: {payload.result}
Unit: {payload.unit}
Reference Range: {payload.referenceRange}

Return a concise summary in 2-4 sentences.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def generate_incident_analysis(payload):

    prompt = f"""
You are an IBM MQ and IBM ACE production support engineer.

Analyze the following operational metrics.

Return:
1. Severity
2. Root Cause
3. Recommendations

Queue: {payload.queue}
Depth: {payload.depth}
Consumer Status: {payload.consumerStatus}
DLQ Depth: {payload.dlqDepth}
BOQ Depth: {payload.boqDepth}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]



def save_clinical_summary(request, summary):

    file_path = "data/clinical_summaries.json"

    record = {
        "patientId": request.patientId,
        "testName": request.testName,
        "result": request.result,
        "unit": request.unit,
        "referenceRange": request.referenceRange,
        "summary": summary,
        "generatedAt": datetime.now().isoformat()
    }

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(record)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)



@app.get("/")
def home():
    return {
        "message": "HealthConnect AI Service"
    }

@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "AIService",
        "provider": "Ollama",
        "model": "qwen3:8b"
    }


@app.post("/ai/clinical-summary")
def clinical_summary(request: ClinicalSummaryRequest):

    summary = generate_clinical_summary(request)

    save_clinical_summary(request, summary)

    return {
        "patientId": request.patientId,
        "summary": summary
    }

@app.post("/ai/incident-analysis")
def incident_analysis(request: IncidentAnalysisRequest):

    analysis = generate_incident_analysis(request)

    return {
        "analysis": analysis
    }