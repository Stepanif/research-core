from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import pandas as pd
import typer

from research_core.bundle.exporter import export_bundle
from research_core.doctor.bundle_verify import verify_bundle_text
from research_core.doctor.project_doctor import doctor_project_text
from research_core.doctor.run_doctor import doctor_run_text
from research_core.experiments.batch import run_experiment_batch
from research_core.experiments.promote import promote_experiment_label
from research_core.experiments.report import compute_experiments_report
from research_core.experiments.report_writer import build_report_manifest, write_report_artifacts
from research_core.experiments.registry import list_experiment_ids, show_experiment_summary
from research_core.experiments.runner import run_experiment_from_spec_path
from research_core.projects.index import list_projects, refresh_projects_index, show_project_index_entry
from research_core.projects.promotions import promote_project
from research_core.projects.runner import report_project, run_project
from research_core.canon.manifest import build_manifest, write_contract_snapshot, write_manifest
from research_core.canon.normalize import canonicalize_file
from research_core.canon.writer import write_canon_parquet
from research_core.observe.profile import build_observe_profile
from research_core.observe.summarize import build_observe_summary
from research_core.observe.writer import (
    build_observe_manifest,
    build_observe_profile_manifest,
    write_observe_manifest,
    write_observe_profile,
    write_observe_profile_manifest,
    write_observe_summary,
)
from research_core.plan.build import build_plan
from research_core.plan.execute import execute_plan
from research_core.psa.contracts import load_psa_schema_contract
from research_core.psa.engine import run_psa_v1
from research_core.psa.writer import build_psa_manifest, write_psa_log, write_psa_manifest, write_psa_parquet
from research_core.registry.observe_registry import refresh_registry_for_run, show_registry_run
from research_core.registry.dataset_registry import build_dataset_registry
from research_core.registry.run_index import build_run_index
from research_core.util.hashing import sha256_bytes
from research_core.util.io import ensure_dir
from research_core.util.types import ResearchError
from research_core.validate.canon_checks import validate_canon_file

app = typer.Typer(no_args_is_help=True)
validate_app = typer.Typer(no_args_is_help=True)
registry_app = typer.Typer(no_args_is_help=True)
observe_app = typer.Typer(no_args_is_help=True)
bundle_app = typer.Typer(no_args_is_help=True)
experiment_app = typer.Typer(no_args_is_help=True)
project_app = typer.Typer(no_args_is_help=True)
project_index_app = typer.Typer(no_args_is_help=True)
doctor_app = typer.Typer(no_args_is_help=True)
verify_app = typer.Typer(no_args_is_help=True)
plan_app = typer.Typer(no_args_is_help=True)
app.add_typer(validate_app, name="validate")
app.add_typer(registry_app, name="registry")
app.add_typer(observe_app, name="observe")
app.add_typer(bundle_app, name="bundle")
app.add_typer(experiment_app, name="experiment")
app.add_typer(project_app, name="project")
app.add_typer(doctor_app, name="doctor")
app.add_typer(verify_app, name="verify")
app.add_typer(plan_app, name="plan")
project_app.add_typer(project_index_app, name="index")


def _discover_input_files(input_path: Path) -> list[Path]:
    if input_path.is_file():
        return [input_path]
    if input_path.is_dir():
        files = [
            p
            for p in input_path.rglob("*")
            if p.is_file() and p.suffix.lower() in {".txt", ".csv"}
        ]
        return sorted(files, key=lambda p: str(p.as_posix()))
    raise ResearchError(f"Input path does not exist: {input_path}")


def _git_commit_or_unknown(cwd: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=str(cwd),
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip() or "unknown"
    except Exception:  # noqa: BLE001
        return "unknown"


def _run_subdir_name(dataset_root: Path, file_path: Path) -> str:
    rel = str(file_path.relative_to(dataset_root).as_posix()) if file_path.is_relative_to(dataset_root) else file_path.name
    suffix = sha256_bytes(rel.encode("utf-8"))[:10]
    stem = file_path.stem.replace(" ", "_")
    return f"{stem}__{suffix}"


def _write_log(log_path: Path, payload: dict[str, Any]) -> None:
    ensure_dir(log_path.parent)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True, ensure_ascii=False) + "\n")


def _stable_source_ref(input_root: Path, file_path: Path) -> str:
    if input_root.is_dir():
        return file_path.relative_to(input_root).as_posix()
    return file_path.name


def _extract_tz_from_ts_type(ts_type: Any) -> str:
    if not isinstance(ts_type, str):
        raise ResearchError("Canon contract missing timezone metadata: schema_contract.types.ts")
    if "," not in ts_type or not ts_type.endswith("]"):
        raise ResearchError(f"Unsupported canon ts type format for timezone extraction: {ts_type}")
    return ts_type.split(",", 1)[1].rstrip("]").strip()


