from __future__ import annotations

from typing import Any


def create_schedule(
    name: str,
    cron_expression: str,
    job_type: str,
    organization_id: str,
    status: str = "active",
) -> dict[str, Any]:
    if not name or not name.strip():
        raise ValueError("Schedule name is required.")
    if not cron_expression or not cron_expression.strip():
        raise ValueError("Cron expression is required.")

    return {
        "name": name,
        "cron_expression": cron_expression,
        "job_type": job_type,
        "organization_id": organization_id,
        "status": status,
        "next_run": "next scheduled window",
    }
