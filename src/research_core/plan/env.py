from __future__ import annotations

import json
import platform
import subprocess
import sys
from importlib import metadata
from pathlib import Path
from typing import Any

from research_core.plan.io import canonical_json_bytes
from research_core.util.hashing import sha256_bytes
from research_core.util.types import ValidationError


def _canonical_hash_without_self(payload: dict[str, Any], self_key: str) -> str:
    body = {key: value for key, value in payload.items() if key != self_key}
    return sha256_bytes(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


def _git_commit_or_unknown(repo_root: Path) -> str:
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


def _pip_freeze_sha256() -> str:
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise ValidationError(f"Failed to compute pip freeze fingerprint: {result.stderr.strip()}")

    lines = [line.strip() for line in result.stdout.splitlines()]
    non_empty = sorted([line for line in lines if line])
    canonical = "\n".join(non_empty) + "\n"
    return sha256_bytes(canonical.encode("utf-8"))


def collect_env_fingerprint(repo_root: Path) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "fingerprint_version": "v1",
        "python": {
            "implementation": platform.python_implementation(),
            "version": platform.python_version(),
            "executable_basename": Path(sys.executable).name,
        },
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
        },
        "research_core": {
            "git_commit": _git_commit_or_unknown(repo_root),
        },
        "dependencies": {
            "pip_freeze_sha256": _pip_freeze_sha256(),
        },
    }

    try:
        package_version = metadata.version("research-core")
    except Exception:  # noqa: BLE001
        package_version = None
    if isinstance(package_version, str) and package_version:
        payload["research_core"]["package_version"] = package_version

    payload["fingerprint_canonical_sha256"] = _canonical_hash_without_self(payload, "fingerprint_canonical_sha256")
    return payload


def ensure_env_fingerprint(plan_dir: Path, repo_root: Path) -> str:
    path = plan_dir / "env.fingerprint.json"
    payload = collect_env_fingerprint(repo_root)
    fingerprint_hash = str(payload["fingerprint_canonical_sha256"])

    if path.exists():
        existing = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(existing, dict):
            raise ValidationError(f"Invalid existing env fingerprint payload: {path}")
        existing_hash = existing.get("fingerprint_canonical_sha256")
        recomputed_existing_hash = _canonical_hash_without_self(existing, "fingerprint_canonical_sha256")
        if not isinstance(existing_hash, str) or existing_hash != recomputed_existing_hash:
            raise ValidationError(f"Existing env fingerprint hash mismatch: {path}")
        if existing_hash != fingerprint_hash:
            raise ValidationError("Environment fingerprint mismatch for plan directory (immutability violation)")
        return fingerprint_hash

    path.write_bytes(canonical_json_bytes(payload))
    return fingerprint_hash
