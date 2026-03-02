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


def _write_project_spec(path: Path, runs: list[Path], spec_dir: Path, output_dir: Path) -> None:
    payload = {
        "project_version": "v1",
        "name": "project-smoke",
        "runs": [run.name for run in runs],
        "spec_dirs": [spec_dir.name],
        "output_dir": output_dir.name,
        "policy": {"fail_fast": True, "require_observe": False},
    }
    path.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


def test_project_run_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_a = tmp_path / "run_a"
    run_b = tmp_path / "run_b"
    _build_run(runner, run_a)
    _build_run(runner, run_b)

    spec_dir = tmp_path / "specs"
    spec_dir.mkdir(parents=True, exist_ok=True)
    (spec_dir / "spec_01.json").write_text(
        Path("tests/fixtures/exp_specs/spec_01_global_min.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    project_spec = tmp_path / "project.json"
    output_dir = tmp_path / "project_outputs"
    _write_project_spec(project_spec, [run_a, run_b], spec_dir, output_dir)

    result = runner.invoke(app, ["project", "run", "--project", str(project_spec)])
    assert result.exit_code == 0, result.stdout

    project_dirs = sorted([path for path in output_dir.iterdir() if path.is_dir()])
    assert len(project_dirs) == 1
    project_dir = project_dirs[0]

    assert (project_dir / "project.summary.json").exists()
    assert (project_dir / "project.manifest.json").exists()
    assert (project_dir / "README_PROJECT.txt").exists()
