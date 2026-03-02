from __future__ import annotations

from pathlib import Path

import pytest

from research_core.canon.normalize import canonicalize_file
from research_core.util.types import ParseError


def test_parse_small_sample_schema_and_timezone() -> None:
    fixture = Path("tests/fixtures/raw_small_sample.txt")
    df, _, _ = canonicalize_file(
        input_path=fixture,
        schema_path=Path("schemas/canon.schema.v1.json"),
        colmap_path=Path("schemas/colmap.raw_vendor_v1.json"),
        instrument="ES",
        tf="1min",
        session_policy="full",
        rth_start="09:30",
        rth_end="16:00",
        keep_updown=False,
    )
    assert list(df.columns) == ["ts", "instrument", "tf", "open", "high", "low", "close", "volume"]
    assert str(df["ts"].dtype).endswith("America/New_York]")
    assert len(df) == 3


def test_bad_timestamp_fails_loud() -> None:
    fixture = Path("tests/fixtures/raw_bad_timestamp.txt")
    with pytest.raises(ParseError, match="Timestamp parsing failed"):
        canonicalize_file(
            input_path=fixture,
            schema_path=Path("schemas/canon.schema.v1.json"),
            colmap_path=Path("schemas/colmap.raw_vendor_v1.json"),
            instrument="ES",
            tf="1min",
            session_policy="full",
            rth_start="09:30",
            rth_end="16:00",
            keep_updown=False,
        )


def test_dst_ambiguous_timestamp_fails_loud(tmp_path: Path) -> None:
    raw = tmp_path / "raw_dst_ambiguous.txt"
    raw.write_text(
        "Date,Time,Open,High,Low,Close,Up,Down\n"
        "11/03/2024,01:30,100.0,101.0,99.5,100.5,10,5\n",
        encoding="utf-8",
    )

    with pytest.raises(ParseError, match="timezone localization failed"):
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


def test_missing_numeric_value_fails_loud(tmp_path: Path) -> None:
    raw = tmp_path / "raw_missing.txt"
    raw.write_text(
        "Date,Time,Open,High,Low,Close,Up,Down\n"
        "03/07/2024,09:30,,101.0,99.5,100.5,10,5\n",
        encoding="utf-8",
    )
    with pytest.raises(ParseError, match="Numeric parsing failed"):
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
