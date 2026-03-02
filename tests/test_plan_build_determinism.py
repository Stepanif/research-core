from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app
from research_core.util.hashing import sha256_file


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


def test_plan_build_determinism(monkeypatch: object, tmp_path: Path) -> None:
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
                "name": "plan-build-determinism",
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

    plan_1 = tmp_path / "plan_1.json"
    plan_2 = tmp_path / "plan_2.json"

    r1 = runner.invoke(app, ["plan", "build", "--project", str(project_path), "--out", str(plan_1)])
    assert r1.exit_code == 0, r1.stdout
    r2 = runner.invoke(app, ["plan", "build", "--project", str(project_path), "--out", str(plan_2)])
    assert r2.exit_code == 0, r2.stdout

    assert sha256_file(plan_1) == sha256_file(plan_2)
