from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app
from research_core.experiments.spec import load_experiment_spec
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


def test_experiment_run_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    spec_path = tmp_path / "experiment.spec.json"
    spec_path.write_text(
        json.dumps(
            {
                "spec_version": "v1",
                "kind": "transition_matrix",
                "params": {"transition_scope": "global"},
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    normalized_spec = load_experiment_spec(spec_path)
    assert normalized_spec["params"]["include_event_bits"] is False

    result = runner.invoke(app, ["experiment", "run", "--run", str(run_dir), "--spec", str(spec_path)])
    assert result.exit_code == 0, result.stdout

    exp_root = run_dir / "experiments"
    exp_ids = sorted([path.name for path in exp_root.iterdir() if path.is_dir()])
    assert len(exp_ids) == 1

    exp_dir = exp_root / exp_ids[0]
    assert (exp_dir / "transition_matrix.json").exists()
    assert (exp_dir / "exp.manifest.json").exists()
    assert (exp_root / "experiments.index.json").exists()

    manifest = read_json(exp_dir / "exp.manifest.json")
    expected_manifest_hash = sha256_json({key: value for key, value in manifest.items() if key != "exp_manifest_canonical_sha256"})
    assert manifest["exp_manifest_canonical_sha256"] == expected_manifest_hash
