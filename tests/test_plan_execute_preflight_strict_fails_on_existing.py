from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app
from research_core.util.io import read_json


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
        ["observe", "summary", "--run", str(run_dir)],
        ["observe", "profile", "--run", str(run_dir)],
        ["registry", "refresh", "--run", str(run_dir)],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout


def test_plan_execute_preflight_strict_fails_on_existing(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_a = tmp_path / "run_a"
    _build_run(runner, run_a)

    specs = tmp_path / "specs"
    specs.mkdir(parents=True, exist_ok=True)
    (specs / "spec_01.json").write_text(Path("tests/fixtures/exp_specs/spec_01_global_min.json").read_text(encoding="utf-8"), encoding="utf-8")

    project_path = tmp_path / "project.json"
    project_path.write_text(
        json.dumps(
            {
                "project_version": "v1",
                "name": "plan-preflight-strict",
                "runs": ["run_a"],
                "spec_dirs": ["specs"],
                "output_dir": "project_outputs",
                "policy": {"fail_fast": True, "require_observe": False},
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    plan_path = tmp_path / "plan.json"
    build_result = runner.invoke(app, ["plan", "build", "--project", str(project_path), "--out", str(plan_path)])
    assert build_result.exit_code == 0, build_result.stdout

    first_execute = runner.invoke(app, ["plan", "execute", "--plan", str(plan_path), "--jobs", "1"])
    assert first_execute.exit_code == 0, first_execute.stdout

    logs_dir = plan_path.parent / "logs"
    before_logs = sorted([path.name for path in logs_dir.iterdir() if path.is_file()])

    second_execute = runner.invoke(app, ["plan", "execute", "--plan", str(plan_path), "--jobs", "1"])
    assert second_execute.exit_code != 0
    assert "preflight" in second_execute.stdout
    assert "EXISTS_COMPLETE" in second_execute.stdout

    after_logs = sorted([path.name for path in logs_dir.iterdir() if path.is_file()])
    assert after_logs == before_logs
