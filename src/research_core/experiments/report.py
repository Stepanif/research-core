from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_file, sha256_json
from research_core.util.io import read_json
from research_core.util.types import ValidationError


def _exp_manifest_hash(payload: dict[str, Any]) -> str:
    return sha256_json({key: value for key, value in payload.items() if key != "exp_manifest_canonical_sha256"})


def _collect_run_ref(run_dir: Path) -> dict[str, str]:
    run_ref: dict[str, str] = {}

    canon_manifest_path = run_dir / "canon.manifest.json"
    if canon_manifest_path.exists():
        canon_manifest = read_json(canon_manifest_path)
        for key in ["instrument", "tf", "session_policy", "rth_start", "rth_end"]:
            value = canon_manifest.get(key)
            if isinstance(value, str) and value:
                run_ref[key] = value

    psa_manifest_path = run_dir / "psa.manifest.json"
    if psa_manifest_path.exists():
        psa_manifest = read_json(psa_manifest_path)
        session = psa_manifest.get("session", {})
        if isinstance(session, dict):
            for key in ["session_policy", "tz", "rth_start", "rth_end"]:
                if key in run_ref:
                    continue
                value = session.get(key)
                if isinstance(value, str) and value:
                    run_ref[key] = value

    return run_ref


def _output_hash_entry(output_name: str, output_info: dict[str, Any]) -> tuple[str, str] | None:
    expected_sha = output_info.get("sha256")
    if not isinstance(expected_sha, str) or not expected_sha:
        return None
    key = f"{output_name.replace('.', '_')}_sha256"
    return key, expected_sha


