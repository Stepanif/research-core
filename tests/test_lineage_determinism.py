from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

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


def test_lineage_determinism(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw"])
    assert reg.exit_code == 0, reg.stdout
    raw_dataset_id = _extract_dataset_id(reg.stdout)

    run_dir = tmp_path / "run"
    canon = runner.invoke(
        app,
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
    )
    assert canon.exit_code == 0, canon.stdout

    first = runner.invoke(app, ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", raw_dataset_id])
    assert first.exit_code == 0, first.stdout

    lineage_hash_1 = hashlib.sha256((run_dir / "lineage" / "lineage.json").read_bytes()).hexdigest()
    index_hash_1 = _canonical_hash(tmp_path / "catalog" / "links" / "dataset_to_runs.index.json")

    second = runner.invoke(app, ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", raw_dataset_id])
    assert second.exit_code == 0, second.stdout

    lineage_hash_2 = hashlib.sha256((run_dir / "lineage" / "lineage.json").read_bytes()).hexdigest()
    index_hash_2 = _canonical_hash(tmp_path / "catalog" / "links" / "dataset_to_runs.index.json")

    assert lineage_hash_1 == lineage_hash_2
    assert index_hash_1 == index_hash_2
