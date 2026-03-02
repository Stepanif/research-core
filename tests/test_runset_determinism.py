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


def _extract_runset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("RUNSET_CREATED runset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing runset id in output: {stdout}")


def _canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def test_runset_determinism(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()

    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw"])
    assert reg.exit_code == 0, reg.stdout
    dataset_id = _extract_dataset_id(reg.stdout)

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

    lineage = runner.invoke(app, ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", dataset_id])
    assert lineage.exit_code == 0, lineage.stdout

    canon_manifest = json.loads((tmp_path / "run" / "canon.manifest.json").read_text(encoding="utf-8"))
    canon_hash = canon_manifest["output_files"]["canon.parquet"]["canonical_table_sha256"]

    spec_path = tmp_path / "runset.json"
    spec_path.write_text(
        json.dumps(
            {
                "runset_version": "v1",
                "name": "runset-determinism",
                "datasets": [dataset_id],
                "runs": [
                    {
                        "run_ref": "run",
                        "dataset_id": dataset_id,
                        "canon_table_sha256": canon_hash,
                    }
                ],
                "policy": {
                    "allow_materialize_missing": False,
                    "require_lineage_links": True,
                    "require_bidirectional": True,
                },
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    first = runner.invoke(app, ["runset", "create", "--catalog", "catalog", "--spec", str(spec_path)])
    assert first.exit_code == 0, first.stdout
    runset_id = _extract_runset_id(first.stdout)

    entry_path = tmp_path / "catalog" / "runsets" / "entries" / f"{runset_id}.json"
    index_path = tmp_path / "catalog" / "runsets" / "runsets.index.json"

    entry_hash_1 = _canonical_hash(entry_path)
    index_hash_1 = _canonical_hash(index_path)

    second = runner.invoke(app, ["runset", "create", "--catalog", "catalog", "--spec", str(spec_path)])
    assert second.exit_code == 0, second.stdout

    entry_hash_2 = _canonical_hash(entry_path)
    index_hash_2 = _canonical_hash(index_path)

    assert entry_hash_1 == entry_hash_2
    assert index_hash_1 == index_hash_2
