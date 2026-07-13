from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import APP_NAME
from app.api.router import api_router
from app.db.pool import create_pool

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    create_pool()

    yield

    # Shutdown
    print("TradePilot AI shutting down...")

app = FastAPI(
    title="TradePilot AI API",
    version="0.1.0",
    description="AI-powered business assistant built with FastAPI and Oracle",
    lifespan=lifespan
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to TradePilot AI 🚀",
        "status": "Running"
    }
