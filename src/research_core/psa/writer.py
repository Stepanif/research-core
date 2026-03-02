from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from research_core.util.hashing import canonical_table_sha256, sha256_file
from research_core.util.time import current_utc_iso8601


def _stable_manifest_path(path: Path, input_root: Path) -> str:
    if input_root.is_dir():
        return path.relative_to(input_root).as_posix()
    return path.name


def psa_arrow_schema() -> pa.Schema:
    return pa.schema(
        [
            pa.field("ts", pa.timestamp("ns", tz="America/New_York"), nullable=False),
            pa.field("instrument", pa.string(), nullable=False),
            pa.field("tf", pa.string(), nullable=False),
            pa.field("open", pa.float64(), nullable=False),
            pa.field("close", pa.float64(), nullable=False),
            pa.field("a", pa.string(), nullable=False),
            pa.field("state_id", pa.string(), nullable=False),
            pa.field("event_mask", pa.int64(), nullable=False),
        ]
    )


def write_psa_parquet(df: pd.DataFrame, output_path: Path) -> dict[str, str | int]:
    table_columns = ["ts", "instrument", "tf", "open", "close", "a", "state_id", "event_mask"]
    table = pa.Table.from_pandas(df[table_columns], schema=psa_arrow_schema(), preserve_index=False)
    pq.write_table(table, output_path, compression="snappy", use_dictionary=False)
    return {
        "parquet_bytes_sha256": sha256_file(output_path),
        "canonical_table_sha256": canonical_table_sha256(table),
        "bytes": output_path.stat().st_size,
    }


def write_psa_log(df: pd.DataFrame, output_path: Path) -> None:
    lines = []
    for row in df.itertuples(index=False):
        lines.append(
            f"{row.ts.isoformat()},{row.instrument},{row.tf},{row.p},{row.s},{row.a},{row.state_id},{int(row.event_mask)}"
        )
    payload = "\n".join(lines) + "\n"
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(payload)


def build_psa_manifest(
    run_dir: Path,
    input_files: list[Path],
    input_root: Path,
    psa_df: pd.DataFrame,
    parquet_hashes: dict[str, Any],
    psa_version: str,
    session_metadata: dict[str, str],
    git_commit: str,
) -> dict[str, Any]:
    psa_path = run_dir / "psa.parquet"
    log_path = run_dir / "psa.log"
    sorted_input_files = sorted(input_files, key=lambda p: _stable_manifest_path(p, input_root))

    payload = {
        "manifest_version": "v1",
        "created_utc": current_utc_iso8601(),
        "psa_version": psa_version,
        "input_files": [
            {
                "bytes": path.stat().st_size,
                "path": _stable_manifest_path(path, input_root),
                "sha256": sha256_file(path),
            }
            for path in sorted_input_files
        ],
        "rowcount": int(len(psa_df)),
        "start_ts": psa_df["ts"].iloc[0].isoformat() if not psa_df.empty else None,
        "end_ts": psa_df["ts"].iloc[-1].isoformat() if not psa_df.empty else None,
        "session": {
            "session_policy": session_metadata["session_policy"],
            "tz": session_metadata["tz"],
            "rth_start": session_metadata["rth_start"],
            "rth_end": session_metadata["rth_end"],
        },
        "output_files": {
            "psa.parquet": {
                "sha256": parquet_hashes["parquet_bytes_sha256"],
                "canonical_table_sha256": parquet_hashes["canonical_table_sha256"],
                "bytes": psa_path.stat().st_size,
            }
        },
        "code_version": {"git_commit": git_commit},
        "determinism_notes": {
            "alignment_rule": "A=BULL if close>open, BEAR if close<open, DOJI if close==open",
            "hash_source_of_truth": "canonical_table_sha256 from Arrow IPC stream",
        },
    }

    if log_path.exists():
        payload["output_files"]["psa.log"] = {
            "sha256": sha256_file(log_path),
            "bytes": log_path.stat().st_size,
        }
    return payload


def write_psa_manifest(path: Path, payload: dict[str, Any]) -> None:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    path.write_text(serialized, encoding="utf-8")
