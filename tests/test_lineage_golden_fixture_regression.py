from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def _canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def test_lineage_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"
    psa_schema_path = repo_root / "schemas" / "psa.schema.v1.json"

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "raw-source"])
    assert reg.exit_code == 0, reg.stdout
    raw_dataset_id = _extract_dataset_id(reg.stdout)

    run_dir = tmp_path / "run"
    for args in [
        [
            "canon",
            "--in",
            str(fixture_path),
            "--out",
            "run",
            "--instrument",
            "ES",
            "--tf",
            "1min",
            "--schema",
            str(schema_path),
            "--colmap",
            str(colmap_path),
        ],
        ["psa", "--in", str(run_dir / "canon.parquet"), "--out", "run", "--schema", str(psa_schema_path)],
        ["observe", "summary", "--run", "run"],
        ["observe", "profile", "--run", "run"],
        ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", raw_dataset_id],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout

    lineage_bytes_hash = hashlib.sha256((run_dir / "lineage" / "lineage.json").read_bytes()).hexdigest()
    lineage_manifest_canonical_hash = _canonical_hash(run_dir / "lineage" / "lineage.manifest.json")
    index_canonical_hash = _canonical_hash(tmp_path / "catalog" / "links" / "dataset_to_runs.index.json")

    expected_lineage_hash = (repo_root / "tests" / "golden" / "lineage_small_sample_v1.lineage.json.sha256").read_text(encoding="utf-8").strip()
    expected_manifest_hash = (repo_root / "tests" / "golden" / "lineage_small_sample_v1.lineage.manifest.json.sha256").read_text(encoding="utf-8").strip()
    expected_index_hash = (repo_root / "tests" / "golden" / "lineage_small_sample_v1.dataset_to_runs.index.json.sha256").read_text(encoding="utf-8").strip()

    assert lineage_bytes_hash == expected_lineage_hash
    assert lineage_manifest_canonical_hash == expected_manifest_hash
    assert index_canonical_hash == expected_index_hash
