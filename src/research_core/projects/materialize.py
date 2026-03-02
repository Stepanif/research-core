from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from research_core.doctor.run_doctor import doctor_run_text
from research_core.datasets.catalog import show_dataset
from research_core.projects.contracts import PROJECT_TOOL_VERSION, canonical_json_bytes, canonical_json_sha256
from research_core.projects.spec import load_project_spec
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def _resolve_path(path_value: str, base_dir: Path) -> Path:
    path = Path(path_value)
    if not path.is_absolute():
        path = (base_dir / path).resolve()
    return path


def _display_label(abs_path: Path, base_dir: Path, original_label: str) -> str:
    if abs_path.is_relative_to(base_dir):
        return abs_path.relative_to(base_dir).as_posix()
    return Path(original_label).as_posix()


def _require_created_utc() -> str:
    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Project materialize requires RESEARCH_CREATED_UTC for deterministic created_utc")
    return created_utc


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _project_id(project_spec: dict[str, Any]) -> str:
    ordered_block: dict[str, Any] = {}
    if "runs" in project_spec:
        ordered_block["runs"] = sorted(project_spec["runs"])
    if "datasets" in project_spec:
        ordered_block["datasets"] = sorted(
            [dict(item) for item in project_spec["datasets"]],
            key=lambda item: (str(item.get("dataset_id", "")), str(item.get("tf", ""))),
        )
    ordered_block["spec_dirs"] = sorted(project_spec["spec_dirs"])

    payload = {
        "spec": project_spec,
        "tool": {"research_project_version": PROJECT_TOOL_VERSION},
        "ordered": ordered_block,
    }
    return sha256_bytes(canonical_json_bytes(payload))


