from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from research_core.util.io import read_json
from research_core.util.types import ContractError, ValidationError


def load_psa_schema_contract(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    version = payload.get("psa_version")
    if version != "v1":
        raise ContractError(f"Unsupported psa_version: {version}")

    required_columns = payload.get("required_columns")
    if not isinstance(required_columns, list) or not required_columns:
        raise ContractError("PSA schema must declare non-empty required_columns")

    return payload


def validate_canon_input_v1(canon_df: pd.DataFrame) -> None:
    required = ["ts", "instrument", "tf", "open", "high", "low", "close", "volume"]
    missing = [column for column in required if column not in canon_df.columns]
    if missing:
        raise ValidationError(f"Canon schema mismatch: missing required columns {missing}")
