from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _build_run_with_experiment_and_promotion(runner: CliRunner, run_dir: Path, tmp_path: Path) -> str:
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

    spec_path = tmp_path / "spec.json"
    spec_path.write_text(
        json.dumps(
            {
                "spec_version": "v1",
                "kind": "transition_matrix",
                "params": {"transition_scope": "global", "include_event_bits": False},
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    result = runner.invoke(app, ["experiment", "run", "--run", str(run_dir), "--spec", str(spec_path)])
    assert result.exit_code == 0, result.stdout

    exp_ids = sorted([path.name for path in (run_dir / "experiments").iterdir() if path.is_dir()])
    assert len(exp_ids) == 1
    exp_id = exp_ids[0]

    result = runner.invoke(app, ["experiment", "promote", "--run", str(run_dir), "--id", exp_id, "--label", "prod"])
    assert result.exit_code == 0, result.stdout
    return exp_id


def test_experiment_report_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run_with_experiment_and_promotion(runner, run_dir, tmp_path)

    result = runner.invoke(app, ["experiment", "report", "--run", str(run_dir)])
    assert result.exit_code == 0, result.stdout

    report_path = run_dir / "experiments" / "experiments.report.json"
    manifest_path = run_dir / "experiments" / "experiments.report.manifest.json"
    assert report_path.exists()
    assert manifest_path.exists()

    report = json.loads(report_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert report["report_version"] == "v1"
    assert "index_snapshot" in report
    assert "integrity" in report
    assert report["integrity"]["summary"]["failed"] == 0

    assert manifest["manifest_version"] == "v1"
    assert "report_manifest_canonical_sha256" in manifest
