from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from research_core.util.hashing import sha256_file
from research_core.util.io import write_json
from research_core.util.time import current_utc_iso8601


def _stable_manifest_path(path: Path) -> str:
    if path.is_absolute():
        try:
            return path.relative_to(Path.cwd()).as_posix()
        except ValueError:
            return path.name
    return path.as_posix()


def write_contract_snapshot(
    path: Path,
    schema_payload: dict[str, Any],
    colmap_payload: dict[str, Any],
    session_policy: str,
    rth_start: str,
    rth_end: str,
    keep_updown: bool,
    include_instrument_tf_columns: bool,
) -> dict[str, Any]:
    payload = {
        "contract_version": "v1",
        "schema_version": schema_payload["schema_version"],
        "colmap_version": colmap_payload["colmap_version"],
        "session_policy": session_policy,
        "rth_start": rth_start,
        "rth_end": rth_end,
        "keep_updown": keep_updown,
        "include_instrument_tf_columns": include_instrument_tf_columns,
        "schema_contract": schema_payload,
        "colmap_contract": colmap_payload,
    }
    write_json(path, payload)
    return payload


def build_manifest(
    run_dir: Path,
    input_files: list[Path],
    canon_df: pd.DataFrame,
    parquet_hashes: dict[str, Any],
    schema_version: str,
    colmap_version: str,
    instrument: str,
    tf: str,
    session_policy: str,
    rth_start: str,
    rth_end: str,
    git_commit: str,
) -> dict[str, Any]:
    canon_path = run_dir / "canon.parquet"
    contract_path = run_dir / "canon.contract.json"
    log_path = run_dir / "logs" / "canon.log"

    sorted_input_files = sorted(input_files, key=lambda p: _stable_manifest_path(p))

    payload: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": current_utc_iso8601(),
        "instrument": instrument,
        "tf": tf,
        "session_policy": session_policy,
        "rth_start": rth_start,
        "rth_end": rth_end,
        "input_files": [
            {
                "bytes": path.stat().st_size,
                "path": _stable_manifest_path(path),
                "sha256": sha256_file(path),
            }
            for path in sorted_input_files
        ],
        "rowcount": int(len(canon_df)),
        "start_ts": canon_df["ts"].iloc[0].isoformat() if not canon_df.empty else None,
        "end_ts": canon_df["ts"].iloc[-1].isoformat() if not canon_df.empty else None,
        "output_files": {
            "canon.parquet": {
                "sha256": parquet_hashes["parquet_bytes_sha256"],
                "canonical_table_sha256": parquet_hashes["canonical_table_sha256"],
                "bytes": canon_path.stat().st_size,
            },
            "canon.contract.json": {
                "sha256": sha256_file(contract_path),
                "bytes": contract_path.stat().st_size,
            },
        },
        "schema_version": schema_version,
        "colmap_version": colmap_version,
        "code_version": {"git_commit": git_commit},
        "determinism_notes": {
            "row_order": "stable sort by ts ascending after fail-loud monotonic check",
            "float_policy": "float64 columns; volume exact as parsed Up+Down",
            "hash_source_of_truth": "canonical_table_sha256 from Arrow IPC stream",
        },
    }

    if log_path.exists():
        payload["output_files"]["canon.log"] = {
            "sha256": sha256_file(log_path),
            "bytes": log_path.stat().st_size,
        }
    return payload


def write_manifest(path: Path, payload: dict[str, Any]) -> None:
    serialized = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ) + "\n"
    path.write_text(serialized, encoding="utf-8")
