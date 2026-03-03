from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any, cast

from research_core.baselines.resolve import resolve_baseline
from research_core.ci_doctor.runner import run_ci_doctor
from research_core.pilot.config import load_pilot_ops_config
from research_core.pilot.explicit import build_explicit_runset_spec, explicit_runset_spec_sha256
from research_core.pilot.writer import build_pilot_summary, write_pilot_artifacts
from research_core.risk.drift import run_risk_drift
from research_core.risk.sweep import run_risk_sweep
from research_core.runsets.catalog import create_runset, list_runsets, validate_runset
from research_core.runsets.ids import runset_id_from_fingerprint
from research_core.runsets.io import canonical_hash, read_json, write_canonical_json
from research_core.runsets.spec import load_runset_spec
from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_file
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="pilot run requires RESEARCH_CREATED_UTC")


def _baseline_paths(baseline_root: Path, runset_id: str) -> tuple[Path, Path]:
    runset_dir = baseline_root / runset_id
    return runset_dir / "baseline.card.json", runset_dir / "baseline.card.manifest.json"


def _verify_baseline_card_manifest(*, baseline_card_path: Path, baseline_manifest_path: Path) -> bool:
    if not baseline_card_path.exists() or not baseline_card_path.is_file():
        return False
    if not baseline_manifest_path.exists() or not baseline_manifest_path.is_file():
        return False

    manifest_payload = read_json(baseline_manifest_path)

    outputs = manifest_payload.get("outputs")
    if not isinstance(outputs, dict):
        return False
    outputs_obj = cast(dict[str, Any], outputs)
    card_output = outputs_obj.get("baseline.card.json")
    if not isinstance(card_output, dict):
        return False
    card_output_obj = cast(dict[str, Any], card_output)

    expected_card_sha = card_output_obj.get("sha256")
    if not isinstance(expected_card_sha, str) or not expected_card_sha:
        return False

    actual_card_sha = sha256_file(baseline_card_path)
    if actual_card_sha != expected_card_sha:
        return False

    expected_manifest_hash = manifest_payload.get("baseline_card_manifest_canonical_sha256")
    actual_manifest_hash = canonical_hash(manifest_payload, self_field="baseline_card_manifest_canonical_sha256")
    if not isinstance(expected_manifest_hash, str) or expected_manifest_hash != actual_manifest_hash:
        return False

    return True


def _read_baseline_id(baseline_card_path: Path) -> str:
    payload = read_json(baseline_card_path)
    checksums = payload.get("checksums")
    if not isinstance(checksums, dict):
        raise ValidationError(f"Invalid baseline card checksums: {baseline_card_path}")
    checksums_obj = cast(dict[str, Any], checksums)
    baseline_id = checksums_obj.get("per_run_vector_sha256")
    if not isinstance(baseline_id, str) or not baseline_id:
        raise ValidationError(f"Missing checksums.per_run_vector_sha256 in baseline card: {baseline_card_path}")
    return baseline_id


