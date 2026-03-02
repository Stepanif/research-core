from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.experiments.ids import derive_experiment_id
from research_core.experiments.registry import update_experiments_index
from research_core.experiments.spec import load_experiment_spec
from research_core.experiments.transition_matrix import build_transition_matrix_from_psa
from research_core.experiments.writer import (
    build_experiment_manifest,
    ensure_experiment_immutable,
    write_experiment_manifest,
    write_transition_matrix,
)
from research_core.util.types import ValidationError


def _canonical_table_hashes_for_experiment(run_dir: Path) -> tuple[str, str | None]:
    psa_manifest_path = run_dir / "psa.manifest.json"
    if not psa_manifest_path.exists():
        raise ValidationError(f"Missing required psa manifest for experiment run: {psa_manifest_path}")

    psa_manifest = json.loads(psa_manifest_path.read_text(encoding="utf-8"))
    psa_canonical_table_sha256 = psa_manifest.get("output_files", {}).get("psa.parquet", {}).get("canonical_table_sha256")
    if not isinstance(psa_canonical_table_sha256, str) or not psa_canonical_table_sha256:
        raise ValidationError("psa.manifest.json missing output_files.psa.parquet.canonical_table_sha256")

    canon_canonical_table_sha256: str | None = None
    canon_manifest_path = run_dir / "canon.manifest.json"
    if canon_manifest_path.exists():
        canon_manifest = json.loads(canon_manifest_path.read_text(encoding="utf-8"))
        canon_value = canon_manifest.get("output_files", {}).get("canon.parquet", {}).get("canonical_table_sha256")
        if isinstance(canon_value, str) and canon_value:
            canon_canonical_table_sha256 = canon_value

    return psa_canonical_table_sha256, canon_canonical_table_sha256


def run_experiment_from_spec_path(run_dir: Path, spec_path: Path) -> dict[str, Any]:
    spec_payload = load_experiment_spec(spec_path=spec_path)

    psa_table_sha256, canon_table_sha256 = _canonical_table_hashes_for_experiment(run_dir)
    exp_id, _ = derive_experiment_id(
        spec_payload=spec_payload,
        psa_canonical_table_sha256=psa_table_sha256,
        canon_canonical_table_sha256=canon_table_sha256,
    )

    exp_dir = run_dir / "experiments" / exp_id
    exp_exists = exp_dir.exists()

    transition_payload = build_transition_matrix_from_psa(
        psa_path=run_dir / "psa.parquet",
        include_event_bits=bool(spec_payload["params"]["include_event_bits"]),
    )

    manifest_payload = build_experiment_manifest(
        run_dir=run_dir,
        exp_id=exp_id,
        spec_payload=spec_payload,
        transition_matrix_payload=transition_payload,
    )

    if exp_exists:
        ensure_experiment_immutable(exp_dir=exp_dir, expected_manifest_payload=manifest_payload)
    else:
        exp_dir.mkdir(parents=True, exist_ok=True)
        write_transition_matrix(exp_dir / "transition_matrix.json", transition_payload)
        write_experiment_manifest(exp_dir / "exp.manifest.json", manifest_payload)

    update_experiments_index(
        run_dir=run_dir,
        exp_id=exp_id,
        kind=str(spec_payload["kind"]),
        spec_sha256=str(manifest_payload["spec_canonical_sha256"]),
        manifest_canonical_sha256=str(manifest_payload["exp_manifest_canonical_sha256"]),
        created_utc=str(manifest_payload["created_utc"]),
    )

    return {
        "exp_id": exp_id,
        "kind": str(spec_payload["kind"]),
        "spec_payload": spec_payload,
        "manifest_payload": manifest_payload,
    }
