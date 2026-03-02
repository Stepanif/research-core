from __future__ import annotations

from pathlib import Path

from research_core.canon.normalize import canonicalize_file


def test_volume_equals_up_plus_down_exact() -> None:
    df, _, _ = canonicalize_file(
        input_path=Path("tests/fixtures/raw_small_sample.txt"),
        schema_path=Path("schemas/canon.schema.v1.json"),
        colmap_path=Path("schemas/colmap.raw_vendor_v1.json"),
        instrument="ES",
        tf="1min",
        session_policy="full",
        rth_start="09:30",
        rth_end="16:00",
        keep_updown=True,
    )
    assert (df["volume"] == (df["up"] + df["down"])).all()
