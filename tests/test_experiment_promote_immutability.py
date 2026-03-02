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


def _write_spec(path: Path, include_event_bits: bool) -> None:
    payload = {
        "spec_version": "v1",
        "kind": "transition_matrix",
        "params": {"transition_scope": "global", "include_event_bits": include_event_bits},
    }
    path.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


def test_experiment_promote_immutability(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    spec1 = tmp_path / "spec1.json"
    spec2 = tmp_path / "spec2.json"
    _write_spec(spec1, include_event_bits=False)
    _write_spec(spec2, include_event_bits=True)

    r1 = runner.invoke(app, ["experiment", "run", "--run", str(run_dir), "--spec", str(spec1)])
    assert r1.exit_code == 0, r1.stdout
    r2 = runner.invoke(app, ["experiment", "run", "--run", str(run_dir), "--spec", str(spec2)])
    assert r2.exit_code == 0, r2.stdout

    exp_ids = sorted([path.name for path in (run_dir / "experiments").iterdir() if path.is_dir()])
    assert len(exp_ids) == 2
    first_exp = exp_ids[0]
    second_exp = exp_ids[1]

    promote1 = runner.invoke(app, ["experiment", "promote", "--run", str(run_dir), "--id", first_exp, "--label", "prod"])
    assert promote1.exit_code == 0, promote1.stdout

    promote2 = runner.invoke(app, ["experiment", "promote", "--run", str(run_dir), "--id", first_exp, "--label", "prod"])
    assert promote2.exit_code == 0, promote2.stdout

    promote3 = runner.invoke(app, ["experiment", "promote", "--run", str(run_dir), "--id", second_exp, "--label", "prod"])
    assert promote3.exit_code != 0
    assert promote3.exception is not None
    assert "immutability" in str(promote3.exception).lower()

    promote4 = runner.invoke(app, ["experiment", "promote", "--run", str(run_dir), "--id", "does-not-exist", "--label", "staging"])
    assert promote4.exit_code != 0
    assert promote4.exception is not None
    assert "missing experiment" in str(promote4.exception).lower()
