from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _validate_schema_shape(payload: dict[str, object], schema: dict[str, object]) -> None:
    required = schema.get("required")
    assert isinstance(required, list)
    for key in required:
        assert key in payload


def test_psa_report_smoke(monkeypatch: object, tmp_path: Path) -> None:
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
    assert "PSA_REPORT status=PASS" in report.stdout

    report_path = run_dir / "psa.report.json"
    manifest_path = run_dir / "psa.report.manifest.json"
    assert report_path.exists()
    assert manifest_path.exists()

    schema = json.loads((Path("schemas") / "psa.report.schema.v1.json").read_text(encoding="utf-8"))
    payload = json.loads(report_path.read_text(encoding="utf-8"))

    _validate_schema_shape(payload, schema)
    assert payload["report_version"] == "v1"
    assert payload["metrics"]["row_count"] == 3
    assert "alignment_vector_sha256" in payload["checksums"]
