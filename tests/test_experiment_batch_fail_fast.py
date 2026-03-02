from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _build_run(runner: CliRunner, run_dir: Path) -> None:
    for args in [
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
        ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout


def test_experiment_batch_fail_fast(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    spec_dir = tmp_path / "specs"
    spec_dir.mkdir(parents=True, exist_ok=True)
    for name in ["spec_01_global_min.json", "spec_99_invalid_kind.json"]:
        (spec_dir / name).write_text((Path("tests/fixtures/exp_specs") / name).read_text(encoding="utf-8"), encoding="utf-8")

    batch_dir = tmp_path / "batch"
    result = runner.invoke(
        app,
        ["experiment", "batch", "--run", str(run_dir), "--spec-dir", str(spec_dir), "--out", str(batch_dir)],
    )
    assert result.exit_code != 0
    assert batch_dir.exists() is False

    experiments_root = run_dir / "experiments"
    assert experiments_root.exists() is False
