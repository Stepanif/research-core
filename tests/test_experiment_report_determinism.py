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


def test_experiment_report_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run_with_experiment_and_promotion(runner, run_dir, tmp_path)

    r1 = runner.invoke(app, ["experiment", "report", "--run", str(run_dir)])
    assert r1.exit_code == 0, r1.stdout
    report1 = (run_dir / "experiments" / "experiments.report.json").read_bytes()
    manifest1 = json.loads((run_dir / "experiments" / "experiments.report.manifest.json").read_text(encoding="utf-8"))

    r2 = runner.invoke(app, ["experiment", "report", "--run", str(run_dir)])
    assert r2.exit_code == 0, r2.stdout
    report2 = (run_dir / "experiments" / "experiments.report.json").read_bytes()
    manifest2 = json.loads((run_dir / "experiments" / "experiments.report.manifest.json").read_text(encoding="utf-8"))

    assert hashlib.sha256(report1).hexdigest() == hashlib.sha256(report2).hexdigest()

    manifest_hash1 = sha256_json({key: value for key, value in manifest1.items() if key != "report_manifest_canonical_sha256"})
    manifest_hash2 = sha256_json({key: value for key, value in manifest2.items() if key != "report_manifest_canonical_sha256"})
    assert manifest_hash1 == manifest_hash2
