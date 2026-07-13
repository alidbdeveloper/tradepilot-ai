from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="TradePilot AI API",
    version="0.1.0",
    description="AI-powered business assistant built with FastAPI and Oracle"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to TradePilot AI 🚀",
        "status": "Running"
    }