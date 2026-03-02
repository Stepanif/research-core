from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def test_golden_hashes_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()
    run_dir = tmp_path / "run"
    result = runner.invoke(
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
    assert result.exit_code == 0, result.stdout

    manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    canonical_hash = manifest["output_files"]["canon.parquet"]["canonical_table_sha256"]
    manifest_canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":"))
    manifest_hash = hashlib.sha256(manifest_canonical.encode("utf-8")).hexdigest()

    expected_canonical = Path("tests/golden/canon_small_sample_v1.parquet.sha256").read_text(encoding="utf-8").strip()
    expected_manifest = Path("tests/golden/canon_small_sample_v1.manifest.json.sha256").read_text(encoding="utf-8").strip()

    assert canonical_hash == expected_canonical
    assert manifest_hash == expected_manifest
