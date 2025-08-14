from fastapi import FastAPI
from pydantic import BaseModel
from nlp_utils import generate_prescription

app = FastAPI(title="AI Medical Prescription API")

class PrescriptionRequest(BaseModel):
    patient_info: str
    symptoms: str
    context: str = None  # Optional extra context

class PrescriptionResponse(BaseModel):
    prescription: str

@app.post("/prescribe", response_model=PrescriptionResponse)
def prescribe(request: PrescriptionRequest):
    prompt = f"Patient info: {request.patient_info}\nSymptoms: {request.symptoms}"
    if request.context:
        prompt += f"\nAdditional context: {request.context}"
    prompt += "\nProvide a medical prescription suitable for the patient."

    prescription = generate_prescription(prompt)
    return PrescriptionResponse(prescription=prescription)

@app.get("/health")
def health_check():
    return {"status": "ok"}
