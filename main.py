from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FraudReport(BaseModel):
    phone: str
    fraud_type: str
    description: str

@app.get("/health")
def health_deck():
    return{"Status" : "ok", "app" : "payscout"}

@app.get("/check")
def check_number(phone:str):
    return{
        "phone" : phone,
        "risk_score" : 0.0,
        "message" : "no reports found" 
    }

@app.post("/report")
def report_fraud(report: FraudReport):
    return{
        "message" : "report received",
        "phone" : report.phone,
        "fraud_type" : report.fraud_type
    }