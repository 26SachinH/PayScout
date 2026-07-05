from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_deck():
    return{"Status" : "ok", "app" : "payscout"}
