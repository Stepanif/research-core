from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app
from research_core.util.hashing import sha256_file, sha256_json
from research_core.util.io import read_json


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


def _write_project(path: Path, out_dir_name: str = "project_outputs") -> None:
    payload = {
        "project_version": "v1",
        "name": "project-index-smoke",
        "runs": ["run_a", "run_b"],
        "spec_dirs": ["specs"],
        "output_dir": out_dir_name,
        "policy": {"fail_fast": True, "require_observe": False},
    }
    path.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


def test_project_index_refresh_smoke(monkeypatch: object, tmp_path: Path) -> None:
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
    _write_project(project_path)

    run_result = runner.invoke(app, ["project", "run", "--project", str(project_path)])
    assert run_result.exit_code == 0, run_result.stdout

    output_dir = tmp_path / "project_outputs"
    refresh_result = runner.invoke(app, ["project", "index", "refresh", "--output-dir", str(output_dir)])
    assert refresh_result.exit_code == 0, refresh_result.stdout

    index_path = output_dir / "projects.index.json"
    assert index_path.exists()

    index_payload = read_json(index_path)
    assert index_payload["index_version"] == "v1"
    assert len(index_payload["projects"]) == 1

    project_id = next(iter(index_payload["projects"].keys()))
    entry = index_payload["projects"][project_id]

    project_dir = output_dir / project_id
    assert entry["summary_sha256"] == sha256_file(project_dir / "project.summary.json")
    assert entry["manifest_canonical_sha256"] == sha256_json(read_json(project_dir / "project.manifest.json"))
