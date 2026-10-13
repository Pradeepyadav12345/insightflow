from app.services.integration_service import build_integration_summary
from app.services.monitoring_service import build_system_health
from app.services.scheduler_service import create_schedule


def test_build_integration_summary_returns_status_and_type() -> None:
    summary = build_integration_summary(
        name="salesforce",
        connector_type="crm",
        enabled=True,
        status="connected",
    )

    assert summary["name"] == "salesforce"
    assert summary["connector_type"] == "crm"
    assert summary["status"] == "connected"
    assert summary["enabled"] is True


def test_create_schedule_generates_cron_and_job_metadata() -> None:
    schedule = create_schedule(
        name="daily-sales-sync",
        cron_expression="0 2 * * *",
        job_type="etl",
        organization_id="org-123",
    )

    assert schedule["name"] == "daily-sales-sync"
    assert schedule["cron_expression"] == "0 2 * * *"
    assert schedule["job_type"] == "etl"
    assert schedule["organization_id"] == "org-123"
    assert schedule["status"] == "active"


def test_build_system_health_reports_ready_state() -> None:
    health = build_system_health()

    assert health["status"] == "healthy"
    assert health["services"]["backend"] == "ok"
    assert health["services"]["database"] in {"ok", "pending"}