def _load_canon_session_metadata(run_dir: Path) -> dict[str, str]:
    manifest_path = run_dir / "canon.manifest.json"
    contract_path = run_dir / "canon.contract.json"

    if not manifest_path.exists():
        raise ResearchError(f"Missing canon manifest for psa input run: {manifest_path}")
    if not contract_path.exists():
        raise ResearchError(f"Missing canon contract for psa input run: {contract_path}")

    manifest_payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    contract_payload = json.loads(contract_path.read_text(encoding="utf-8"))

    session_policy = manifest_payload.get("session_policy")
    rth_start = manifest_payload.get("rth_start")
    rth_end = manifest_payload.get("rth_end")
    ts_type = contract_payload.get("schema_contract", {}).get("types", {}).get("ts")
    tz = _extract_tz_from_ts_type(ts_type)

    required = {
        "session_policy": session_policy,
        "rth_start": rth_start,
        "rth_end": rth_end,
        "tz": tz,
    }
    missing = [key for key, value in required.items() if not isinstance(value, str) or not value]
    if missing:
        raise ResearchError(f"Missing required canon session metadata fields: {missing}")

    return {
        "session_policy": session_policy,
        "tz": tz,
        "rth_start": rth_start,
        "rth_end": rth_end,
    }


@app.command("canon")
def canon_command(
    in_path: Path = typer.Option(..., "--in"),
    out_path: Path = typer.Option(..., "--out"),
    instrument: str = typer.Option(..., "--instrument"),
    tf: str = typer.Option(..., "--tf"),
    schema: Path = typer.Option(..., "--schema"),
    colmap: Path = typer.Option(..., "--colmap"),
    session_policy: str = typer.Option("full", "--session-policy"),
    rth_start: str = typer.Option("09:30", "--rth-start"),
    rth_end: str = typer.Option("16:00", "--rth-end"),
    keep_updown: bool = typer.Option(False, "--keep-updown"),
) -> None:
    files = _discover_input_files(in_path)
    if not files:
        raise ResearchError("No input files discovered")

    is_dir_input = in_path.is_dir()
    if is_dir_input:
        ensure_dir(out_path)

    for file_path in files:
        source_ref = _stable_source_ref(in_path, file_path)
        run_dir = out_path
        if is_dir_input:
            run_dir = out_path / _run_subdir_name(in_path, file_path)
        ensure_dir(run_dir)
        ensure_dir(run_dir / "logs")

        canon_df, schema_payload, colmap_payload = canonicalize_file(
            input_path=file_path,
            schema_path=schema,
            colmap_path=colmap,
            instrument=instrument,
            tf=tf,
            session_policy=session_policy,
            rth_start=rth_start,
            rth_end=rth_end,
            keep_updown=keep_updown,
        )

        parquet_path = run_dir / "canon.parquet"
        parquet_hashes = write_canon_parquet(canon_df, parquet_path, keep_updown=keep_updown)

        contract_path = run_dir / "canon.contract.json"
        write_contract_snapshot(
            path=contract_path,
            schema_payload=schema_payload,
            colmap_payload=colmap_payload,
            session_policy=session_policy,
            rth_start=rth_start,
            rth_end=rth_end,
            keep_updown=keep_updown,
            include_instrument_tf_columns=True,
        )

        log_path = run_dir / "logs" / "canon.log"
        _write_log(
            log_path,
            {
                "event": "canon_complete",
                "input_file": source_ref,
                "rowcount": len(canon_df),
                "canonical_table_sha256": parquet_hashes["canonical_table_sha256"],
            },
        )

        manifest = build_manifest(
            run_dir=run_dir,
            input_files=[file_path],
            input_root=in_path,
            canon_df=canon_df,
            parquet_hashes=parquet_hashes,
            schema_version=schema_payload["schema_version"],
            colmap_version=colmap_payload["colmap_version"],
            instrument=instrument,
            tf=tf,
            session_policy=session_policy,
            rth_start=rth_start,
            rth_end=rth_end,
            git_commit=_git_commit_or_unknown(Path(__file__).resolve().parents[2]),
        )
        write_manifest(run_dir / "canon.manifest.json", manifest)


