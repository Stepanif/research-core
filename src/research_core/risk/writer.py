from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import pandas as pd

from research_core.risk.compute import compute_risk_metrics
from research_core.risk.contracts import REQUIRED_ENV_VAR_CREATED_UTC, RISK_MANIFEST_VERSION, RISK_VERSION
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Risk operations require RESEARCH_CREATED_UTC")


def _load_psa_manifest(run_dir: Path) -> dict[str, Any]:
    path = run_dir / "psa.manifest.json"
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Risk run missing psa.manifest.json: {path}")
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError("Risk run invalid psa.manifest.json payload")
    return payload


def _load_psa_df(run_dir: Path) -> pd.DataFrame:
    path = run_dir / "psa.parquet"
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Risk run missing psa.parquet: {path}")
    return pd.read_parquet(path)


def _run_ref(psa_manifest: dict[str, Any], psa_df: pd.DataFrame) -> dict[str, str]:
    session = psa_manifest.get("session")
    if not isinstance(session, dict):
        raise ValidationError("Risk run psa.manifest.json missing session payload")

    instrument_values = sorted(set([str(value) for value in psa_df["instrument"].dropna().tolist()])) if "instrument" in psa_df.columns else []
    tf_values = sorted(set([str(value) for value in psa_df["tf"].dropna().tolist()])) if "tf" in psa_df.columns else []
    if len(instrument_values) != 1 or len(tf_values) != 1:
        raise ValidationError("Risk run requires single instrument and tf in psa.parquet")

    required = {
        "session_policy": session.get("session_policy"),
        "tz": session.get("tz"),
        "rth_start": session.get("rth_start"),
        "rth_end": session.get("rth_end"),
    }
    missing = [key for key, value in required.items() if not isinstance(value, str) or not value]
    if missing:
        raise ValidationError(f"Risk run missing required session fields in psa.manifest.json: {missing}")

    return {
        "instrument": instrument_values[0],
        "tf": tf_values[0],
        "session_policy": str(required["session_policy"]),
        "tz": str(required["tz"]),
        "rth_start": str(required["rth_start"]),
        "rth_end": str(required["rth_end"]),
    }


def _psa_table_sha256(psa_manifest: dict[str, Any]) -> str:
    output_files = psa_manifest.get("output_files")
    if not isinstance(output_files, dict):
        raise ValidationError("Risk run psa.manifest.json missing output_files")
    psa_file = output_files.get("psa.parquet")
    if not isinstance(psa_file, dict):
        raise ValidationError("Risk run psa.manifest.json missing psa.parquet metadata")
    value = psa_file.get("canonical_table_sha256")
    if not isinstance(value, str) or not value:
        raise ValidationError("Risk run psa.manifest.json missing psa.parquet canonical_table_sha256")
    return value


def build_risk_summary(run_dir: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    psa_manifest = _load_psa_manifest(run_dir)
    psa_df = _load_psa_df(run_dir)

    required_columns = ["state_id", "event_mask", "instrument", "tf"]
    missing = [column for column in required_columns if column not in psa_df.columns]
    if missing:
        raise ValidationError(f"Risk run psa.parquet missing required columns: {missing}")

    state_id = [str(value) for value in psa_df["state_id"].tolist()]
    event_mask = [int(value) for value in psa_df["event_mask"].tolist()]

    metrics = compute_risk_metrics(event_mask=event_mask, state_id=state_id)

    summary: dict[str, Any] = {
        "risk_version": RISK_VERSION,
        "created_utc": created_utc,
        "run_ref": _run_ref(psa_manifest, psa_df),
        "inputs": {
            "psa_table_sha256": _psa_table_sha256(psa_manifest),
        },
        "counts": metrics["counts"],
        "event_rates_per_1000": metrics["event_rates_per_1000"],
        "streaks": metrics["streaks"],
        "distributions": metrics["distributions"],
        "instability_score": metrics["instability_score"],
        "invariants": {
            "required_files_present": True,
            "row_count_positive": int(metrics["counts"]["row_count"]) > 0,
        },
    }
    summary["risk_summary_canonical_sha256"] = canonical_hash(summary, self_field="risk_summary_canonical_sha256")
    return summary


def write_risk_artifacts(run_dir: Path) -> dict[str, Any]:
    summary_payload = build_risk_summary(run_dir)

    risk_dir = run_dir / "risk"
    summary_path = risk_dir / "risk.summary.json"
    manifest_path = risk_dir / "risk.summary.manifest.json"

    summary_bytes = canonical_json_bytes(summary_payload)

    psa_parquet_path = run_dir / "psa.parquet"
    psa_manifest_path = run_dir / "psa.manifest.json"

    manifest_payload: dict[str, Any] = {
        "manifest_version": RISK_MANIFEST_VERSION,
        "created_utc": summary_payload["created_utc"],
        "inputs": sorted(
            [
                {
                    "path": "psa.parquet",
                    "bytes": int(psa_parquet_path.stat().st_size),
                    "sha256": sha256_file(psa_parquet_path),
                },
                {
                    "path": "psa.manifest.json",
                    "bytes": int(psa_manifest_path.stat().st_size),
                    "sha256": sha256_file(psa_manifest_path),
                },
            ],
            key=lambda item: str(item["path"]),
        ),
        "outputs": {
            "risk.summary.json": {
                "bytes": len(summary_bytes),
                "sha256": sha256_bytes(summary_bytes),
            }
        },
    }
    manifest_payload["risk_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="risk_manifest_canonical_sha256",
    )

    risk_dir.mkdir(parents=True, exist_ok=True)
    summary_path.write_bytes(summary_bytes)
    write_canonical_json(manifest_path, manifest_payload)

    return {
        "summary": summary_payload,
        "manifest": manifest_payload,
        "summary_path": summary_path,
        "manifest_path": manifest_path,
    }
