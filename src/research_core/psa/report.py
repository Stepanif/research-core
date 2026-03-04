from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def _canonical_hash(payload: dict[str, Any], self_field: str | None = None) -> str:
    clone = dict(payload)
    if isinstance(self_field, str):
        clone.pop(self_field, None)
    data = json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return sha256_bytes(data)


def _alignment_vector_sha256(alignment: pd.Series) -> str:
    lines = "".join(f"{value}\n" for value in alignment.astype(str).tolist())
    return sha256_bytes(lines.encode("utf-8"))


def _longest_streaks(alignment: pd.Series) -> dict[str, int]:
    values = alignment.astype(str).tolist()
    if not values:
        return {}

    best: dict[str, int] = {}
    current = values[0]
    count = 1
    for item in values[1:]:
        if item == current:
            count += 1
            continue
        best[current] = max(best.get(current, 0), count)
        current = item
        count = 1
    best[current] = max(best.get(current, 0), count)
    return {key: best[key] for key in sorted(best)}


def _transition_matrix(alignment: pd.Series) -> dict[str, dict[str, int]]:
    shifted = alignment.shift(1)
    matrix = pd.crosstab(shifted, alignment)
    output: dict[str, dict[str, int]] = {}
    for row_key in sorted([str(key) for key in matrix.index.tolist()]):
        row = matrix.loc[row_key]
        row_dict: dict[str, int] = {}
        for col_key in sorted([str(key) for key in matrix.columns.tolist()]):
            value = int(row[col_key])
            if value > 0:
                row_dict[col_key] = value
        if row_dict:
            output[row_key] = row_dict
    return output


def build_psa_report(*, run_dir: Path) -> dict[str, Any]:
    created_utc = get_created_utc(required=True, error_message="psa report requires RESEARCH_CREATED_UTC")

    if not run_dir.exists() or not run_dir.is_dir():
        raise ValidationError(f"psa report run directory does not exist: {run_dir}")

    psa_parquet = run_dir / "psa.parquet"
    psa_manifest = run_dir / "psa.manifest.json"

    if not psa_parquet.exists() or not psa_parquet.is_file():
        raise ValidationError(f"psa report missing required file: {psa_parquet}")
    if not psa_manifest.exists() or not psa_manifest.is_file():
        raise ValidationError(f"psa report missing required file: {psa_manifest}")

    df = pd.read_parquet(psa_parquet, columns=["a"])
    if "a" not in df.columns:
        raise ValidationError("psa report requires column 'a' in psa.parquet")

    alignment = df["a"].astype(str)
    counts = alignment.value_counts(dropna=False)
    total = int(len(alignment))
    percents = (counts / total * 100.0).round(6) if total > 0 else counts.astype(float)

    alignment_counts = {str(key): int(value) for key, value in counts.sort_index().items()}
    alignment_percent = {str(key): f"{float(value):.6f}" for key, value in percents.sort_index().items()}

    manifest_payload = json.loads(psa_manifest.read_text(encoding="utf-8"))
    inputs: dict[str, str] = {
        "psa_parquet_sha256": sha256_file(psa_parquet),
        "psa_manifest_sha256": sha256_file(psa_manifest),
    }

    canonical_table_hash = (
        manifest_payload.get("output_files", {})
        .get("psa.parquet", {})
        .get("canonical_table_sha256")
    )
    if isinstance(canonical_table_hash, str) and canonical_table_hash:
        inputs["psa_canonical_table_sha256"] = canonical_table_hash

    report: dict[str, Any] = {
        "report_version": "v1",
        "created_utc": created_utc,
        "run_ref": run_dir.name,
        "inputs": inputs,
        "metrics": {
            "row_count": total,
            "alignment_counts": alignment_counts,
            "alignment_percent": alignment_percent,
            "longest_streaks": _longest_streaks(alignment),
            "transition_matrix_counts": _transition_matrix(alignment),
        },
        "checksums": {
            "alignment_vector_sha256": _alignment_vector_sha256(alignment),
        },
    }
    report["psa_report_canonical_sha256"] = _canonical_hash(report, self_field="psa_report_canonical_sha256")
    return report
