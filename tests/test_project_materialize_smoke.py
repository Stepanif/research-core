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


def test_project_materialize_smoke(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "source"])
    assert reg.exit_code == 0, reg.stdout
    dataset_id = _extract_dataset_id(reg.stdout)

    specs_dir = tmp_path / "specs"
    specs_dir.mkdir(parents=True, exist_ok=True)
    (specs_dir / "spec_01.json").write_text(
        (repo_root / "tests" / "fixtures" / "exp_specs" / "spec_01_global_min.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    project_path = tmp_path / "project.json"
    project_path.write_text(
        json.dumps(
            {
                "project_version": "v1",
                "name": "project-materialize-smoke",
                "datasets": [
                    {
                        "dataset_id": dataset_id,
                        "instrument": "ES",
                        "tf": "1min",
                        "session_policy": "full",
                        "schema_path": str(schema_path),
                        "colmap_path": str(colmap_path),
                    }
                ],
                "spec_dirs": ["specs"],
                "output_dir": "project_outputs",
                "policy": {"fail_fast": True, "require_observe": False},
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    runs_root = tmp_path / "runs_root"
    result = runner.invoke(
        app,
        [
            "project",
            "materialize",
            "--project",
            str(project_path),
            "--catalog",
            str(tmp_path / "catalog"),
            "--runs-root",
            str(runs_root),
        ],
    )
    assert result.exit_code == 0, result.stdout

    project_output_root = tmp_path / "project_outputs"
    project_dir = sorted([path for path in project_output_root.iterdir() if path.is_dir()])[0]
    summary = json.loads((project_dir / "materialize.summary.json").read_text(encoding="utf-8"))

    assert isinstance(summary.get("runs"), list) and len(summary["runs"]) == 1
    run_dir = (runs_root / str(summary["runs"][0]["run_dir"]))

    assert (run_dir / "canon.parquet").exists()
    assert (run_dir / "canon.manifest.json").exists()
    assert (run_dir / "psa.parquet").exists()
    assert (run_dir / "psa.manifest.json").exists()
    assert (run_dir / "observe" / "observe.summary.json").exists()
    assert (run_dir / "observe" / "observe.profile.json").exists()
    assert (run_dir / "lineage" / "lineage.json").exists()
    assert (run_dir.parent / "index.json").exists()
    assert (tmp_path / "catalog" / "links" / "dataset_to_runs.index.json").exists()
