from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from research_core.experiments.runner import run_experiment_from_spec_path
from research_core.experiments.spec import load_experiment_spec
from research_core.util.hashing import sha256_bytes, sha256_file, sha256_json
from research_core.util.io import read_json
from research_core.util.types import ValidationError


def _sorted_spec_files(spec_dir: Path) -> list[Path]:
    if not spec_dir.exists() or not spec_dir.is_dir():
        raise ValidationError(f"Spec directory does not exist: {spec_dir}")
    files = sorted([path for path in spec_dir.iterdir() if path.is_file() and path.suffix.lower() == ".json"], key=lambda p: p.name)
    if not files:
        raise ValidationError(f"No spec JSON files found in spec-dir: {spec_dir}")
    return files


def _run_ref(run_dir: Path) -> dict[str, str]:
    run_ref: dict[str, str] = {}

    canon_manifest_path = run_dir / "canon.manifest.json"
    if canon_manifest_path.exists():
        canon_manifest = read_json(canon_manifest_path)
        for key in ["instrument", "tf", "session_policy"]:
            value = canon_manifest.get(key)
            if isinstance(value, str) and value:
                run_ref[key] = value

    psa_manifest_path = run_dir / "psa.manifest.json"
    if psa_manifest_path.exists() and "session_policy" not in run_ref:
        psa_manifest = read_json(psa_manifest_path)
        session_policy = psa_manifest.get("session", {}).get("session_policy")
        if isinstance(session_policy, str) and session_policy:
            run_ref["session_policy"] = session_policy

    return run_ref


def _batch_manifest_hash_without_self(payload: dict[str, Any]) -> str:
    clone = dict(payload)
    clone.pop("batch_manifest_canonical_sha256", None)
    return sha256_json(clone)


def run_experiment_batch(run_dir: Path, spec_dir: Path, batch_dir: Path) -> dict[str, Any]:
    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Experiment batch requires RESEARCH_CREATED_UTC for deterministic created_utc")

    specs = _sorted_spec_files(spec_dir)

    for spec_path in specs:
        load_experiment_spec(spec_path=spec_path)

    results: list[dict[str, Any]] = []
    for spec_path in specs:
        run_result = run_experiment_from_spec_path(run_dir=run_dir, spec_path=spec_path)

        exp_id = str(run_result["exp_id"])
        exp_dir = run_dir / "experiments" / exp_id
        exp_manifest = read_json(exp_dir / "exp.manifest.json")

        results.append(
            {
                "spec_file": spec_path.name,
                "spec_sha256": sha256_file(spec_path),
                "exp_id": exp_id,
                "kind": str(run_result["kind"]),
                "exp_manifest_canonical_sha256": str(exp_manifest["exp_manifest_canonical_sha256"]),
                "transition_matrix_json_sha256": sha256_file(exp_dir / "transition_matrix.json"),
            }
        )

    summary_payload: dict[str, Any] = {
        "batch_version": "v1",
        "run_ref": _run_ref(run_dir),
        "spec_dir_listing": [path.name for path in specs],
        "results": sorted(results, key=lambda item: str(item["spec_file"])),
        "counts": {"total": len(specs), "succeeded": len(specs), "failed": 0},
        "created_utc": created_utc,
    }

    summary_bytes = (json.dumps(summary_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")

    manifest_payload: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": created_utc,
        "inputs": [
            {
                "path": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
            for path in specs
        ],
        "outputs": {
            "batch.summary.json": {
                "bytes": len(summary_bytes),
                "sha256": sha256_bytes(summary_bytes),
            }
        },
    }
    manifest_payload["batch_manifest_canonical_sha256"] = _batch_manifest_hash_without_self(manifest_payload)

    if batch_dir.exists():
        raise ValidationError(f"Batch output directory already exists: {batch_dir}")

    batch_dir.mkdir(parents=True, exist_ok=False)
    (batch_dir / "batch.summary.json").write_bytes(summary_bytes)
    (batch_dir / "batch.manifest.json").write_text(
        json.dumps(manifest_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    return {
        "summary": summary_payload,
        "manifest": manifest_payload,
    }
