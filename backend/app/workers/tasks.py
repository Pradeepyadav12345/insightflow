from app.workers.celery_app import celery_app


@celery_app.task(name="insightflow.health_check")
def health_check_task() -> dict:
    return {"status": "ok", "service": "worker"}
