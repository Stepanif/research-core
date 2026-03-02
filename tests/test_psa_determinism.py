from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def _canonical_manifest_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()


def test_psa_deterministic_hashes_across_runs(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()

    canon_run = tmp_path / "canon"
    canon_result = runner.invoke(
        app,
        [
            "canon",
            "--in",
            "tests/fixtures/raw_small_sample.txt",
            "--out",
            str(canon_run),
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

    in_parquet = canon_run / "canon.parquet"
    run1 = tmp_path / "psa_run1"
    run2 = tmp_path / "psa_run2"

    result1 = runner.invoke(app, ["psa", "--in", str(in_parquet), "--out", str(run1)])
    assert result1.exit_code == 0, result1.stdout
    result2 = runner.invoke(app, ["psa", "--in", str(in_parquet), "--out", str(run2)])
    assert result2.exit_code == 0, result2.stdout

    manifest1 = json.loads((run1 / "psa.manifest.json").read_text(encoding="utf-8"))
    manifest2 = json.loads((run2 / "psa.manifest.json").read_text(encoding="utf-8"))

    assert (
        manifest1["output_files"]["psa.parquet"]["canonical_table_sha256"]
        == manifest2["output_files"]["psa.parquet"]["canonical_table_sha256"]
    )
    assert _canonical_manifest_hash(run1 / "psa.manifest.json") == _canonical_manifest_hash(run2 / "psa.manifest.json")
    assert manifest1["input_files"][0]["path"] == "canon.parquet"
    assert manifest2["input_files"][0]["path"] == "canon.parquet"