def _replace_dir(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(src.as_posix(), dst.as_posix())


def _cleanup_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def run_pilot(*, config_path: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    config = load_pilot_ops_config(config_path)

    catalog_dir = config["catalog_dir"]
    datasets_path = config["datasets_path"]
    baseline_root = config["baseline_root"]
    label = config["label"]
    out_dir = config["out_dir"]
    drift_subdir = config["drift_out_subdir"]
    doctor_subdir = config["doctor_out_subdir"]

    staging_dir = out_dir.with_name(f"{out_dir.name}.staging")
    internal_dir = staging_dir / ".pilot_internal"
    drift_stage_root = staging_dir / drift_subdir
    doctor_stage_root = staging_dir / doctor_subdir

    failures: list[dict[str, str]] = []
    runset_id = "UNKNOWN"
    baseline_id = "UNKNOWN"
    generated_runset_spec_sha = ""

    baseline_card_path = baseline_root / runset_id / "baseline.card.json"
    drift_report_rel = f"{drift_subdir}/{runset_id}/drift.report.json"
    doctor_summary_rel = f"{doctor_subdir}/ci.doctor.summary.json"

    failure_detail = ""

    _cleanup_dir(staging_dir)

    try:
        internal_dir.mkdir(parents=True, exist_ok=True)

        generated_spec = build_explicit_runset_spec(catalog_dir=catalog_dir, datasets_path=datasets_path)
        generated_runset_spec_sha = explicit_runset_spec_sha256(generated_spec)

        generated_spec_path = internal_dir / "generated.runset.explicit.json"
        write_canonical_json(generated_spec_path, generated_spec)

        normalized_spec = load_runset_spec(generated_spec_path)
        fingerprint = normalized_spec.get("fingerprint")
        if not isinstance(fingerprint, dict):
            raise ValidationError("Pilot run failed: generated runset fingerprint missing")
        fingerprint_obj = cast(dict[str, Any], fingerprint)

        runset_id = runset_id_from_fingerprint(fingerprint_obj)
        baseline_card_path, baseline_manifest_path = _baseline_paths(baseline_root, runset_id)
        drift_report_rel = f"{drift_subdir}/{runset_id}/drift.report.json"

        known_runsets = {row["runset_id"] for row in list_runsets(catalog_root=catalog_dir)}
        if runset_id not in known_runsets:
            created = create_runset(catalog_root=catalog_dir, spec_path=generated_spec_path)
            created_runset_id = str(created.get("runset_id", ""))
            if created_runset_id != runset_id:
                raise ValidationError("Pilot run failed: runset_id mismatch after create")

        valid, text = validate_runset(catalog_root=catalog_dir, runset_id=runset_id)
        if not valid:
            raise ValidationError(text)

        if not _verify_baseline_card_manifest(
            baseline_card_path=baseline_card_path,
            baseline_manifest_path=baseline_manifest_path,
        ):
            run_risk_sweep(catalog_dir=catalog_dir, runset_id=runset_id, out_dir=baseline_root)
            if not _verify_baseline_card_manifest(
                baseline_card_path=baseline_card_path,
                baseline_manifest_path=baseline_manifest_path,
            ):
                raise ValidationError("Pilot run failed: baseline.card.manifest.json did not verify after risk sweep")

        current_baseline_id = _read_baseline_id(baseline_card_path)
        try:
            resolved = resolve_baseline(root=baseline_root, runset_id=runset_id, label=label)
            baseline_id = str(resolved["baseline_id"])
        except Exception as exc:  # noqa: BLE001
            raise ValidationError(
                "Missing promoted baseline for label="
                + f"{label} runset_id={runset_id}. "
                + "Run: python -m research_core.cli baseline promote "
                + f"--root {baseline_root.as_posix()} --runset {runset_id} "
                + f"--baseline-id {current_baseline_id} --label {label}"
            ) from exc

        run_risk_drift(
            catalog_dir=catalog_dir,
            baseline_root=baseline_root,
            runset_id=runset_id,
            label=label,
            out_dir=drift_stage_root,
        )

        runsets_path = internal_dir / "runsets.single.json"
        write_canonical_json(runsets_path, {"runset_ids": [runset_id]})

        doctor_config_path = internal_dir / "doctor.config.json"
        write_canonical_json(
            doctor_config_path,
            {
                "doctor_version": "v1",
                "catalog_dir": catalog_dir.as_posix(),
                "baseline_root": baseline_root.as_posix(),
                "runsets_path": runsets_path.as_posix(),
                "out_dir": doctor_stage_root.as_posix(),
                "label": label,
                "checks": {
                    "verify_baseline_root": True,
                    "verify_promotions": True,
                    "verify_runsets": True,
                    "verify_bundles": False,
                    "verify_dashboard": False,
                },
            },
        )

        doctor_result = run_ci_doctor(config_path=doctor_config_path)
        if doctor_result["status"] != "PASS":
            raise ValidationError(f"Pilot run failed: ci doctor status={doctor_result['status']}")
        manifest_inputs: list[Path]
        out_dir.mkdir(parents=True, exist_ok=True)
        _replace_dir(drift_stage_root, out_dir / drift_subdir)
        _replace_dir(doctor_stage_root, out_dir / doctor_subdir)

        if baseline_id == "UNKNOWN":
            baseline_id = current_baseline_id

        manifest_inputs = [
            datasets_path,
            catalog_dir / "links" / "dataset_to_runs.index.json",
            catalog_dir / "runsets" / "entries" / f"{runset_id}.json",
            baseline_card_path,
            baseline_manifest_path,
            out_dir / drift_subdir / runset_id / "drift.report.json",
            out_dir / doctor_subdir / "ci.doctor.summary.json",
        ]

    except Exception as exc:  # noqa: BLE001
        failures.append({"stage": "pilot_run", "detail": str(exc)})
        failure_detail = str(exc)
        _cleanup_dir(staging_dir)

        if baseline_id == "UNKNOWN" and baseline_card_path.exists() and baseline_card_path.is_file():
            try:
                baseline_id = _read_baseline_id(baseline_card_path)
            except Exception:  # noqa: BLE001
                baseline_id = "UNKNOWN"

        manifest_inputs = [
            datasets_path,
            catalog_dir / "links" / "dataset_to_runs.index.json",
            catalog_dir / "runsets" / "entries" / f"{runset_id}.json",
            baseline_card_path,
            baseline_card_path.with_name("baseline.card.manifest.json"),
            out_dir / drift_subdir / runset_id / "drift.report.json",
            out_dir / doctor_subdir / "ci.doctor.summary.json",
        ]

    summary_payload = build_pilot_summary(
        created_utc=created_utc,
        label=label,
        runset_id=runset_id,
        baseline_id=baseline_id,
        baseline_card_path=baseline_card_path.as_posix(),
        drift_report_path=drift_report_rel,
        doctor_summary_path=doctor_summary_rel,
        failures=failures,
        generated_runset_spec_canonical_sha256=generated_runset_spec_sha,
    )
    artifacts = write_pilot_artifacts(out_dir=out_dir, summary_payload=summary_payload, manifest_inputs=manifest_inputs)

    _cleanup_dir(staging_dir)

    return {
        "status": summary_payload["results"]["status"],
        "runset_id": runset_id,
        "baseline_id": baseline_id,
        "failure_detail": failure_detail,
        "drift_report": out_dir / drift_report_rel,
        "doctor_summary": out_dir / doctor_summary_rel,
        "summary_path": artifacts["summary_path"],
        "manifest_path": artifacts["manifest_path"],
    }
