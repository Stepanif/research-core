from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def test_psa_report_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setenv("RESEARCH_GIT_COMMIT", "unknown")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()

    hashes: list[tuple[str, str, str]] = []
    for index in [1, 2]:
        run_dir = tmp_path / f"case{index}" / "run"
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
        payload = json.loads(report_path.read_text(encoding="utf-8"))

        report_sha = hashlib.sha256(report_path.read_bytes()).hexdigest()
        manifest_sha = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        vector_sha = str(payload["checksums"]["alignment_vector_sha256"])
        hashes.append((report_sha, manifest_sha, vector_sha))

    assert hashes[0] == hashes[1]