@app.command("psa")
def psa_command(
    in_path: Path = typer.Option(..., "--in"),
    out_path: Path = typer.Option(..., "--out"),
    schema: Path = typer.Option(Path("schemas/psa.schema.v1.json"), "--schema"),
) -> None:
    if not in_path.exists() or not in_path.is_file():
        raise ResearchError(f"Input canon parquet does not exist: {in_path}")

    if in_path.suffix.lower() != ".parquet":
        raise ResearchError(f"Input must be a parquet file: {in_path}")

    canon_run_dir = in_path.parent
    session_metadata = _load_canon_session_metadata(canon_run_dir)

    psa_schema_payload = load_psa_schema_contract(schema)
    canon_df = pd.read_parquet(in_path)
    psa_df = run_psa_v1(canon_df, psa_schema_payload)

    ensure_dir(out_path)
    write_psa_log(psa_df, out_path / "psa.log")
    psa_path = out_path / "psa.parquet"
    parquet_hashes = write_psa_parquet(psa_df, psa_path)

    manifest = build_psa_manifest(
        run_dir=out_path,
        input_files=[in_path],
        input_root=in_path,
        psa_df=psa_df,
        parquet_hashes=parquet_hashes,
        psa_version=psa_schema_payload["psa_version"],
        session_metadata=session_metadata,
        git_commit=_git_commit_or_unknown(Path(__file__).resolve().parents[2]),
    )
    write_psa_manifest(out_path / "psa.manifest.json", manifest)


@observe_app.command("summary")
def observe_summary_command(
    run_dir: Path = typer.Option(..., "--run"),
    top_n: int = typer.Option(25, "--top-n"),
) -> None:
    required_inputs = [
        run_dir / "canon.parquet",
        run_dir / "canon.manifest.json",
        run_dir / "psa.parquet",
        run_dir / "psa.manifest.json",
    ]
    missing = [str(path) for path in required_inputs if not path.exists()]
    if missing:
        raise ResearchError(f"Missing required observe input files: {missing}")

    observe_dir = run_dir / "observe"
    ensure_dir(observe_dir)

    summary_payload, _ = build_observe_summary(run_dir=run_dir, top_n=top_n)
    summary_path = observe_dir / "observe.summary.json"
    write_observe_summary(summary_path, summary_payload)

    observe_manifest_payload = build_observe_manifest(run_dir=run_dir, observe_summary_path=summary_path)
    write_observe_manifest(observe_dir / "observe.summary.manifest.json", observe_manifest_payload)


@observe_app.command("profile")
def observe_profile_command(
    run_dir: Path = typer.Option(..., "--run"),
) -> None:
    required_inputs = [
        run_dir / "psa.parquet",
        run_dir / "psa.manifest.json",
        run_dir / "canon.manifest.json",
    ]
    missing = [str(path) for path in required_inputs if not path.exists()]
    if missing:
        raise ResearchError(f"Missing required observe profile input files: {missing}")

    observe_dir = run_dir / "observe"
    ensure_dir(observe_dir)

    profile_payload, _ = build_observe_profile(run_dir=run_dir, top_n=25)
    profile_path = observe_dir / "observe.profile.json"
    write_observe_profile(profile_path, profile_payload)

    profile_manifest = build_observe_profile_manifest(run_dir=run_dir, observe_profile_path=profile_path)
    write_observe_profile_manifest(observe_dir / "observe.profile.manifest.json", profile_manifest)


@bundle_app.command("export")
def bundle_export_command(
    run_dir: Path = typer.Option(..., "--run"),
    out_path: Path = typer.Option(..., "--out"),
) -> None:
    export_bundle(run_dir=run_dir, bundle_zip_path=out_path)


@experiment_app.command("run")
def experiment_run_command(
    run_dir: Path = typer.Option(..., "--run"),
    spec_path: Path = typer.Option(..., "--spec"),
) -> None:
    run_experiment_from_spec_path(run_dir=run_dir, spec_path=spec_path)


@experiment_app.command("batch")
def experiment_batch_command(
    run_dir: Path = typer.Option(..., "--run"),
    spec_dir: Path = typer.Option(..., "--spec-dir"),
    out_path: Path = typer.Option(..., "--out"),
) -> None:
    run_experiment_batch(run_dir=run_dir, spec_dir=spec_dir, batch_dir=out_path)


@experiment_app.command("promote")
def experiment_promote_command(
    run_dir: Path = typer.Option(..., "--run"),
    exp_id: str = typer.Option(..., "--id"),
    label: str = typer.Option(..., "--label"),
) -> None:
    promote_experiment_label(run_dir=run_dir, exp_id=exp_id, label=label)


@experiment_app.command("report")
def experiment_report_command(
    run_dir: Path = typer.Option(..., "--run"),
) -> None:
    report_payload = compute_experiments_report(run_dir=run_dir)
    manifest_payload = build_report_manifest(run_dir=run_dir, report_payload=report_payload)
    write_report_artifacts(run_dir=run_dir, report_payload=report_payload, report_manifest_payload=manifest_payload)


