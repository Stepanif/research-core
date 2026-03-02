from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()


def test_observe_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"

    canon = runner.invoke(
        app,
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
    )
    assert canon.exit_code == 0, canon.stdout

    psa = runner.invoke(app, ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)])
    assert psa.exit_code == 0, psa.stdout

    observe = runner.invoke(app, ["observe", "summary", "--run", str(run_dir)])
    assert observe.exit_code == 0, observe.stdout

    summary_hash = hashlib.sha256((run_dir / "observe" / "observe.summary.json").read_bytes()).hexdigest()
    manifest_hash = _canonical_hash(run_dir / "observe" / "observe.summary.manifest.json")

    expected_summary_hash = Path("tests/golden/observe_small_sample_v1.summary.json.sha256").read_text(encoding="utf-8").strip()
    expected_manifest_hash = Path("tests/golden/observe_small_sample_v1.manifest.json.sha256").read_text(encoding="utf-8").strip()

    assert summary_hash == expected_summary_hash
    assert manifest_hash == expected_manifest_hash
