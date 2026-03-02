from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.util.io import read_json
from research_core.util.types import ValidationError


def _experiments_root(run_dir: Path) -> Path:
    return run_dir / "experiments"


def experiments_index_path(run_dir: Path) -> Path:
    return _experiments_root(run_dir) / "experiments.index.json"


def list_experiment_ids(run_dir: Path) -> list[str]:
    root = _experiments_root(run_dir)
    if not root.exists():
        return []

    return sorted(
        [
            path.name
            for path in root.iterdir()
            if path.is_dir() and (path / "exp.manifest.json").exists()
        ]
    )


def _run_ref(run_dir: Path) -> dict[str, str]:
    canon_manifest = run_dir / "canon.manifest.json"
    if not canon_manifest.exists():
        return {}

    payload = read_json(canon_manifest)
    run_ref: dict[str, str] = {}
    instrument = payload.get("instrument")
    tf = payload.get("tf")
    if isinstance(instrument, str) and instrument:
        run_ref["instrument"] = instrument
    if isinstance(tf, str) and tf:
        run_ref["tf"] = tf
    return run_ref


def _load_or_init_index(run_dir: Path) -> dict[str, Any]:
    path = experiments_index_path(run_dir)
    if not path.exists():
        return {
            "index_version": "v1",
            "run_ref": _run_ref(run_dir),
            "experiments": {},
        }

    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid experiments index payload: {path}")
    if payload.get("index_version") != "v1":
        raise ValidationError(f"Unsupported experiments index version in {path}")
    if not isinstance(payload.get("experiments"), dict):
        raise ValidationError(f"Invalid experiments index.experiments block: {path}")
    if not isinstance(payload.get("run_ref"), dict):
        raise ValidationError(f"Invalid experiments index.run_ref block: {path}")
    return payload


def update_experiments_index(
    run_dir: Path,
    exp_id: str,
    kind: str,
    spec_sha256: str,
    manifest_canonical_sha256: str,
    created_utc: str,
) -> dict[str, Any]:
    index_payload = _load_or_init_index(run_dir)
    experiments = index_payload["experiments"]

    entry = {
        "kind": kind,
        "spec_sha256": spec_sha256,
        "manifest_canonical_sha256": manifest_canonical_sha256,
        "created_utc": created_utc,
    }

    existing = experiments.get(exp_id)
    if existing is not None and existing != entry:
        raise ValidationError(
            f"Experiments index immutability violation for exp_id={exp_id}: existing entry differs"
        )

    experiments[exp_id] = entry
    sorted_experiments = {key: experiments[key] for key in sorted(experiments.keys())}

    output_payload = {
        "index_version": "v1",
        "run_ref": index_payload.get("run_ref", _run_ref(run_dir)),
        "experiments": sorted_experiments,
    }

    path = experiments_index_path(run_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(output_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    path.write_text(serialized, encoding="utf-8")
    return output_payload


def show_experiment_summary(run_dir: Path, exp_id: str) -> dict[str, Any]:
    manifest_path = _experiments_root(run_dir) / exp_id / "exp.manifest.json"
    if not manifest_path.exists():
        raise ValidationError(f"Experiment manifest not found for exp_id={exp_id}: {manifest_path}")

    manifest = read_json(manifest_path)
    return {
        "exp_id": manifest.get("exp_id"),
        "manifest_version": manifest.get("manifest_version"),
        "spec_canonical_sha256": manifest.get("spec_canonical_sha256"),
        "inputs": manifest.get("inputs"),
        "outputs": manifest.get("outputs"),
        "created_utc": manifest.get("created_utc"),
        "exp_manifest_canonical_sha256": manifest.get("exp_manifest_canonical_sha256"),
    }