def compute_experiments_report(run_dir: Path) -> dict[str, Any]:
    experiments_root = run_dir / "experiments"
    index_path = experiments_root / "experiments.index.json"
    if not index_path.exists():
        raise ValidationError(f"Missing required experiments index file: {index_path}")

    index_payload = read_json(index_path)
    if not isinstance(index_payload, dict):
        raise ValidationError(f"Invalid experiments index payload: {index_path}")

    index_version = index_payload.get("index_version")
    if not isinstance(index_version, str) or not index_version:
        raise ValidationError(f"Invalid experiments index_version in {index_path}")

    experiments_block = index_payload.get("experiments")
    if not isinstance(experiments_block, dict):
        raise ValidationError(f"Invalid experiments index.experiments block in {index_path}")

    integrity_checks: list[dict[str, Any]] = []

    integrity_checks.append({"check": "index_file_exists", "pass": True})

    experiments_snapshot: list[dict[str, Any]] = []
    indexed_exp_ids = sorted(experiments_block.keys())
    for exp_id in indexed_exp_ids:
        exp_dir = experiments_root / exp_id
        if not exp_dir.exists() or not exp_dir.is_dir():
            raise ValidationError(f"Indexed experiment directory does not exist for exp_id={exp_id}: {exp_dir}")

        manifest_path = exp_dir / "exp.manifest.json"
        if not manifest_path.exists():
            raise ValidationError(f"Indexed experiment manifest does not exist for exp_id={exp_id}: {manifest_path}")

        manifest_payload = read_json(manifest_path)
        manifest_hash = _exp_manifest_hash(manifest_payload)

        index_entry = experiments_block.get(exp_id)
        if not isinstance(index_entry, dict):
            raise ValidationError(f"Invalid experiments index entry for exp_id={exp_id}")

        indexed_manifest_hash = index_entry.get("manifest_canonical_sha256")
        if isinstance(indexed_manifest_hash, str) and indexed_manifest_hash:
            if indexed_manifest_hash != manifest_hash:
                raise ValidationError(
                    f"Experiment manifest hash mismatch for exp_id={exp_id}: index={indexed_manifest_hash} actual={manifest_hash}"
                )

        output_hashes: dict[str, str] = {}
        outputs = manifest_payload.get("outputs")
        if not isinstance(outputs, dict):
            raise ValidationError(f"Invalid outputs block in experiment manifest for exp_id={exp_id}: {manifest_path}")

        for output_name in sorted(outputs.keys()):
            output_info = outputs[output_name]
            if not isinstance(output_info, dict):
                raise ValidationError(f"Invalid output metadata in manifest for exp_id={exp_id}, output={output_name}")

            expected_sha = output_info.get("sha256")
            if not isinstance(expected_sha, str) or not expected_sha:
                continue

            relative_path = output_info.get("path") if isinstance(output_info.get("path"), str) else output_name
            output_path = exp_dir / relative_path
            if not output_path.exists():
                raise ValidationError(f"Missing experiment output file for exp_id={exp_id}: {output_path}")

            actual_sha = sha256_file(output_path)
            if actual_sha != expected_sha:
                raise ValidationError(
                    f"Experiment output hash mismatch for exp_id={exp_id}, output={output_name}: expected={expected_sha} actual={actual_sha}"
                )

            hash_entry = _output_hash_entry(output_name, output_info)
            if hash_entry is not None:
                key, value = hash_entry
                output_hashes[key] = value

        experiments_snapshot.append(
            {
                "exp_id": exp_id,
                "kind": index_entry.get("kind"),
                "spec_sha256": index_entry.get("spec_sha256"),
                "exp_manifest_canonical_sha256": manifest_hash,
                "created_utc": index_entry.get("created_utc"),
                "outputs": {key: output_hashes[key] for key in sorted(output_hashes.keys())},
            }
        )

    integrity_checks.append({"check": "indexed_experiments_exist", "pass": True})
    integrity_checks.append({"check": "manifest_hash_matches_index", "pass": True})
    integrity_checks.append({"check": "manifest_outputs_match_disk", "pass": True})

    promotions_snapshot: dict[str, Any] = {"labels": []}
    promotions_path = experiments_root / "promotions.json"
    if promotions_path.exists():
        promotions_payload = read_json(promotions_path)
        if not isinstance(promotions_payload, dict):
            raise ValidationError(f"Invalid promotions payload: {promotions_path}")

        promotions_version = promotions_payload.get("promotions_version")
        labels = promotions_payload.get("labels")
        if not isinstance(promotions_version, str) or not promotions_version:
            raise ValidationError(f"Invalid promotions_version in {promotions_path}")
        if not isinstance(labels, dict):
            raise ValidationError(f"Invalid promotions labels in {promotions_path}")

        label_entries = []
        for label in sorted(labels.keys()):
            exp_id = labels[label]
            if not isinstance(exp_id, str) or not exp_id:
                raise ValidationError(f"Invalid promoted exp_id for label={label} in {promotions_path}")
            if exp_id not in experiments_block:
                raise ValidationError(f"Promoted exp_id not present in index for label={label}: {exp_id}")

            manifest_path = experiments_root / exp_id / "exp.manifest.json"
            if not manifest_path.exists():
                raise ValidationError(f"Promoted exp_id manifest missing on disk for label={label}: {manifest_path}")
            label_entries.append({"label": label, "exp_id": exp_id})

        promotions_snapshot = {"promotions_version": promotions_version, "labels": label_entries}

    integrity_checks.append({"check": "promotions_present_in_index_and_disk", "pass": True})

    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Experiment report requires RESEARCH_CREATED_UTC for deterministic created_utc")

    integrity_checks = sorted(integrity_checks, key=lambda item: str(item["check"]))
    report_payload: dict[str, Any] = {
        "report_version": "v1",
        "created_utc": created_utc,
        "run_ref": _collect_run_ref(run_dir),
        "index_snapshot": {
            "index_version": index_version,
            "experiment_count": len(experiments_snapshot),
            "experiments": experiments_snapshot,
        },
        "promotions_snapshot": promotions_snapshot,
        "integrity": {
            "checks": integrity_checks,
            "summary": {"passed": len(integrity_checks), "failed": 0},
        },
    }
    return report_payload