@experiment_app.command("list")
def experiment_list_command(
    run_dir: Path = typer.Option(..., "--run"),
) -> None:
    payload = {"exp_ids": list_experiment_ids(run_dir=run_dir)}
    typer.echo(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


@experiment_app.command("show")
def experiment_show_command(
    run_dir: Path = typer.Option(..., "--run"),
    exp_id: str = typer.Option(..., "--id"),
) -> None:
    payload = show_experiment_summary(run_dir=run_dir, exp_id=exp_id)
    typer.echo(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


@project_app.command("run")
def project_run_command(
    project_path: Path = typer.Option(..., "--project"),
) -> None:
    run_project(project_path=project_path)


@project_app.command("report")
def project_report_command(
    project_path: Path = typer.Option(..., "--project"),
) -> None:
    report_project(project_path=project_path)


@project_index_app.command("refresh")
def project_index_refresh_command(
    output_dir: Path = typer.Option(..., "--output-dir"),
) -> None:
    refresh_projects_index(output_dir=output_dir)


@project_index_app.command("show")
def project_index_show_command(
    output_dir: Path = typer.Option(..., "--output-dir"),
    project_id: str = typer.Option(..., "--id"),
) -> None:
    payload = show_project_index_entry(output_dir=output_dir, project_id=project_id)
    typer.echo(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


@project_app.command("list")
def project_list_command(
    output_dir: Path = typer.Option(..., "--output-dir"),
) -> None:
    payload = {"project_ids": list_projects(output_dir=output_dir)}
    typer.echo(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


@project_app.command("promote")
def project_promote_command(
    output_dir: Path = typer.Option(..., "--output-dir"),
    project_id: str = typer.Option(..., "--id"),
    label: str = typer.Option(..., "--label"),
) -> None:
    promote_project(output_dir=output_dir, project_id=project_id, label=label)


@doctor_app.command("run")
def doctor_run_command(
    run_dir: Path = typer.Option(..., "--run"),
) -> None:
    text, ok = doctor_run_text(run_dir=run_dir)
    typer.echo(text)
    if not ok:
        raise typer.Exit(code=1)


@doctor_app.command("project")
def doctor_project_command(
    output_dir: Path = typer.Option(..., "--output-dir"),
    project_id: str = typer.Option(..., "--id"),
) -> None:
    text, ok = doctor_project_text(output_dir=output_dir, project_id=project_id)
    typer.echo(text)
    if not ok:
        raise typer.Exit(code=1)


@verify_app.command("bundle")
def verify_bundle_command(
    zip_path: Path = typer.Option(..., "--zip"),
) -> None:
    text, ok = verify_bundle_text(bundle_zip_path=zip_path)
    typer.echo(text)
    if not ok:
        raise typer.Exit(code=1)


@plan_app.command("build")
def plan_build_command(
    project_path: Path = typer.Option(..., "--project"),
    out_path: Path = typer.Option(..., "--out"),
) -> None:
    build_plan(project_path=project_path, out_path=out_path)


@plan_app.command("execute")
def plan_execute_command(
    plan_path: Path = typer.Option(..., "--plan"),
    jobs: int = typer.Option(..., "--jobs"),
) -> None:
    summary_lines, ok = execute_plan(plan_path=plan_path, jobs=jobs)
    for line in summary_lines:
        typer.echo(line)
    if not ok:
        raise typer.Exit(code=1)


@validate_app.command("canon")
def validate_canon_command(
    input_path: Path = typer.Option(..., "--input"),
    schema: Path = typer.Option(..., "--schema"),
    contract: Path | None = typer.Option(None, "--contract"),
) -> None:
    run_dir = input_path.parent
    out_report = run_dir / "validate" / "canon_validate.json"
    ensure_dir(out_report.parent)
    validate_canon_file(input_path=input_path, schema_path=schema, out_report_path=out_report, contract_path=contract)


@registry_app.command("build")
def registry_build_command(
    data_root: Path = typer.Option(..., "--data-root"),
    out_path: Path = typer.Option(..., "--out"),
) -> None:
    ensure_dir(out_path.parent)
    build_dataset_registry(data_root=data_root, out_path=out_path)


@registry_app.command("index-runs")
def registry_index_runs_command(
    runs_root: Path = typer.Option(..., "--runs-root"),
    out_path: Path = typer.Option(..., "--out"),
) -> None:
    ensure_dir(out_path.parent)
    build_run_index(runs_root=runs_root, out_path=out_path)


@registry_app.command("refresh")
def registry_refresh_command(
    run_dir: Path = typer.Option(..., "--run"),
) -> None:
    refresh_registry_for_run(run_dir=run_dir)


@registry_app.command("show")
def registry_show_command(
    run_dir: Path = typer.Option(..., "--run"),
) -> None:
    payload = show_registry_run(run_dir=run_dir)
    typer.echo(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def main() -> None:
    app()


if __name__ == "__main__":
    main()
