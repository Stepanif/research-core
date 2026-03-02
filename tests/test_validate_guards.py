from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from research_core.cli import app
from research_core.canon.normalize import canonicalize_file
from research_core.util.types import ValidationError


def test_negative_up_down_fails_loud(tmp_path: Path) -> None:
    raw = tmp_path / "raw_negative_up.txt"
    raw.write_text(
        "Date,Time,Open,High,Low,Close,Up,Down\n"
        "03/07/2024,09:30,100.0,101.0,99.5,100.5,-1,5\n",
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="negative"):
        canonicalize_file(
            input_path=raw,
            schema_path=Path("schemas/canon.schema.v1.json"),
            colmap_path=Path("schemas/colmap.raw_vendor_v1.json"),
            instrument="ES",
            tf="1min",
            session_policy="full",
            rth_start="09:30",
            rth_end="16:00",
            keep_updown=True,
        )


def test_validate_schema_drift_fails(tmp_path: Path, monkeypatch: object) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()
    run_dir = tmp_path / "run"
    canon = runner.invoke(
        app,
        [
            "canon",
            "--in",
            "tests/fixtures/raw_small_sample.txt",
            "--out",
            str(run_dir),
            "--instrument",
            "ES",
            "--tf",
            "1min",
            "--schema",
            "schemas/canon.schema.v1.json",
            "--colmap",
            "schemas/colmap.raw_vendor_v1.json",
        ],
    )
    assert canon.exit_code == 0, canon.stdout

    bad_schema = tmp_path / "bad_schema.json"
    payload = json.loads(Path("schemas/canon.schema.v1.json").read_text(encoding="utf-8"))
    payload["required_columns"] = [
        "ts",
        "instrument",
        "tf",
        "high",
        "open",
        "low",
        "close",
        "volume",
    ]
    bad_schema.write_text(json.dumps(payload), encoding="utf-8")

    result = runner.invoke(
        app,
        [
            "validate",
            "canon",
            "--input",
            str(run_dir / "canon.parquet"),
            "--schema",
            str(bad_schema),
        ],
    )
    assert result.exit_code != 0
    assert result.exception is not None
    assert "Column order mismatch" in str(result.exception)
