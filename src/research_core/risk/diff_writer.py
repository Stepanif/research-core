from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.risk.contracts import BASELINE_DIFF_MANIFEST_VERSION, REQUIRED_ENV_VAR_CREATED_UTC
from research_core.risk.diff import compare_baseline_cards
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Risk operations require RESEARCH_CREATED_UTC")


def _load_baseline_card(path: Path, name: str) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Risk diff input missing file for {name}: {path}")
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Risk diff input invalid JSON object for {name}: {path}")
    card_version = payload.get("card_version")
    if card_version != "v1":
        raise ValidationError(f"Risk diff requires baseline card_version v1 for {name}")
    return payload


def write_baseline_diff_artifacts(*, a_path: Path, b_path: Path, out_dir: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()

    a_card = _load_baseline_card(a_path, "a")
    b_card = _load_baseline_card(b_path, "b")

    diff_payload = compare_baseline_cards(a_card=a_card, b_card=b_card, created_utc=created_utc)
    diff_payload["baseline_diff_canonical_sha256"] = canonical_hash(
        diff_payload,
        self_field="baseline_diff_canonical_sha256",
    )

    diff_bytes = canonical_json_bytes(diff_payload)

    manifest_payload: dict[str, Any] = {
        "manifest_version": BASELINE_DIFF_MANIFEST_VERSION,
        "created_utc": created_utc,
        "inputs": [
            {
                "path": "a",
                "sha256": sha256_file(a_path),
                "bytes": int(a_path.stat().st_size),
            },
            {
                "path": "b",
                "sha256": sha256_file(b_path),
                "bytes": int(b_path.stat().st_size),
            },
        ],
        "outputs": {
            "baseline.diff.json": {
                "sha256": sha256_bytes(diff_bytes),
                "bytes": len(diff_bytes),
            }
        },
    }
    manifest_payload["baseline_diff_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="baseline_diff_manifest_canonical_sha256",
    )

    diff_path = out_dir / "baseline.diff.json"
    manifest_path = out_dir / "baseline.diff.manifest.json"

    diff_tmp_path = out_dir / "baseline.diff.json.tmp"
    manifest_tmp_path = out_dir / "baseline.diff.manifest.json.tmp"

    out_dir.mkdir(parents=True, exist_ok=True)
    diff_tmp_path.write_bytes(diff_bytes)
    write_canonical_json(manifest_tmp_path, manifest_payload)

    diff_tmp_path.replace(diff_path)
    manifest_tmp_path.replace(manifest_path)

    return {
        "diff": diff_payload,
        "manifest": manifest_payload,
        "diff_path": diff_path,
        "manifest_path": manifest_path,
    }
