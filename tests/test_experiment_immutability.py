from __future__ import annotations

import json
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


def _write_spec(path: Path) -> None:
    payload = {
        "spec_version": "v1",
        "kind": "transition_matrix",
        "params": {"transition_scope": "global", "include_event_bits": False},
    }
    path.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


def test_experiment_immutability(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    spec_path = tmp_path / "spec.json"
    _write_spec(spec_path)

    first = runner.invoke(app, ["experiment", "run", "--run", str(run_dir), "--spec", str(spec_path)])
    assert first.exit_code == 0, first.stdout

    exp_root = run_dir / "experiments"
    exp_id = sorted([path.name for path in exp_root.iterdir() if path.is_dir()])[0]
    transition_path = exp_root / exp_id / "transition_matrix.json"
    transition_path.write_text(transition_path.read_text(encoding="utf-8") + " ", encoding="utf-8")

    second = runner.invoke(app, ["experiment", "run", "--run", str(run_dir), "--spec", str(spec_path)])
    assert second.exit_code != 0
    assert second.exception is not None
    assert "immutability violation" in str(second.exception).lower()
