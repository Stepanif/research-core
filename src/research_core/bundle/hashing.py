from __future__ import annotations

from typing import Any

from research_core.util.hashing import sha256_bytes
from research_core.util.io import canonical_json_bytes


def canonical_json_sha256(payload: dict[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(payload))
