from __future__ import annotations

from typing import Any


def build_integration_summary(
    name: str,
    connector_type: str,
    enabled: bool,
    status: str,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not name or not name.strip():
        raise ValueError("Integration name is required.")

    return {
        "name": name,
        "connector_type": connector_type,
        "enabled": bool(enabled),
        "status": status,
        "metadata": metadata or {},
        "ready": status.lower() in {"connected", "healthy", "ok"},
    }
