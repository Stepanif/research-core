from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from research_core.doctor.contracts import RUN_REQUIRED_FILES
from research_core.doctor.formatting import CheckItem, render_doctor_text
from research_core.util.hashing import sha256_file, sha256_json
from research_core.util.io import read_json


def _canonical_hash_without_self(payload: dict[str, Any], self_key: str) -> str:
    return sha256_json({key: value for key, value in payload.items() if key != self_key})


def _record(section: list[CheckItem], check_id: str, ok: bool, detail: str) -> None:
    section.append(CheckItem(check_id=check_id, ok=ok, detail=detail))


def _verify_manifest_outputs(
    manifest_path: Path,
    outputs_key: str,
    section: list[CheckItem],
    check_prefix: str,
) -> None:
    try:
        payload = read_json(manifest_path)
    except Exception as exc:  # noqa: BLE001
        _record(section, f"{check_prefix}.manifest_json", False, f"invalid json: {exc}")
        return
    outputs = payload.get(outputs_key)
    if not isinstance(outputs, dict):
        _record(section, f"{check_prefix}.outputs_block", False, f"missing/invalid {outputs_key}")
        return

    for output_name in sorted(outputs.keys()):
        output_info = outputs[output_name]
        if not isinstance(output_info, dict):
            _record(section, f"{check_prefix}.output.{output_name}", False, "invalid output metadata")
            continue

        expected_sha = output_info.get("sha256")
        if not isinstance(expected_sha, str) or not expected_sha:
            _record(section, f"{check_prefix}.output.{output_name}", False, "missing sha256")
            continue

        rel_path = output_info.get("path") if isinstance(output_info.get("path"), str) else output_name
        output_path = manifest_path.parent / rel_path
        if not output_path.exists() and "/" not in rel_path:
            alt_log_path = manifest_path.parent / "logs" / rel_path
            if alt_log_path.exists():
                output_path = alt_log_path
                rel_path = f"logs/{rel_path}"
        if not output_path.exists():
            _record(section, f"{check_prefix}.output.{output_name}", False, f"missing {rel_path}")
            continue

        actual_sha = sha256_file(output_path)
        _record(
            section,
            f"{check_prefix}.output.{output_name}",
            actual_sha == expected_sha,
            f"path={rel_path}",
        )


def _verify_optional_canonical_fields(payload: dict[str, Any], section: list[CheckItem], prefix: str) -> None:
    canonical_keys = sorted(
        [
            key
            for key, value in payload.items()
            if isinstance(value, str) and (key == "canonical_json_sha256" or key.endswith("_canonical_sha256"))
        ]
    )
    for key in canonical_keys:
        expected = payload[key]
        actual = _canonical_hash_without_self(payload, key)
        _record(section, f"{prefix}.{key}", actual == expected, "canonical")


def _profile_row_count(profile_payload: dict[str, Any]) -> int | None:
    by_date = profile_payload.get("by_date")
    if not isinstance(by_date, dict):
        return None

    total = 0
    for value in by_date.values():
        if not isinstance(value, dict):
            return None
        bar_count = value.get("bar_count")
        if not isinstance(bar_count, int):
            return None
        total += bar_count
    return total


def _safe_read_json(path: Path, section: list[CheckItem], check_id: str) -> dict[str, Any] | None:
    try:
        payload = read_json(path)
    except Exception as exc:  # noqa: BLE001
        _record(section, check_id, False, f"invalid json: {exc}")
        return None
    if not isinstance(payload, dict):
        _record(section, check_id, False, "payload is not object")
        return None
    return payload


