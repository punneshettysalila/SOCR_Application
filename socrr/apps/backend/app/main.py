from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="SOCRR Enterprise API",
    description="AI-Powered SOC Report Review Platform",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
async def root():
    return {
        "application": "SOCRR Enterprise",
        "version": "0.1.0",
        "status": "running",
    }