from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app
from research_core.util.hashing import sha256_json


def _build_run_with_experiment_and_promotion(runner: CliRunner, run_dir: Path, tmp_path: Path) -> None:
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

    exp_id = sorted([path.name for path in (run_dir / "experiments").iterdir() if path.is_dir()])[0]
    result = runner.invoke(app, ["experiment", "promote", "--run", str(run_dir), "--id", exp_id, "--label", "prod"])
    assert result.exit_code == 0, result.stdout


def test_experiment_report_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run_with_experiment_and_promotion(runner, run_dir, tmp_path)

    result = runner.invoke(app, ["experiment", "report", "--run", str(run_dir)])
    assert result.exit_code == 0, result.stdout

    report_hash = hashlib.sha256((run_dir / "experiments" / "experiments.report.json").read_bytes()).hexdigest()
    report_manifest = json.loads((run_dir / "experiments" / "experiments.report.manifest.json").read_text(encoding="utf-8"))
    report_manifest_hash = sha256_json(
        {key: value for key, value in report_manifest.items() if key != "report_manifest_canonical_sha256"}
    )

    expected_report = Path("tests/golden/experiment_report_small_sample_v1.report.json.sha256").read_text(encoding="utf-8").strip()
    expected_manifest = Path("tests/golden/experiment_report_small_sample_v1.manifest.json.sha256").read_text(encoding="utf-8").strip()

    assert report_hash == expected_report
    assert report_manifest_hash == expected_manifest
