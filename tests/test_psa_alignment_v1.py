from __future__ import annotations

from pathlib import Path

import pandas as pd

from research_core.psa.contracts import load_psa_schema_contract
from research_core.psa.engine import run_psa_v1


def test_alignment_close_open_rule_v1() -> None:
    payload = load_psa_schema_contract(Path("schemas/psa.schema.v1.json"))
    df = pd.DataFrame(
        {
            "ts": pd.to_datetime([
                "2026-01-01T09:30:00-05:00",
                "2026-01-01T09:31:00-05:00",
                "2026-01-01T09:32:00-05:00",
            ]),
            "instrument": ["ES", "ES", "ES"],
            "tf": ["1min", "1min", "1min"],
            "open": [100.0, 100.0, 100.0],
            "high": [101.0, 101.0, 101.0],
            "low": [99.0, 99.0, 99.0],
            "close": [101.0, 99.0, 100.0],
            "volume": [10.0, 11.0, 12.0],
        }
    )

    output = run_psa_v1(df, payload)
    assert list(output["a"]) == ["BULL", "BEAR", "DOJI"]
