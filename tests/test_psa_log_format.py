from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def test_psa_log_format_and_eof_newline(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"

    canon_result = runner.invoke(
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
    assert canon_result.exit_code == 0, canon_result.stdout

    psa_result = runner.invoke(app, ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)])
    assert psa_result.exit_code == 0, psa_result.stdout

    log_path = run_dir / "psa.log"
    assert log_path.exists()

    raw_bytes = log_path.read_bytes()
    assert raw_bytes.endswith(b"\n")

    lines = log_path.read_text(encoding="utf-8").splitlines()
    manifest = json.loads((run_dir / "psa.manifest.json").read_text(encoding="utf-8"))
    manifest_rowcount = int(manifest["rowcount"])
    assert len(lines) == 3
    assert len(lines) == manifest_rowcount

    for line in lines:
        parts = line.split(",")
        assert len(parts) == 8
        assert parts[3] in {"UP", "DOWN", "CONST"}
        assert parts[4] == "FLAT"
        assert parts[5] in {"BULL", "BEAR", "DOJI"}
        assert parts[6].startswith("PSA.v1|P=")
        int(parts[7])
