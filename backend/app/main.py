from fastapi import FastAPI

app = FastAPI(
    title="TradePilot AI API",
    version="0.1.0",
    description="AI-powered business assistant built with FastAPI and Oracle"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to TradePilot AI 🚀",
        "status": "Running"
    }