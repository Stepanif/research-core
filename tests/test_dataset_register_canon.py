from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app
from research_core.util.io import read_json


def _extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def test_dataset_register_canon(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    run_dir = tmp_path / "run"

    canon = runner.invoke(
        app,
        [
            "canon",
            "--in",
            str((Path(__file__).parent / "fixtures" / "raw_small_sample.txt").resolve()),
            "--out",
            "run",
            "--instrument",
            "ES",
            "--tf",
            "1min",
            "--schema",
            str((Path(__file__).parent.parent / "schemas" / "canon.schema.v1.json").resolve()),
            "--colmap",
            str((Path(__file__).parent.parent / "schemas" / "colmap.raw_vendor_v1.json").resolve()),
        ],
    )
    assert canon.exit_code == 0, canon.stdout

    reg = runner.invoke(
        app,
        ["dataset", "register", "canon", "--catalog", "catalog", "--run", "run", "--desc", "canon ds"],
    )
    assert reg.exit_code == 0, reg.stdout
    dataset_id = _extract_dataset_id(reg.stdout)

    entry = read_json(tmp_path / "catalog" / "entries" / f"{dataset_id}.json")
    manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    expected = manifest["output_files"]["canon.parquet"]["canonical_table_sha256"]

    assert entry["kind"] == "canon_v1"
    assert entry["tz"] == "America/New_York"
    assert entry["fingerprint"]["canon_table_sha256"] == expected
