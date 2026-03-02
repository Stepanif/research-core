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


def _write_project(path: Path, name: str, output_dir_name: str) -> None:
    payload = {
        "project_version": "v1",
        "name": name,
        "runs": ["run_a", "run_b"],
        "spec_dirs": ["specs"],
        "output_dir": output_dir_name,
        "policy": {"fail_fast": True, "require_observe": False},
    }
    path.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


def test_project_promotions_immutability(monkeypatch: object, tmp_path: Path) -> None:
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

    output_dir = tmp_path / "project_outputs"

    project_1 = tmp_path / "project_1.json"
    project_2 = tmp_path / "project_2.json"
    _write_project(project_1, name="project-promote-a", output_dir_name="project_outputs")
    _write_project(project_2, name="project-promote-b", output_dir_name="project_outputs")

    r1 = runner.invoke(app, ["project", "run", "--project", str(project_1)])
    assert r1.exit_code == 0, r1.stdout
    r2 = runner.invoke(app, ["project", "run", "--project", str(project_2)])
    assert r2.exit_code == 0, r2.stdout

    refresh = runner.invoke(app, ["project", "index", "refresh", "--output-dir", str(output_dir)])
    assert refresh.exit_code == 0, refresh.stdout

    project_ids = sorted([path.name for path in output_dir.iterdir() if path.is_dir()])
    assert len(project_ids) == 2

    p1 = runner.invoke(app, ["project", "promote", "--output-dir", str(output_dir), "--id", project_ids[0], "--label", "prod"])
    assert p1.exit_code == 0, p1.stdout

    p2 = runner.invoke(app, ["project", "promote", "--output-dir", str(output_dir), "--id", project_ids[0], "--label", "prod"])
    assert p2.exit_code == 0, p2.stdout

    p3 = runner.invoke(app, ["project", "promote", "--output-dir", str(output_dir), "--id", project_ids[1], "--label", "prod"])
    assert p3.exit_code != 0
    assert p3.exception is not None
    assert "immutability" in str(p3.exception).lower()
