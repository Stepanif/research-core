from __future__ import annotations

import zipfile
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
        ["observe", "summary", "--run", str(run_dir)],
        ["observe", "profile", "--run", str(run_dir)],
        ["registry", "refresh", "--run", str(run_dir)],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout


def test_verify_bundle_detects_corruption(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    bundle_path = tmp_path / "bundle.zip"
    export_result = runner.invoke(app, ["bundle", "export", "--run", str(run_dir), "--out", str(bundle_path)])
    assert export_result.exit_code == 0, export_result.stdout

    corrupted_bundle_path = tmp_path / "bundle_corrupted.zip"
    with zipfile.ZipFile(bundle_path, "r") as source, zipfile.ZipFile(corrupted_bundle_path, "w", compression=zipfile.ZIP_DEFLATED) as target:
        for name in source.namelist():
            data = source.read(name)
            if name == "bundle/run/observe/observe.summary.json":
                data = data + b"\nCORRUPTED"
            target.writestr(name, data)

    verify_result = runner.invoke(app, ["verify", "bundle", "--zip", str(corrupted_bundle_path)])
    assert verify_result.exit_code != 0
    assert "RESEARCH DOCTOR v1" in verify_result.stdout
    assert "[FAIL]" in verify_result.stdout
    assert "bundle/run/observe/observe.summary.json" in verify_result.stdout
