from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_json
from research_core.util.io import read_json, write_json
from research_core.util.types import ValidationError


def build_dataset_registry(data_root: Path, out_path: Path) -> dict[str, Any]:
    manifests = sorted(data_root.rglob("canon.manifest.json"), key=lambda p: str(p.as_posix()))
    if not manifests:
        raise ValidationError(f"No canon.manifest.json files found under data root: {data_root}")

    datasets: list[dict[str, Any]] = []
    for manifest_path in manifests:
        payload = read_json(manifest_path)
        input_files = payload.get("input_files", [])
        first_input = input_files[0] if input_files else {}
        datasets.append(
            {
                "instrument": payload["instrument"],
                "tf": payload["tf"],
                "source_path": first_input.get("path"),
                "source_hash": first_input.get("sha256"),
                "rowcount": payload["rowcount"],
                "start_ts": payload["start_ts"],
                "end_ts": payload["end_ts"],
                "schema_version": payload["schema_version"],
                "colmap_version": payload["colmap_version"],
                "session_policy": payload["session_policy"],
                "output_hashes": payload["output_files"]["canon.parquet"],
                "manifest_path": str(manifest_path),
            }
        )

    datasets_sorted = sorted(datasets, key=lambda x: (x["instrument"], x["tf"], x["source_path"] or ""))
    registry = {
        "registry_version": "v1",
        "datasets": datasets_sorted,
    }
    registry["registry_sha256"] = sha256_json(registry)
    write_json(out_path, registry)
    return registry
