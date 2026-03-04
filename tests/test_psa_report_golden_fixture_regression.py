from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _manifest_canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    clone = {key: value for key, value in payload.items() if key != "manifest_canonical_sha256"}
    data = json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def test_psa_report_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setenv("RESEARCH_GIT_COMMIT", "unknown")
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

    report = runner.invoke(app, ["psa", "report", "--run", str(run_dir)])
    assert report.exit_code == 0, report.stdout

    report_path = run_dir / "psa.report.json"
    manifest_path = run_dir / "psa.report.manifest.json"

    report_hash = hashlib.sha256(report_path.read_bytes()).hexdigest()
    manifest_hash = _manifest_canonical_hash(manifest_path)

    expected_report_hash = Path("tests/golden/psa_report_small_sample_v1.report.json.sha256").read_text(encoding="utf-8").strip()
    expected_manifest_hash = Path("tests/golden/psa_report_small_sample_v1.manifest.json.sha256").read_text(encoding="utf-8").strip()

    assert report_hash == expected_report_hash
    assert manifest_hash == expected_manifest_hash
