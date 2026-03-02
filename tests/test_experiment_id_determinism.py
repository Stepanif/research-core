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


def _single_exp_id(run_dir: Path) -> str:
    exp_root = run_dir / "experiments"
    exp_dirs = sorted([path.name for path in exp_root.iterdir() if path.is_dir()])
    assert len(exp_dirs) == 1
    return exp_dirs[0]


def test_experiment_id_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()

    run1 = tmp_path / "run_a"
    run2 = tmp_path / "run_b"
    _build_run(runner, run1)
    _build_run(runner, run2)

    spec1 = tmp_path / "spec_a.json"
    spec2 = tmp_path / "spec_b.json"
    _write_spec(spec1)
    _write_spec(spec2)

    r1 = runner.invoke(app, ["experiment", "run", "--run", str(run1), "--spec", str(spec1)])
    assert r1.exit_code == 0, r1.stdout
    r2 = runner.invoke(app, ["experiment", "run", "--run", str(run2), "--spec", str(spec2)])
    assert r2.exit_code == 0, r2.stdout

    assert _single_exp_id(run1) == _single_exp_id(run2)
