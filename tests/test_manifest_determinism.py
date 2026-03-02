from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app
from research_core.util.hashing import sha256_file


def test_canonical_table_hash_deterministic_across_runs(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()
    fixture = Path("tests/fixtures/raw_small_sample.txt").resolve()
    schema = Path("schemas/canon.schema.v1.json").resolve()
    colmap = Path("schemas/colmap.raw_vendor_v1.json").resolve()

    run1 = tmp_path / "run1"
    run2 = tmp_path / "run2"
    args = [
        "canon",
        "--in",
        str(fixture),
        "--out",
        str(run1),
        "--instrument",
        "ES",
        "--tf",
        "1min",
        "--schema",
        str(schema),
        "--colmap",
        str(colmap),
    ]
    cwd1 = Path.cwd()
    cwd2 = tmp_path / "cwd2"
    cwd2.mkdir(parents=True)
    monkeypatch.chdir(cwd1)
    result1 = runner.invoke(app, args)
    assert result1.exit_code == 0, result1.stdout

    args[4] = str(run2)
    monkeypatch.chdir(cwd2)
    result2 = runner.invoke(app, args)
    assert result2.exit_code == 0, result2.stdout

    manifest1 = json.loads((run1 / "canon.manifest.json").read_text(encoding="utf-8"))
    manifest2 = json.loads((run2 / "canon.manifest.json").read_text(encoding="utf-8"))
    assert (
        manifest1["output_files"]["canon.parquet"]["canonical_table_sha256"]
        == manifest2["output_files"]["canon.parquet"]["canonical_table_sha256"]
    )
    assert manifest1["input_files"][0]["path"] == "raw_small_sample.txt"
    assert manifest2["input_files"][0]["path"] == "raw_small_sample.txt"
    assert sha256_file(run1 / "canon.manifest.json") == sha256_file(run2 / "canon.manifest.json")


def test_directory_traversal_stable_order(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()

    inp = tmp_path / "raw"
    (inp / "b").mkdir(parents=True)
    (inp / "a").mkdir(parents=True)
    sample = Path("tests/fixtures/raw_small_sample.txt").read_text(encoding="utf-8")
    (inp / "b" / "x.txt").write_text(sample, encoding="utf-8")
    (inp / "a" / "y.txt").write_text(sample, encoding="utf-8")

    out = tmp_path / "runs"
    result = runner.invoke(
        app,
        [
            "canon",
            "--in",
            str(inp),
            "--out",
            str(out),
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

    run_dirs = sorted([p.name for p in out.iterdir() if p.is_dir()])
    assert run_dirs == sorted(run_dirs)

    manifest_paths = set()
    for run_dir in out.iterdir():
        if run_dir.is_dir():
            manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
            manifest_paths.add(manifest["input_files"][0]["path"])
    assert manifest_paths == {"a/y.txt", "b/x.txt"}
