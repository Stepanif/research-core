from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_bytes, sha256_file

PROJECT_VERSION = "v1"
PROJECT_TOOL_VERSION = "v1"
PROJECT_MANIFEST_VERSION = "v1"
PROJECT_REPORT_VERSION = "v1"


def canonical_json_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def canonical_json_sha256(payload: dict[str, Any], self_hash_key: str | None = None) -> str:
    clone = dict(payload)
    if self_hash_key is not None:
        clone.pop(self_hash_key, None)
    return sha256_bytes(
        json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    )


def stable_path_label(path_value: str) -> str:
    return Path(path_value).as_posix()


def file_entry(path_label: str, file_path: Path) -> dict[str, Any]:
    return {
        "path": path_label,
        "bytes": file_path.stat().st_size,
        "sha256": sha256_file(file_path),
    }
