from __future__ import annotations

import hashlib
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app
from research_core.util.hashing import sha256_json
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
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout


def _make_valid_spec_dir(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for name in ["spec_01_global_min.json", "spec_02_global_event_bits.json"]:
        (target / name).write_text((Path("tests/fixtures/exp_specs") / name).read_text(encoding="utf-8"), encoding="utf-8")


def test_experiment_batch_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    spec_dir = tmp_path / "valid_specs"
    _make_valid_spec_dir(spec_dir)

    batch_dir = tmp_path / "batch"
    result = runner.invoke(app, ["experiment", "batch", "--run", str(run_dir), "--spec-dir", str(spec_dir), "--out", str(batch_dir)])
    assert result.exit_code == 0, result.stdout

    summary_hash = hashlib.sha256((batch_dir / "batch.summary.json").read_bytes()).hexdigest()
    manifest = read_json(batch_dir / "batch.manifest.json")
    manifest_canonical_hash = sha256_json({key: value for key, value in manifest.items() if key != "batch_manifest_canonical_sha256"})

    expected_summary = Path("tests/golden/experiment_batch_small_sample_v1.summary.json.sha256").read_text(encoding="utf-8").strip()
    expected_manifest = Path("tests/golden/experiment_batch_small_sample_v1.manifest.json.sha256").read_text(encoding="utf-8").strip()

    assert summary_hash == expected_summary
    assert manifest_canonical_hash == expected_manifest
