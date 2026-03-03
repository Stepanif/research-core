from __future__ import annotations

import json
import shutil
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def extract_runset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("RUNSET_CREATED runset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing runset id in output: {stdout}")


def build_small_run_with_dataset(runner: CliRunner, tmp_path: Path) -> tuple[str, Path, str]:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"
    psa_schema_path = repo_root / "schemas" / "psa.schema.v1.json"

    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "raw-source"])
    assert reg.exit_code == 0, reg.stdout
    dataset_id = extract_dataset_id(reg.stdout)

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
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout

    canon_manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    canon_hash = str(canon_manifest["output_files"]["canon.parquet"]["canonical_table_sha256"])
    return dataset_id, run_dir, canon_hash


def build_small_run_with_dataset_at(
    runner: CliRunner,
    tmp_path: Path,
    *,
    run_dir_name: str,
    raw_root_name: str | None = None,
    raw_dataset_id: str | None = None,
    instrument: str = "ES",
    tf: str = "1min",
) -> tuple[str, Path, str]:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"
    psa_schema_path = repo_root / "schemas" / "psa.schema.v1.json"

    if raw_dataset_id is None:
        if not isinstance(raw_root_name, str) or not raw_root_name:
            raise AssertionError("build_small_run_with_dataset_at requires raw_root_name when raw_dataset_id is not provided")
        raw_root = tmp_path / raw_root_name
        raw_root.mkdir(parents=True, exist_ok=True)
        (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

        reg = runner.invoke(
            app,
            [
                "dataset",
                "register",
                "raw",
                "--catalog",
                "catalog",
                "--root",
                raw_root_name,
                "--desc",
                "raw-source",
            ],
        )
        assert reg.exit_code == 0, reg.stdout
        dataset_id = extract_dataset_id(reg.stdout)
    else:
        dataset_id = raw_dataset_id

    run_dir = tmp_path / run_dir_name
    for args in [
        [
            "canon",
            "--in",
            str(fixture_path),
            "--out",
            run_dir_name,
            "--instrument",
                instrument,
            "--tf",
                tf,
            "--schema",
            str(schema_path),
            "--colmap",
            str(colmap_path),
        ],
        ["psa", "--in", str(run_dir / "canon.parquet"), "--out", run_dir_name, "--schema", str(psa_schema_path)],
        ["observe", "summary", "--run", run_dir_name],
        ["observe", "profile", "--run", run_dir_name],
        ["lineage", "build", "--run", run_dir_name, "--catalog", "catalog", "--raw-dataset-id", dataset_id],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout

    canon_manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    canon_hash = str(canon_manifest["output_files"]["canon.parquet"]["canonical_table_sha256"])
    return dataset_id, run_dir, canon_hash


def create_runset(
    runner: CliRunner,
    tmp_path: Path,
    dataset_id: str,
    canon_hash: str,
    runset_name: str,
    run_ref: str = "run",
    allow_materialize_missing: bool = False,
) -> str:
    runset_spec = tmp_path / f"{runset_name}.json"
    runset_spec.write_text(
        json.dumps(
            {
                "runset_version": "v1",
                "name": runset_name,
                "datasets": [dataset_id],
                "runs": [
                    {
                        "run_ref": run_ref,
                        "dataset_id": dataset_id,
                        "canon_table_sha256": canon_hash,
                    }
                ],
                "policy": {
                    "allow_materialize_missing": allow_materialize_missing,
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
    return extract_runset_id(create.stdout)


def sweep_to_baseline_root(runner: CliRunner, tmp_path: Path, runset_id: str, baseline_root: Path) -> tuple[Path, str]:
    sweep = runner.invoke(app, ["risk", "sweep", "--catalog", "catalog", "--runset", runset_id, "--out", "risk_out"])
    assert sweep.exit_code == 0, sweep.stdout

    source_dir = tmp_path / "risk_out" / runset_id
    card_path = source_dir / "baseline.card.json"
    manifest_path = source_dir / "baseline.card.manifest.json"
    assert card_path.exists()
    assert manifest_path.exists()

    target_dir = baseline_root / runset_id
    target_dir.mkdir(parents=True, exist_ok=True)
    target_card = target_dir / "baseline.card.json"
    target_manifest = target_dir / "baseline.card.manifest.json"

    shutil.copyfile(card_path, target_card)
    shutil.copyfile(manifest_path, target_manifest)

    card_payload = json.loads(target_card.read_text(encoding="utf-8"))
    baseline_id = str(card_payload["checksums"]["per_run_vector_sha256"])
    return target_card, baseline_id


def prepare_promoted_baseline_root(
    runner: CliRunner,
    tmp_path: Path,
    runset_id: str,
    baseline_root: Path,
    label: str = "prod",
) -> tuple[Path, str]:
    card_path, baseline_id = sweep_to_baseline_root(runner, tmp_path, runset_id, baseline_root)

    refresh = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh.exit_code == 0, refresh.stdout

    promote = runner.invoke(
        app,
        [
            "baseline",
            "promote",
            "--root",
            str(baseline_root),
            "--runset",
            runset_id,
            "--baseline-id",
            baseline_id,
            "--label",
            label,
        ],
    )
    assert promote.exit_code == 0, promote.stdout
    return card_path, baseline_id