def _resolve_dataset_root(root_ref: str, catalog_dir: Path, project_base_dir: Path) -> Path:
    ref = Path(root_ref)
    if ref.is_absolute():
        return ref

    candidates = [
        (project_base_dir / ref).resolve(),
        (catalog_dir.parent / ref).resolve(),
        (Path.cwd() / ref).resolve(),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise ValidationError(f"Dataset source root could not be resolved for materialize: {root_ref}")


def _run_subprocess(argv: list[str], repo_root: Path, env: dict[str, str]) -> None:
    result = subprocess.run(
        argv,
        cwd=str(repo_root),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise ValidationError(
            f"Materialize command failed (exit={result.returncode}): {' '.join(argv)}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )


def _dataset_run_id(dataset_ref: dict[str, Any], schema_abs: Path, colmap_abs: Path) -> str:
    payload: dict[str, Any] = {
        "dataset_id": dataset_ref["dataset_id"],
        "instrument": dataset_ref["instrument"],
        "tf": dataset_ref["tf"],
        "session_policy": dataset_ref["session_policy"],
        "canon_schema_sha256": sha256_file(schema_abs),
        "colmap_sha256": sha256_file(colmap_abs),
        "tool": {"phase": "materialize", "version": "v1"},
    }
    if dataset_ref["session_policy"] == "rth":
        payload["rth_start"] = dataset_ref["rth_start"]
        payload["rth_end"] = dataset_ref["rth_end"]
    return sha256_bytes(canonical_json_bytes(payload))


def materialize_project(project_path: Path, catalog_dir: Path, runs_root: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    spec = load_project_spec(project_path)
    if "datasets" not in spec:
        raise ValidationError("project materialize requires project spec datasets mode")

    base_dir = project_path.parent.resolve()
    output_abs = _resolve_path(spec["output_dir"], base_dir)
    output_label = _display_label(output_abs, base_dir, spec["output_dir"])
    spec_dirs_abs = [_resolve_path(item, base_dir) for item in spec["spec_dirs"]]

    for spec_dir in spec_dirs_abs:
        if not spec_dir.exists() or not spec_dir.is_dir():
            raise ValidationError(f"Project materialize spec_dir does not exist: {spec_dir}")

    datasets = sorted([dict(item) for item in spec["datasets"]], key=lambda item: (str(item["dataset_id"]), str(item["tf"])))

    runs_root_abs = runs_root.resolve()
    runs_root_abs.mkdir(parents=True, exist_ok=True)

    repo_root = _repo_root()
    env = dict(os.environ)
    env["RESEARCH_CREATED_UTC"] = created_utc

    materialized_runs: list[dict[str, str]] = []
    resolved_run_labels: list[str] = []

    for dataset_ref in datasets:
        dataset_entry = show_dataset(catalog_root=catalog_dir, dataset_id=str(dataset_ref["dataset_id"]))
        kind = dataset_entry.get("kind")
        if kind != "raw_vendor_v1":
            raise ValidationError(f"Project materialize only supports raw_vendor_v1 datasets, got kind={kind}")

        source = dataset_entry.get("source")
        if not isinstance(source, dict):
            raise ValidationError("Dataset source payload invalid for materialize")
        source_files = source.get("files")
        if not isinstance(source_files, list) or len(source_files) != 1:
            raise ValidationError(
                f"Project materialize v1 requires dataset with exactly one source file, dataset_id={dataset_ref['dataset_id']}"
            )
        source_file_row = source_files[0]
        if not isinstance(source_file_row, dict):
            raise ValidationError("Dataset source file row invalid")
        rel_input_file = source_file_row.get("path")
        if not isinstance(rel_input_file, str) or not rel_input_file:
            raise ValidationError("Dataset source file path invalid")

        root_ref = source.get("root")
        if not isinstance(root_ref, str) or not root_ref:
            raise ValidationError("Dataset source root invalid")

        source_root_abs = _resolve_dataset_root(root_ref=root_ref, catalog_dir=catalog_dir.resolve(), project_base_dir=base_dir)
        input_file_abs = (source_root_abs / rel_input_file).resolve()
        if not input_file_abs.exists() or not input_file_abs.is_file():
            raise ValidationError(f"Dataset source input file missing for materialize: {input_file_abs}")

        schema_abs = _resolve_path(str(dataset_ref["schema_path"]), base_dir)
        colmap_abs = _resolve_path(str(dataset_ref["colmap_path"]), base_dir)
        if not schema_abs.exists() or not schema_abs.is_file():
            raise ValidationError(f"Materialize schema_path does not exist: {schema_abs}")
        if not colmap_abs.exists() or not colmap_abs.is_file():
            raise ValidationError(f"Materialize colmap_path does not exist: {colmap_abs}")

        run_id = _dataset_run_id(dataset_ref=dataset_ref, schema_abs=schema_abs, colmap_abs=colmap_abs)
        run_rel = Path("runs") / run_id
        run_dir = runs_root_abs / run_rel

        if run_dir.exists():
            text, ok = doctor_run_text(run_dir=run_dir)
            if not ok:
                raise ValidationError(f"Existing run_dir failed doctor run during materialize reuse: {run_dir}\n{text}")
        else:
            run_dir.parent.mkdir(parents=True, exist_ok=True)

            canon_cmd = [
                sys.executable,
                "-m",
                "research_core.cli",
                "canon",
                "--in",
                str(input_file_abs),
                "--out",
                str(run_dir),
                "--instrument",
                str(dataset_ref["instrument"]),
                "--tf",
                str(dataset_ref["tf"]),
                "--schema",
                str(schema_abs),
                "--colmap",
                str(colmap_abs),
                "--session-policy",
                str(dataset_ref["session_policy"]),
                "--catalog",
                str(catalog_dir.resolve()),
                "--raw-dataset-id",
                str(dataset_ref["dataset_id"]),
            ]
            if dataset_ref["session_policy"] == "rth":
                canon_cmd.extend(["--rth-start", str(dataset_ref["rth_start"]), "--rth-end", str(dataset_ref["rth_end"])])

            _run_subprocess(canon_cmd, repo_root=repo_root, env=env)
            _run_subprocess(
                [
                    sys.executable,
                    "-m",
                    "research_core.cli",
                    "psa",
                    "--in",
                    str(run_dir / "canon.parquet"),
                    "--out",
                    str(run_dir),
                ],
                repo_root=repo_root,
                env=env,
            )
            _run_subprocess(
                [sys.executable, "-m", "research_core.cli", "observe", "summary", "--run", str(run_dir)],
                repo_root=repo_root,
                env=env,
            )
            _run_subprocess(
                [sys.executable, "-m", "research_core.cli", "observe", "profile", "--run", str(run_dir)],
                repo_root=repo_root,
                env=env,
            )
            _run_subprocess(
                [sys.executable, "-m", "research_core.cli", "registry", "refresh", "--run", str(run_dir)],
                repo_root=repo_root,
                env=env,
            )
            _run_subprocess(
                [
                    sys.executable,
                    "-m",
                    "research_core.cli",
                    "lineage",
                    "build",
                    "--run",
                    str(run_dir),
                    "--catalog",
                    str(catalog_dir.resolve()),
                    "--raw-dataset-id",
                    str(dataset_ref["dataset_id"]),
                ],
                repo_root=repo_root,
                env=env,
            )

        run_label = run_rel.as_posix()
        resolved_run_labels.append(run_label)
        materialized_runs.append(
            {
                "dataset_id": str(dataset_ref["dataset_id"]),
                "run_dir": run_label,
                "status": "PASS",
            }
        )

    project_spec_for_id = {
        "project_version": spec["project_version"],
        "name": spec["name"],
        "runs": sorted(resolved_run_labels),
        "spec_dirs": sorted([_display_label(path, base_dir, original_label=path.as_posix()) for path in spec_dirs_abs]),
        "output_dir": output_label,
        "policy": spec["policy"],
        **({"notes": spec["notes"]} if "notes" in spec else {}),
    }
    project_id = _project_id(project_spec_for_id)

    summary_payload: dict[str, Any] = {
        "materialize_version": "v1",
        "project_id": project_id,
        "created_utc": created_utc,
        "runs": sorted(materialized_runs, key=lambda item: (str(item["dataset_id"]), str(item["run_dir"]))),
    }

    output_dir = output_abs / project_id
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_path = output_dir / "materialize.summary.json"
    summary_path.write_bytes(canonical_json_bytes(summary_payload))

    inputs: list[dict[str, Any]] = [
        {
            "path": Path(project_path.name).as_posix(),
            "bytes": int(project_path.stat().st_size),
            "sha256": sha256_file(project_path),
        }
    ]
    for row in summary_payload["runs"]:
        run_dir = (runs_root_abs / str(row["run_dir"])).resolve()
        lineage_path = run_dir / "lineage" / "lineage.json"
        inputs.append(
            {
                "path": f"{Path(str(row['run_dir'])).as_posix()}/lineage/lineage.json",
                "bytes": int(lineage_path.stat().st_size),
                "sha256": sha256_file(lineage_path),
            }
        )

    manifest_payload: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": created_utc,
        "inputs": sorted(inputs, key=lambda item: str(item["path"])),
        "outputs": {
            "materialize.summary.json": {
                "bytes": len(canonical_json_bytes(summary_payload)),
                "sha256": sha256_bytes(canonical_json_bytes(summary_payload)),
            }
        },
    }
    manifest_payload["materialize_manifest_canonical_sha256"] = canonical_json_sha256(
        manifest_payload,
        self_hash_key="materialize_manifest_canonical_sha256",
    )

    manifest_path = output_dir / "materialize.manifest.json"
    manifest_path.write_bytes(canonical_json_bytes(manifest_payload))

    return {
        "project_id": project_id,
        "summary": summary_payload,
        "manifest": manifest_payload,
        "output_dir": output_dir,
    }
