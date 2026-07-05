from fastapi import FastAPI

app = FastAPI()

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
def report_found(phone:str, fraud_type:str, description:str):
    return{
        "message" : "report received",
        "phone" : phone,
        "fraud_type" : fraud_type
    }