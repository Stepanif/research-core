from __future__ import annotations

import os
from datetime import datetime, timezone


def current_utc_iso8601() -> str:
    override = os.getenv("RESEARCH_CREATED_UTC")
    if override:
        return override
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
