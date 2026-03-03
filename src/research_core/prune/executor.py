from __future__ import annotations

from typing import Any

from research_core.util.types import ValidationError


def execute_plan(*, plan: dict[str, Any]) -> dict[str, Any]:
    candidates = plan["delete_candidates"]
    for item in candidates:
        path = item["path"]
        if not path.exists() or not path.is_file():
            raise ValidationError(f"Prune execute preflight failed: candidate missing {path}")

    deleted = 0
    deleted_bytes = 0
    for item in candidates:
        path = item["path"]
        size = int(item["bytes"])
        path.unlink()
        deleted += 1
        deleted_bytes += size

    return {
        "deleted": deleted,
        "deleted_bytes": deleted_bytes,
    }
