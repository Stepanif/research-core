from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _build_run(runner: CliRunner, run_dir: Path) -> None:
    commands = [
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
    ]
    for cmd in commands:
        result = runner.invoke(app, cmd)
        assert result.exit_code == 0, result.stdout


def test_project_index_immutability(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_a = tmp_path / "run_a"
    run_b = tmp_path / "run_b"
    _build_run(runner, run_a)
    _build_run(runner, run_b)

    specs = tmp_path / "specs"
    specs.mkdir(parents=True, exist_ok=True)
    (specs / "spec_01.json").write_text(Path("tests/fixtures/exp_specs/spec_01_global_min.json").read_text(encoding="utf-8"), encoding="utf-8")

    project_path = tmp_path / "project.json"
    project_path.write_text(
        json.dumps(
            {
                "project_version": "v1",
                "name": "project-index-immutability",
                "runs": ["run_a", "run_b"],
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

    run_result = runner.invoke(app, ["project", "run", "--project", str(project_path)])
    assert run_result.exit_code == 0, run_result.stdout

    output_dir = tmp_path / "project_outputs"
    first_refresh = runner.invoke(app, ["project", "index", "refresh", "--output-dir", str(output_dir)])
    assert first_refresh.exit_code == 0, first_refresh.stdout

    project_id = sorted([path.name for path in output_dir.iterdir() if path.is_dir()])[0]
    summary_path = output_dir / project_id / "project.summary.json"
    summary_path.write_text(summary_path.read_text(encoding="utf-8") + " ", encoding="utf-8")

    second_refresh = runner.invoke(app, ["project", "index", "refresh", "--output-dir", str(output_dir)])
    assert second_refresh.exit_code != 0
    assert second_refresh.exception is not None
    assert "immutability violation" in str(second_refresh.exception).lower()
