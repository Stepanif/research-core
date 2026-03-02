from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def test_project_materialize_fail_if_unregistered_dataset(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
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
                "name": "project-materialize-missing-dataset",
                "datasets": [
                    {
                        "dataset_id": "does-not-exist",
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
            str(tmp_path / "runs_root"),
        ],
    )
    assert result.exit_code != 0
