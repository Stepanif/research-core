from __future__ import annotations

from pathlib import Path

import pytest

from research_core.canon.normalize import canonicalize_file
from research_core.util.types import ValidationError


def test_bad_ohlc_fails_loud() -> None:
    with pytest.raises(ValidationError, match="Invalid OHLC"):
        canonicalize_file(
            input_path=Path("tests/fixtures/raw_bad_ohlc.txt"),
            schema_path=Path("schemas/canon.schema.v1.json"),
            colmap_path=Path("schemas/colmap.raw_vendor_v1.json"),
            instrument="ES",
            tf="1min",
            session_policy="full",
            rth_start="09:30",
            rth_end="16:00",
            keep_updown=False,
        )
