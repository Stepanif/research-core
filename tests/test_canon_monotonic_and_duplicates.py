from __future__ import annotations

from pathlib import Path

import pytest

from research_core.canon.normalize import canonicalize_file
from research_core.util.types import ParseError


def test_duplicate_timestamp_fails_loud() -> None:
    with pytest.raises(ParseError, match="Duplicate timestamps"):
        canonicalize_file(
            input_path=Path("tests/fixtures/raw_duplicate_ts.txt"),
            schema_path=Path("schemas/canon.schema.v1.json"),
            colmap_path=Path("schemas/colmap.raw_vendor_v1.json"),
            instrument="ES",
            tf="1min",
            session_policy="full",
            rth_start="09:30",
            rth_end="16:00",
            keep_updown=False,
        )


def test_non_monotonic_input_fails_loud(tmp_path: Path) -> None:
    raw = tmp_path / "raw_non_monotonic.txt"
    raw.write_text(
        "Date,Time,Open,High,Low,Close,Up,Down\n"
        "03/07/2024,09:31,100.0,101.0,99.5,100.5,10,5\n"
        "03/07/2024,09:30,100.5,101.5,100.2,101.0,12,7\n",
        encoding="utf-8",
    )

    with pytest.raises(ParseError, match="non-monotonic"):
        canonicalize_file(
            input_path=raw,
            schema_path=Path("schemas/canon.schema.v1.json"),
            colmap_path=Path("schemas/colmap.raw_vendor_v1.json"),
            instrument="ES",
            tf="1min",
            session_policy="full",
            rth_start="09:30",
            rth_end="16:00",
            keep_updown=False,
        )
