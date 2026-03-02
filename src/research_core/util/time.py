from __future__ import annotations

from research_core.util.buildmeta import get_created_utc


def current_utc_iso8601() -> str:
    return get_created_utc(required=False)
