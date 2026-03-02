from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from research_core.psa.contracts import load_psa_schema_contract
from research_core.psa.engine import run_psa_v1
from research_core.util.types import ValidationError


def test_psa_fails_loud_on_canon_schema_mismatch() -> None:
    payload = load_psa_schema_contract(Path("schemas/psa.schema.v1.json"))
    bad_df = pd.DataFrame(
        {
            "ts": pd.to_datetime(["2026-01-01T09:30:00-05:00"]),
            "instrument": ["ES"],
            "tf": ["1min"],
            "open": [100.0],
            "close": [101.0],
            "volume": [10.0],
        }
    )

    with pytest.raises(ValidationError, match="Canon schema mismatch"):
        run_psa_v1(bad_df, payload)
