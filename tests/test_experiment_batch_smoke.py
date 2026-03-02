from __future__ import annotations

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


def test_experiment_batch_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    batch_dir = tmp_path / "batch"
    result = runner.invoke(
        app,
        [
            "experiment",
            "batch",
            "--run",
            str(run_dir),
            "--spec-dir",
            "tests/fixtures/exp_specs",
            "--out",
            str(batch_dir),
        ],
    )
    assert result.exit_code != 0

    result = runner.invoke(
        app,
        [
            "experiment",
            "batch",
            "--run",
            str(run_dir),
            "--spec-dir",
            str(tmp_path / "valid_specs"),
            "--out",
            str(batch_dir),
        ],
    )
    assert result.exit_code != 0

    valid_specs = tmp_path / "valid_specs"
    valid_specs.mkdir(parents=True, exist_ok=True)
    for name in ["spec_01_global_min.json", "spec_02_global_event_bits.json"]:
        (valid_specs / name).write_text((Path("tests/fixtures/exp_specs") / name).read_text(encoding="utf-8"), encoding="utf-8")

    result = runner.invoke(
        app,
        [
            "experiment",
            "batch",
            "--run",
            str(run_dir),
            "--spec-dir",
            str(valid_specs),
            "--out",
            str(batch_dir),
        ],
    )
    assert result.exit_code == 0, result.stdout

    assert (batch_dir / "batch.summary.json").exists()
    assert (batch_dir / "batch.manifest.json").exists()

    summary = read_json(batch_dir / "batch.summary.json")
    manifest = read_json(batch_dir / "batch.manifest.json")

    assert summary["batch_version"] == "v1"
    assert summary["counts"] == {"total": 2, "succeeded": 2, "failed": 0}
    assert summary["spec_dir_listing"] == ["spec_01_global_min.json", "spec_02_global_event_bits.json"]

    expected_manifest_hash = sha256_json({key: value for key, value in manifest.items() if key != "batch_manifest_canonical_sha256"})
    assert manifest["batch_manifest_canonical_sha256"] == expected_manifest_hash
