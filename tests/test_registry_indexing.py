from __future__ import annotations

import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from research_core.cli import app


def _make_run(runner: CliRunner, out_dir: Path, instrument: str) -> None:
    result = runner.invoke(
        app,
        [
            "canon",
            "--in",
            "tests/fixtures/raw_small_sample.txt",
            "--out",
            str(out_dir),
            "--instrument",
            instrument,
            "--tf",
            "1min",
            "--schema",
            "schemas/canon.schema.v1.json",
            "--colmap",
            "schemas/colmap.raw_vendor_v1.json",
        ],
    )
    assert result.exit_code == 0, result.stdout


def test_registry_build_deterministic(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()
    runs = tmp_path / "runs"
    run_a = runs / "a"
    run_b = runs / "b"
    _make_run(runner, run_a, "ES")
    _make_run(runner, run_b, "NQ")

    out_registry = tmp_path / "registry.json"
    result = runner.invoke(
        app,
        ["registry", "build", "--data-root", str(runs), "--out", str(out_registry)],
    )
    assert result.exit_code == 0, result.stdout
    assert out_registry.exists()


def test_index_runs_duplicate_manifest_hash_fails(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()
    runs = tmp_path / "runs"
    run_a = runs / "a"
    _make_run(runner, run_a, "ES")

    dup = runs / "dup"
    shutil.copytree(run_a, dup)

    result = runner.invoke(
        app,
        ["registry", "index-runs", "--runs-root", str(runs), "--out", str(tmp_path / "index.json")],
    )
    assert result.exit_code != 0
    assert result.exception is not None
    assert "Duplicate manifest hash" in str(result.exception)
