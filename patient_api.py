from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/patient/{patient_id}/vitals")
def get_vitals(patient_id: int):

    return {
        "patient_id": patient_id,
        "heart_rate": random.randint(70,110),
        "oxygen": random.randint(88,99),
        "temperature": round(random.uniform(36.5,38.5),1),
        "blood_pressure": "130/90"
    }


@app.get("/patient/{patient_id}/biomarkers")
def get_biomarkers(patient_id: int):

    return {
        "patient_id": patient_id,
        "CRP": round(random.uniform(1,10),2),
        "WBC": random.randint(5000,15000),
        "hemoglobin": round(random.uniform(9,14),1)
    }