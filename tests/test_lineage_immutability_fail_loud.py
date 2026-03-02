from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def _extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def test_lineage_immutability_fail_loud(monkeypatch: object, tmp_path: Path) -> None:
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

    contract_path = tmp_path / "run" / "canon.contract.json"
    contract_payload = json.loads(contract_path.read_text(encoding="utf-8"))
    contract_payload["colmap_contract"]["mapping"]["Open"] = "open_mutated"
    contract_path.write_text(json.dumps(contract_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")

    second = runner.invoke(app, ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", raw_dataset_id])
    assert second.exit_code != 0
    message = str(second.exception or second.stdout).lower()
    assert "immutable" in message or "conflict" in message


def test_lineage_missing_dataset_id_fail_loud(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
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

    build = runner.invoke(
        app,
        [
            "lineage",
            "build",
            "--run",
            "run",
            "--catalog",
            "catalog",
            "--raw-dataset-id",
            "does-not-exist",
        ],
    )
    assert build.exit_code != 0
