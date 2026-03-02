from __future__ import annotations

import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from research_core.util.types import ValidationError


def get_created_utc(*, required: bool = False, error_message: str | None = None) -> str:
    value = os.getenv("RESEARCH_CREATED_UTC")
    if isinstance(value, str) and value:
        return value
    if required:
        raise ValidationError(error_message or "RESEARCH_CREATED_UTC is required")
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def get_git_commit(repo_root: Path) -> str:
    override = os.getenv("RESEARCH_GIT_COMMIT")
    if isinstance(override, str) and override:
        return override

    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:  # noqa: BLE001
        return "unknown"