def doctor_run_text(run_dir: Path) -> tuple[str, bool]:
    required: list[CheckItem] = []
    hash_integrity: list[CheckItem] = []
    invariants: list[CheckItem] = []
    optionals: list[CheckItem] = []

    for rel_path in sorted(RUN_REQUIRED_FILES):
        path = run_dir / rel_path
        _record(required, f"required.{rel_path}", path.exists(), rel_path)

    canon_manifest_path = run_dir / "canon.manifest.json"
    psa_manifest_path = run_dir / "psa.manifest.json"
    observe_summary_manifest_path = run_dir / "observe" / "observe.summary.manifest.json"
    observe_profile_manifest_path = run_dir / "observe" / "observe.profile.manifest.json"

    if canon_manifest_path.exists():
        _verify_manifest_outputs(canon_manifest_path, "output_files", hash_integrity, "manifest.canon")
        canon_manifest_payload = _safe_read_json(canon_manifest_path, hash_integrity, "manifest.canon.json_parse")
        if canon_manifest_payload is not None:
            _verify_optional_canonical_fields(canon_manifest_payload, hash_integrity, "manifest.canon")
    if psa_manifest_path.exists():
        psa_manifest = _safe_read_json(psa_manifest_path, hash_integrity, "manifest.psa.json_parse")
        _verify_manifest_outputs(psa_manifest_path, "output_files", hash_integrity, "manifest.psa")
        if psa_manifest is not None:
            _verify_optional_canonical_fields(psa_manifest, hash_integrity, "manifest.psa")

            output_files = psa_manifest.get("output_files", {})
            psa_log_referenced = isinstance(output_files, dict) and "psa.log" in output_files
            if psa_log_referenced:
                _record(optionals, "optional.psa.log_required_by_manifest", (run_dir / "psa.log").exists(), "psa.log")
    if observe_summary_manifest_path.exists():
        summary_manifest = _safe_read_json(observe_summary_manifest_path, hash_integrity, "manifest.observe_summary.json_parse")
        _verify_manifest_outputs(observe_summary_manifest_path, "output_files", hash_integrity, "manifest.observe_summary")
        if summary_manifest is not None:
            _verify_optional_canonical_fields(summary_manifest, hash_integrity, "manifest.observe_summary")
    if observe_profile_manifest_path.exists():
        profile_manifest = _safe_read_json(observe_profile_manifest_path, hash_integrity, "manifest.observe_profile.json_parse")
        _verify_manifest_outputs(observe_profile_manifest_path, "output_files", hash_integrity, "manifest.observe_profile")
        if profile_manifest is not None:
            _verify_optional_canonical_fields(profile_manifest, hash_integrity, "manifest.observe_profile")

    canon_parquet = run_dir / "canon.parquet"
    psa_parquet = run_dir / "psa.parquet"
    if canon_parquet.exists() and psa_parquet.exists():
        canon_rows = len(pd.read_parquet(canon_parquet))
        psa_rows = len(pd.read_parquet(psa_parquet))
        _record(invariants, "invariant.canon_psa_row_count", canon_rows == psa_rows, f"canon={canon_rows} psa={psa_rows}")

        summary_path = run_dir / "observe" / "observe.summary.json"
        if summary_path.exists():
            summary_payload = _safe_read_json(summary_path, invariants, "invariant.observe_summary_json_parse")
            summary_psa_rows = summary_payload.get("psa_coverage", {}).get("row_count") if summary_payload is not None else None
            _record(
                invariants,
                "invariant.observe_summary_psa_row_count",
                isinstance(summary_psa_rows, int) and summary_psa_rows == psa_rows,
                f"summary={summary_psa_rows} psa={psa_rows}",
            )

        profile_path = run_dir / "observe" / "observe.profile.json"
        if profile_path.exists():
            profile_payload = _safe_read_json(profile_path, invariants, "invariant.observe_profile_json_parse")
            profile_rows = _profile_row_count(profile_payload) if profile_payload is not None else None
            _record(
                invariants,
                "invariant.observe_profile_psa_row_count",
                isinstance(profile_rows, int) and profile_rows == psa_rows,
                f"profile={profile_rows} psa={psa_rows}",
            )

    experiments_root = run_dir / "experiments"
    index_path = experiments_root / "experiments.index.json"
    if index_path.exists():
        index_payload = read_json(index_path)
        experiments = index_payload.get("experiments")
        if isinstance(experiments, dict):
            _record(optionals, "optional.experiments.index_present", True, "experiments/experiments.index.json")
            for exp_id in sorted(experiments.keys()):
                exp_entry = experiments.get(exp_id)
                manifest_path = experiments_root / exp_id / "exp.manifest.json"
                if not isinstance(exp_entry, dict):
                    _record(optionals, f"optional.experiments.index.entry.{exp_id}", False, "invalid index entry")
                    continue
                if not manifest_path.exists():
                    _record(optionals, f"optional.experiments.manifest.{exp_id}", False, f"missing experiments/{exp_id}/exp.manifest.json")
                    continue

                manifest_payload = read_json(manifest_path)
                expected = exp_entry.get("manifest_canonical_sha256")
                actual = _canonical_hash_without_self(manifest_payload, "exp_manifest_canonical_sha256")
                _record(optionals, f"optional.experiments.index_manifest_hash.{exp_id}", isinstance(expected, str) and expected == actual, exp_id)

                outputs = manifest_payload.get("outputs")
                if isinstance(outputs, dict):
                    for output_name in sorted(outputs.keys()):
                        output_info = outputs[output_name]
                        if not isinstance(output_info, dict):
                            _record(optionals, f"optional.experiments.output.{exp_id}.{output_name}", False, "invalid output metadata")
                            continue
                        expected_output_sha = output_info.get("sha256")
                        if not isinstance(expected_output_sha, str) or not expected_output_sha:
                            _record(optionals, f"optional.experiments.output.{exp_id}.{output_name}", False, "missing sha256")
                            continue
                        rel_path = output_info.get("path") if isinstance(output_info.get("path"), str) else output_name
                        output_path = manifest_path.parent / rel_path
                        if not output_path.exists():
                            _record(optionals, f"optional.experiments.output.{exp_id}.{output_name}", False, f"missing {exp_id}/{rel_path}")
                            continue
                        _record(
                            optionals,
                            f"optional.experiments.output.{exp_id}.{output_name}",
                            sha256_file(output_path) == expected_output_sha,
                            f"{exp_id}/{rel_path}",
                        )
                else:
                    _record(optionals, f"optional.experiments.outputs.{exp_id}", False, "invalid outputs block")
        else:
            _record(optionals, "optional.experiments.index_present", False, "invalid experiments.index.json")

    promotions_candidates = [
        experiments_root / "experiments.promotions.json",
        experiments_root / "promotions.json",
    ]
    promotions_path = next((path for path in promotions_candidates if path.exists()), None)
    if promotions_path is not None:
        promotions_payload = read_json(promotions_path)
        labels = promotions_payload.get("labels")
        if not isinstance(labels, dict):
            _record(optionals, f"optional.experiments.promotions.{promotions_path.name}", False, "invalid labels")
        else:
            index_payload = read_json(index_path) if index_path.exists() else {}
            index_experiments = index_payload.get("experiments") if isinstance(index_payload, dict) else {}
            for label in sorted(labels.keys()):
                exp_id = labels[label]
                ok = isinstance(exp_id, str) and isinstance(index_experiments, dict) and exp_id in index_experiments
                _record(optionals, f"optional.experiments.promotions.{label}", ok, f"{label}->{exp_id}")

    report_path = experiments_root / "experiments.report.json"
    report_manifest_path = experiments_root / "experiments.report.manifest.json"
    if report_path.exists() or report_manifest_path.exists():
        pair_ok = report_path.exists() and report_manifest_path.exists()
        _record(optionals, "optional.experiments.report_pair", pair_ok, "experiments.report.json + manifest")
        if pair_ok:
            report_manifest = read_json(report_manifest_path)
            _verify_manifest_outputs(report_manifest_path, "outputs", optionals, "optional.experiments.report_manifest")
            _verify_optional_canonical_fields(report_manifest, optionals, "optional.experiments.report_manifest")

    all_checks = required + hash_integrity + invariants + optionals
    all_ok = all(item.ok for item in all_checks)
    result = [CheckItem(check_id="result", ok=all_ok, detail="PASS" if all_ok else "FAIL")]

    text = render_doctor_text(
        input_lines=[f"run={run_dir.as_posix()}"],
        required=required,
        hash_integrity=hash_integrity,
        invariants=invariants,
        optionals=optionals,
        result=result,
    )
    return text, all_ok
