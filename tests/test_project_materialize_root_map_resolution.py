from __future__ import annotations

import inspect
import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app
from research_core.datasets.io import canonical_json_bytes, read_json, write_canonical_json
from research_core.util.hashing import sha256_bytes


def _extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def _update_entry_source_root(catalog_dir: Path, dataset_id: str, new_root: str) -> None:
    entry_path = catalog_dir / "entries" / f"{dataset_id}.json"
    payload = read_json(entry_path)
    assert isinstance(payload, dict)
    source = payload.get("source")
    assert isinstance(source, dict)
    source["root"] = new_root

    body = {key: value for key, value in payload.items() if key != "dataset_entry_canonical_sha256"}
    payload["dataset_entry_canonical_sha256"] = sha256_bytes(canonical_json_bytes(body).rstrip(b"\n"))
    write_canonical_json(entry_path, payload)


def _build_project_spec(project_dir: Path, dataset_id: str) -> Path:
    repo_root = Path(__file__).parent.parent
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"

    specs_dir = project_dir / "specs"
    specs_dir.mkdir(parents=True, exist_ok=True)
    (specs_dir / "spec_01.json").write_text(
        (repo_root / "tests" / "fixtures" / "exp_specs" / "spec_01_global_min.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    project_path = project_dir / "project.json"
    project_path.write_text(
        json.dumps(
            {
                "project_version": "v1",
                "name": "project-materialize-root-map",
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
    return project_path


def _register_dataset_for_root(catalog_dir: Path, root_dir: Path) -> str:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"

    root_dir.mkdir(parents=True, exist_ok=True)
    (root_dir / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    runner = CliRunner()
    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", str(catalog_dir), "--root", str(root_dir)])
    assert reg.exit_code == 0, reg.stdout
    return _extract_dataset_id(reg.stdout)


def _materialize(runner: CliRunner, project_path: Path, catalog_dir: Path, runs_root: Path):
    return runner.invoke(
        app,
        [
            "project",
            "materialize",
            "--project",
            str(project_path),
            "--catalog",
            str(catalog_dir),
            "--runs-root",
            str(runs_root),
        ],
    )


def test_materialize_resolver_source_contains_root_map_env() -> None:
    import research_core.projects.materialize as materialize

    source = inspect.getsource(materialize._resolve_dataset_root)
    assert "RESEARCH_DATA_ROOT_MAP_JSON" in source


def test_materialize_relative_root_fails_without_map(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.delenv("RESEARCH_DATA_ROOT_MAP_JSON", raising=False)
    cwd = tmp_path / "cwd_empty"
    cwd.mkdir(parents=True, exist_ok=True)
    monkeypatch.chdir(cwd)

    proj_dir = tmp_path / "proj"
    proj_dir.mkdir(parents=True, exist_ok=True)

    cat_dir = tmp_path / "cat"
    cat_dir.mkdir(parents=True, exist_ok=True)

    runs_root = tmp_path / "runs_root"
    runs_root.mkdir(parents=True, exist_ok=True)

    relative_root = "Raw CSVs/Futures/Indicies/ES/ES 15min 2015-2025"

    monkeypatch.chdir(tmp_path)
    external_root_rel = Path("external_store") / "seed_root"
    dataset_id = _register_dataset_for_root(cat_dir, external_root_rel)
    _update_entry_source_root(cat_dir, dataset_id, relative_root)
    monkeypatch.chdir(cwd)

    project_path = _build_project_spec(proj_dir, dataset_id)
    runner = CliRunner()
    result = _materialize(runner, project_path, cat_dir, runs_root)

    assert result.exit_code != 0
    assert result.exception is not None
    assert f"Dataset source root could not be resolved for materialize: {relative_root}" in str(result.exception)


def test_materialize_relative_root_resolves_with_map(monkeypatch: object, tmp_path: Path) -> None:
    cwd = tmp_path / "cwd_empty"
    cwd.mkdir(parents=True, exist_ok=True)
    monkeypatch.chdir(cwd)

    proj_dir = tmp_path / "proj"
    proj_dir.mkdir(parents=True, exist_ok=True)

    cat_dir = tmp_path / "cat"
    cat_dir.mkdir(parents=True, exist_ok=True)

    runs_root = tmp_path / "runs_root"
    runs_root.mkdir(parents=True, exist_ok=True)

    relative_root = "Raw CSVs/Futures/Indicies/ES/ES 15min 2015-2025"

    base_abs = tmp_path / "lake" / "Raw CSVs"
    base_abs.mkdir(parents=True, exist_ok=True)
    remainder = Path(relative_root).relative_to("Raw CSVs")
    root_rel = Path("lake") / "Raw CSVs" / remainder

    monkeypatch.chdir(tmp_path)
    dataset_id = _register_dataset_for_root(cat_dir, root_rel)
    _update_entry_source_root(cat_dir, dataset_id, relative_root)
    monkeypatch.chdir(cwd)

    monkeypatch.setenv("RESEARCH_DATA_ROOT_MAP_JSON", json.dumps({"Raw CSVs": str(base_abs)}))

    project_path = _build_project_spec(proj_dir, dataset_id)
    runner = CliRunner()
    result = _materialize(runner, project_path, cat_dir, runs_root)

    assert result.exit_code == 0, result.stdout


def test_materialize_root_map_invalid_json_fails_loud(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    relative_root = "Raw CSVs/Futures/Indicies/ES/ES 15min 2015-2025"

    external_root = tmp_path / "external_store" / "Raw CSVs" / "Futures" / "Indicies" / "ES" / "ES 15min 2015-2025"
    dataset_id = _register_dataset_for_root(tmp_path / "catalog", external_root)
    _update_entry_source_root(tmp_path / "catalog", dataset_id, relative_root)

    monkeypatch.setenv("RESEARCH_DATA_ROOT_MAP_JSON", "{invalid")

    project_path = _build_project_spec(tmp_path, dataset_id)
    runner = CliRunner()
    result = _materialize(runner, project_path, tmp_path / "catalog", tmp_path / "runs_root")

    assert result.exit_code != 0
    assert result.exception is not None
    assert "RESEARCH_DATA_ROOT_MAP_JSON is invalid JSON" in str(result.exception)


def test_materialize_root_map_non_absolute_base_fails_loud(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    relative_root = "Raw CSVs/Futures/Indicies/ES/ES 15min 2015-2025"

    external_root = tmp_path / "external_store" / "Raw CSVs" / "Futures" / "Indicies" / "ES" / "ES 15min 2015-2025"
    dataset_id = _register_dataset_for_root(tmp_path / "catalog", external_root)
    _update_entry_source_root(tmp_path / "catalog", dataset_id, relative_root)

    monkeypatch.setenv("RESEARCH_DATA_ROOT_MAP_JSON", json.dumps({"Raw CSVs": "relative/base"}))

    project_path = _build_project_spec(tmp_path, dataset_id)
    runner = CliRunner()
    result = _materialize(runner, project_path, tmp_path / "catalog", tmp_path / "runs_root")

    assert result.exit_code != 0
    assert result.exception is not None
    assert "Mapped base for prefix Raw CSVs must be absolute" in str(result.exception)
