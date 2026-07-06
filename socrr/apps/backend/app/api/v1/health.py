from datetime import UTC, datetime

from fastapi import APIRouter

from app.core.config.settings import settings

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/")
async def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
        "timestamp": datetime.now(UTC).isoformat(),
    }