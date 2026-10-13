from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    return {
        "status": "ok",
        "service": "insightflow-backend",
        "environment": "development",
        "checks": {
            "database": "pending",
            "redis": "pending",
        },
    }
