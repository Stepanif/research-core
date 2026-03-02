from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def test_psa_golden_hashes_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    root = Path(__file__).resolve().parents[1]
    fixture = (root / "tests" / "fixtures" / "raw_small_sample.txt").resolve()
    canon_schema = (root / "schemas" / "canon.schema.v1.json").resolve()
    colmap = (root / "schemas" / "colmap.raw_vendor_v1.json").resolve()
    psa_schema = (root / "schemas" / "psa.schema.v1.json").resolve()

    runner = CliRunner()
    run_dir = tmp_path / "run"

    canon_result = runner.invoke(
        app,
        [
            "canon",
            "--in",
            str(fixture),
            "--out",
            str(run_dir),
            "--instrument",
            "ES",
            "--tf",
            "1min",
            "--schema",
            str(canon_schema),
            "--colmap",
            str(colmap),
        ],
    )
    assert canon_result.exit_code == 0, canon_result.stdout

    psa_result = runner.invoke(
        app,
        [
            "psa",
            "--in",
            str(run_dir / "canon.parquet"),
            "--out",
            str(run_dir),
            "--schema",
            str(psa_schema),
        ],
    )
    assert psa_result.exit_code == 0, psa_result.stdout

    manifest = json.loads((run_dir / "psa.manifest.json").read_text(encoding="utf-8"))
    canonical_table_hash = manifest["output_files"]["psa.parquet"]["canonical_table_sha256"]
    manifest_canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    manifest_hash = hashlib.sha256(manifest_canonical.encode("utf-8")).hexdigest()

    expected_table_hash = Path("tests/golden/psa_small_sample_v1.parquet.sha256").read_text(encoding="utf-8").strip()
    expected_manifest_hash = Path("tests/golden/psa_small_sample_v1.manifest.json.sha256").read_text(encoding="utf-8").strip()

    assert canonical_table_hash == expected_table_hash
    assert manifest_hash == expected_manifest_hash
