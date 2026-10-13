from fastapi import APIRouter

from app.api.v1.analytics import router as analytics_router
from app.api.v1.analytics import router as analytics_router
from app.api.v1.auth import router as auth_router
from app.api.v1.dashboards import router as dashboards_router
from app.api.v1.datasets import router as datasets_router
from app.api.v1.health import router as health_router
from app.api.v1.integrations import router as integrations_router
from app.api.v1.monitoring import router as monitoring_router
from app.api.v1.orchestration import router as orchestration_router
from app.api.v1.schedules import router as schedules_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(auth_router)
api_router.include_router(datasets_router)
api_router.include_router(analytics_router)
api_router.include_router(orchestration_router)
api_router.include_router(dashboards_router)
api_router.include_router(integrations_router)
api_router.include_router(schedules_router)
api_router.include_router(monitoring_router)
