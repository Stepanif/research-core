from __future__ import annotations

import hashlib
import json
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


def test_experiment_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

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

    exp_root = run_dir / "experiments"
    exp_id = sorted([path.name for path in exp_root.iterdir() if path.is_dir()])[0]
    exp_dir = exp_root / exp_id

    transition_hash = hashlib.sha256((exp_dir / "transition_matrix.json").read_bytes()).hexdigest()
    manifest = read_json(exp_dir / "exp.manifest.json")
    manifest_canonical_hash = sha256_json({key: value for key, value in manifest.items() if key != "exp_manifest_canonical_sha256"})

    expected_transition = Path("tests/golden/experiment_small_sample_v1.transition_matrix.json.sha256").read_text(
        encoding="utf-8"
    ).strip()
    expected_manifest = Path("tests/golden/experiment_small_sample_v1.manifest.json.sha256").read_text(
        encoding="utf-8"
    ).strip()

    assert transition_hash == expected_transition
    assert manifest_canonical_hash == expected_manifest
