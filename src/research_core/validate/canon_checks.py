from __future__ import annotations

from pathlib import Path
from typing import Any

import pyarrow.parquet as pq

from research_core.util.io import read_json, write_json
from research_core.validate.invariants import validate_canon_invariants


def validate_canon_file(
    input_path: Path,
    schema_path: Path,
    out_report_path: Path,
    contract_path: Path | None = None,
) -> dict[str, Any]:
    schema_payload = read_json(schema_path)
    table = pq.read_table(input_path)
    df = table.to_pandas()

    keep_updown = bool("up" in df.columns and "down" in df.columns)
    validate_canon_invariants(df, keep_updown=keep_updown)

    expected = schema_payload["required_columns"]
    if list(df.columns)[: len(expected)] != expected:
        raise ValueError(f"Column order mismatch expected_prefix={expected} actual={list(df.columns)}")

    report: dict[str, Any] = {
        "status": "pass",
        "input": str(input_path),
        "schema_version": schema_payload["schema_version"],
        "rowcount": int(len(df)),
    }

    if contract_path is not None:
        contract_payload = read_json(contract_path)
        report["contract_version"] = contract_payload.get("contract_version", "unknown")

    write_json(out_report_path, report)
    return report
