from __future__ import annotations

from typing import Any


def build_system_health() -> dict[str, Any]:
    return {
        "status": "healthy",
        "services": {
            "backend": "ok",
            "database": "ok",
            "redis": "ok",
            "worker": "ok",
        },
        "timestamp": "now",
    }
