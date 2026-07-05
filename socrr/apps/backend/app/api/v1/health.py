from datetime import datetime

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
async def health():
    return {
        "status": "healthy",
        "service": "SOCRR Backend",
        "timestamp": datetime.utcnow().isoformat(),
    }