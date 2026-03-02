from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_file, sha256_json
from research_core.util.io import read_json, write_json
from research_core.util.types import ValidationError


def build_run_index(runs_root: Path, out_path: Path) -> dict[str, Any]:
    manifests = sorted(runs_root.rglob("canon.manifest.json"), key=lambda p: str(p.as_posix()))
    entries: list[dict[str, Any]] = []
    seen_manifest_hashes: set[str] = set()

    for manifest_path in manifests:
        manifest_payload = read_json(manifest_path)
        contract_path = manifest_path.parent / "canon.contract.json"
        if not contract_path.exists():
            raise ValidationError(f"Missing contract file for run: {manifest_path.parent}")

        manifest_hash = sha256_file(manifest_path)
        if manifest_hash in seen_manifest_hashes:
            raise ValidationError(f"Duplicate manifest hash detected: {manifest_hash}")
        seen_manifest_hashes.add(manifest_hash)

        entries.append(
            {
                "run_dir": str(manifest_path.parent),
                "instrument": manifest_payload["instrument"],
                "tf": manifest_payload["tf"],
                "manifest_hash": manifest_hash,
                "contract_hash": sha256_file(contract_path),
            }
        )

    entries = sorted(entries, key=lambda x: (x["instrument"], x["tf"], x["run_dir"]))
    payload: dict[str, Any] = {
        "index_version": "v1",
        "runs": entries,
    }
    payload["index_sha256"] = sha256_json(payload)
    write_json(out_path, payload)
    return payload
