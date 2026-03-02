from __future__ import annotations

from typing import Any

from research_core.runsets.io import canonical_hash


def runset_id_from_fingerprint(fingerprint: dict[str, Any]) -> str:
    return canonical_hash(fingerprint)
