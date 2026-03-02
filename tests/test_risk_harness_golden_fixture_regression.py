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


def test_risk_harness_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
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
    dataset_id = _extract_dataset_id(reg.stdout)

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
        ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", dataset_id],
        ["risk", "run", "--run", "run"],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout

    canon_manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    canon_hash = canon_manifest["output_files"]["canon.parquet"]["canonical_table_sha256"]

    runset_spec = tmp_path / "runset_risk_golden.json"
    runset_spec.write_text(
        json.dumps(
            {
                "runset_version": "v1",
                "name": "runset-risk-golden",
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

    create = runner.invoke(app, ["runset", "create", "--catalog", "catalog", "--spec", str(runset_spec)])
    assert create.exit_code == 0, create.stdout
    runset_id = _extract_runset_id(create.stdout)

    risk_runset = runner.invoke(
        app,
        ["risk", "runset", "--catalog", "catalog", "--id", runset_id, "--out", "risk_out"],
    )
    assert risk_runset.exit_code == 0, risk_runset.stdout

    risk_summary_bytes_hash = hashlib.sha256((run_dir / "risk" / "risk.summary.json").read_bytes()).hexdigest()
    risk_manifest_hash = _canonical_hash(run_dir / "risk" / "risk.summary.manifest.json")

    runset_summary_path = tmp_path / "risk_out" / runset_id / "risk.runset.summary.json"
    runset_manifest_path = tmp_path / "risk_out" / runset_id / "risk.runset.manifest.json"

    runset_summary_bytes_hash = hashlib.sha256(runset_summary_path.read_bytes()).hexdigest()
    runset_manifest_hash = _canonical_hash(runset_manifest_path)

    expected_risk_summary_hash = (repo_root / "tests" / "golden" / "risk_small_sample_v1.risk.summary.json.sha256").read_text(encoding="utf-8").strip()
    expected_risk_manifest_hash = (
        repo_root / "tests" / "golden" / "risk_small_sample_v1.risk.summary.manifest.json.sha256"
    ).read_text(encoding="utf-8").strip()
    expected_runset_summary_hash = (
        repo_root / "tests" / "golden" / "risk_small_sample_v1.risk.runset.summary.json.sha256"
    ).read_text(encoding="utf-8").strip()
    expected_runset_manifest_hash = (
        repo_root / "tests" / "golden" / "risk_small_sample_v1.risk.runset.manifest.json.sha256"
    ).read_text(encoding="utf-8").strip()

    assert risk_summary_bytes_hash == expected_risk_summary_hash
    assert risk_manifest_hash == expected_risk_manifest_hash
    assert runset_summary_bytes_hash == expected_runset_summary_hash
    assert runset_manifest_hash == expected_runset_manifest_hash
