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


def test_experiment_batch_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    spec_dir = tmp_path / "valid_specs"
    _make_valid_spec_dir(spec_dir)

    batch1 = tmp_path / "batch1"
    batch2 = tmp_path / "batch2"

    r1 = runner.invoke(app, ["experiment", "batch", "--run", str(run_dir), "--spec-dir", str(spec_dir), "--out", str(batch1)])
    assert r1.exit_code == 0, r1.stdout
    r2 = runner.invoke(app, ["experiment", "batch", "--run", str(run_dir), "--spec-dir", str(spec_dir), "--out", str(batch2)])
    assert r2.exit_code == 0, r2.stdout

    summary_sha1 = hashlib.sha256((batch1 / "batch.summary.json").read_bytes()).hexdigest()
    summary_sha2 = hashlib.sha256((batch2 / "batch.summary.json").read_bytes()).hexdigest()
    assert summary_sha1 == summary_sha2

    manifest_hash1 = sha256_json(
        {key: value for key, value in read_json(batch1 / "batch.manifest.json").items() if key != "batch_manifest_canonical_sha256"}
    )
    manifest_hash2 = sha256_json(
        {key: value for key, value in read_json(batch2 / "batch.manifest.json").items() if key != "batch_manifest_canonical_sha256"}
    )
    assert manifest_hash1 == manifest_hash2
