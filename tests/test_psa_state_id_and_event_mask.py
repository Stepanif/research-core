from __future__ import annotations

from pathlib import Path

import pandas as pd

from research_core.psa.contracts import (
    EVENT_A_CHANGE,
    EVENT_A_FLIP,
    EVENT_P_CHANGE,
    EVENT_P_FLIP,
    EVENT_STATE_CHANGE,
    load_psa_schema_contract,
)
from research_core.psa.engine import run_psa_v1


def test_state_id_and_event_mask_exact_values() -> None:
    payload = load_psa_schema_contract(Path("schemas/psa.schema.v1.json"))
    canon_df = pd.DataFrame(
        {
            "ts": pd.to_datetime(
                [
                    "2026-01-01T09:30:00-05:00",
                    "2026-01-01T09:31:00-05:00",
                    "2026-01-01T09:32:00-05:00",
                    "2026-01-01T09:33:00-05:00",
                ]
            ),
            "instrument": ["ES", "ES", "ES", "ES"],
            "tf": ["1min", "1min", "1min", "1min"],
            "open": [100.0, 100.0, 100.0, 100.0],
            "high": [101.0, 101.0, 101.0, 101.0],
            "low": [99.0, 99.0, 99.0, 99.0],
            "close": [100.0, 101.0, 99.0, 100.0],
            "volume": [10.0, 10.0, 10.0, 10.0],
        }
    )

    output = run_psa_v1(canon_df, payload)

    assert list(output["state_id"]) == [
        "PSA.v1|P=CONST|S=FLAT|A=DOJI",
        "PSA.v1|P=UP|S=FLAT|A=BULL",
        "PSA.v1|P=DOWN|S=FLAT|A=BEAR",
        "PSA.v1|P=UP|S=FLAT|A=DOJI",
    ]

    expected = [
        0,
        EVENT_STATE_CHANGE | EVENT_P_CHANGE | EVENT_A_CHANGE,
        EVENT_STATE_CHANGE | EVENT_P_CHANGE | EVENT_A_CHANGE | EVENT_P_FLIP | EVENT_A_FLIP,
        EVENT_STATE_CHANGE | EVENT_P_CHANGE | EVENT_A_CHANGE | EVENT_P_FLIP,
    ]
    assert list(output["event_mask"]) == expected
