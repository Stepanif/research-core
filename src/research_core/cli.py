from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd
import typer

from research_core.ci_doctor.runner import run_ci_doctor
from research_core.ci.runner import run_ci_pipeline
from research_core.bundle.exporter import export_bundle
from research_core.baselines.index import refresh_baseline_index, show_baseline_index
from research_core.baselines.promotions import promote_baseline
from research_core.baselines.resolve import resolve_baseline
from research_core.doctor.bundle_verify import verify_bundle_text
from research_core.doctor.project_doctor import doctor_project_text
from research_core.doctor.run_doctor import doctor_run_text
from research_core.datasets.catalog import (
    list_datasets,
    register_canon_dataset,
    register_raw_dataset,
    show_dataset,
    validate_dataset,
)
from research_core.experiments.batch import run_experiment_batch
from research_core.experiments.promote import promote_experiment_label
from research_core.experiments.report import compute_experiments_report
from research_core.experiments.report_writer import build_report_manifest, write_report_artifacts
from research_core.experiments.registry import list_experiment_ids, show_experiment_summary
from research_core.experiments.runner import run_experiment_from_spec_path
from research_core.projects.index import list_projects, refresh_projects_index, show_project_index_entry
from research_core.projects.materialize import materialize_project
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
from research_core.lineage.build_lineage import build_lineage_for_run
from research_core.runsets.catalog import create_runset, list_runsets, show_runset, validate_runset
from research_core.runsets.materialize import materialize_runset
from research_core.risk.diff_writer import write_baseline_diff_artifacts
from research_core.risk.dashboard import run_risk_dashboard
from research_core.risk.drift import run_risk_drift
from research_core.risk.sweep import run_risk_sweep
from research_core.risk.runset_agg import compute_runset_risk
from research_core.risk.writer import write_risk_artifacts
from research_core.plan.build import build_plan
from research_core.plan.execute import execute_plan
from research_core.psa.contracts import load_psa_schema_contract
from research_core.psa.engine import run_psa_v1
from research_core.psa.writer import build_psa_manifest, write_psa_log, write_psa_manifest, write_psa_parquet
from research_core.registry.observe_registry import refresh_registry_for_run, show_registry_run
from research_core.registry.dataset_registry import build_dataset_registry
from research_core.registry.run_index import build_run_index
from research_core.prune.executor import execute_plan as execute_prune_plan
from research_core.prune.formatting import format_prune_report
from research_core.prune.planner import build_prune_plan
from research_core.prune.policy import load_prune_policy
from research_core.release.draft import write_release_draft
from research_core.release.notes import generate_release_notes
from research_core.release.url import build_new_release_url
from research_core.util.hashing import sha256_bytes
from research_core.util.io import ensure_dir
from research_core.util.buildmeta import get_git_commit
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
dataset_app = typer.Typer(no_args_is_help=True)
dataset_register_app = typer.Typer(no_args_is_help=True)
lineage_app = typer.Typer(no_args_is_help=True)
runset_app = typer.Typer(no_args_is_help=True)
risk_app = typer.Typer(no_args_is_help=True)
baseline_app = typer.Typer(no_args_is_help=True)
baseline_index_app = typer.Typer(no_args_is_help=True)
ci_app = typer.Typer(no_args_is_help=True)
release_app = typer.Typer(no_args_is_help=True)
prune_app = typer.Typer(no_args_is_help=True)
app.add_typer(validate_app, name="validate")
app.add_typer(registry_app, name="registry")
app.add_typer(observe_app, name="observe")
app.add_typer(bundle_app, name="bundle")
app.add_typer(experiment_app, name="experiment")
app.add_typer(project_app, name="project")
app.add_typer(doctor_app, name="doctor")
app.add_typer(verify_app, name="verify")
app.add_typer(plan_app, name="plan")
app.add_typer(dataset_app, name="dataset")
app.add_typer(lineage_app, name="lineage")
app.add_typer(runset_app, name="runset")
app.add_typer(risk_app, name="risk")
app.add_typer(baseline_app, name="baseline")
app.add_typer(ci_app, name="ci")
app.add_typer(release_app, name="release")
app.add_typer(prune_app, name="prune")
project_app.add_typer(project_index_app, name="index")
dataset_app.add_typer(dataset_register_app, name="register")
baseline_app.add_typer(baseline_index_app, name="index")


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


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _git_commit_or_unknown(_: Path) -> str:
    return get_git_commit(_repo_root())


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
    raw_dataset_id: str | None = typer.Option(None, "--raw-dataset-id"),
    catalog_dir: Path | None = typer.Option(None, "--catalog"),
) -> None:
    if raw_dataset_id and not catalog_dir:
        raise ResearchError("canon --raw-dataset-id requires --catalog")
    if raw_dataset_id and catalog_dir:
        show_dataset(catalog_root=catalog_dir, dataset_id=raw_dataset_id)

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
            git_commit=_git_commit_or_unknown(_repo_root()),
        )
        write_manifest(run_dir / "canon.manifest.json", manifest)

        if catalog_dir is not None and (run_dir / "psa.manifest.json").exists():
            build_lineage_for_run(
                run_dir=run_dir,
                catalog_dir=catalog_dir,
                raw_dataset_id=raw_dataset_id,
                canon_dataset_id=None,
            )


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
        git_commit=_git_commit_or_unknown(_repo_root()),
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


@project_app.command("materialize")
def project_materialize_command(
    project_path: Path = typer.Option(..., "--project"),
    catalog_dir: Path = typer.Option(..., "--catalog"),
    runs_root: Path = typer.Option(..., "--runs-root"),
) -> None:
    result = materialize_project(project_path=project_path, catalog_dir=catalog_dir, runs_root=runs_root)
    typer.echo(f"MATERIALIZED project_id={result['project_id']}")


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
    allow_existing: bool = typer.Option(False, "--allow-existing"),
) -> None:
    summary_lines, ok = execute_plan(plan_path=plan_path, jobs=jobs, allow_existing=allow_existing)
    for line in summary_lines:
        typer.echo(line)
    if not ok:
        raise typer.Exit(code=1)


@dataset_register_app.command("raw")
def dataset_register_raw_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    root_dir: Path = typer.Option(..., "--root"),
    description: str | None = typer.Option(None, "--desc"),
    tz: str | None = typer.Option(None, "--tz"),
) -> None:
    entry = register_raw_dataset(catalog_root=catalog_dir, root_dir=root_dir, description=description, tz=tz)
    typer.echo(f"REGISTERED dataset_id={entry['dataset_id']}")


@dataset_register_app.command("canon")
def dataset_register_canon_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    run_dir: Path = typer.Option(..., "--run"),
    description: str | None = typer.Option(None, "--desc"),
) -> None:
    entry = register_canon_dataset(catalog_root=catalog_dir, run_dir=run_dir, description=description)
    lineage_path = run_dir / "lineage" / "lineage.json"
    if lineage_path.exists() and lineage_path.is_file():
        lineage_payload = json.loads(lineage_path.read_text(encoding="utf-8"))
        raw_dataset_id = lineage_payload.get("inputs", {}).get("raw_dataset_id") if isinstance(lineage_payload, dict) else None
        build_lineage_for_run(
            run_dir=run_dir,
            catalog_dir=catalog_dir,
            raw_dataset_id=raw_dataset_id if isinstance(raw_dataset_id, str) and raw_dataset_id else None,
            canon_dataset_id=str(entry["dataset_id"]),
        )
    typer.echo(f"REGISTERED dataset_id={entry['dataset_id']}")


@lineage_app.command("build")
def lineage_build_command(
    run_dir: Path = typer.Option(..., "--run"),
    catalog_dir: Path = typer.Option(..., "--catalog"),
    raw_dataset_id: str | None = typer.Option(None, "--raw-dataset-id"),
    canon_dataset_id: str | None = typer.Option(None, "--canon-dataset-id"),
) -> None:
    payload = build_lineage_for_run(
        run_dir=run_dir,
        catalog_dir=catalog_dir,
        raw_dataset_id=raw_dataset_id,
        canon_dataset_id=canon_dataset_id,
    )
    typer.echo(f"LINEAGE_BUILT run_ref={payload['run_ref']['run_dir_ref']} hash={payload['lineage_canonical_sha256']}")


@runset_app.command("create")
def runset_create_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    spec_path: Path = typer.Option(..., "--spec"),
) -> None:
    payload = create_runset(catalog_root=catalog_dir, spec_path=spec_path)
    typer.echo(f"RUNSET_CREATED runset_id={payload['runset_id']}")


@runset_app.command("list")
def runset_list_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
) -> None:
    rows = list_runsets(catalog_root=catalog_dir)
    if not rows:
        typer.echo("RUNSETS 0")
        return
    typer.echo(f"RUNSETS {len(rows)}")
    for row in rows:
        typer.echo(f"{row['runset_id']} {row['created_utc']} {row['entry_path']}")


@runset_app.command("show")
def runset_show_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    runset_id: str = typer.Option(..., "--id"),
) -> None:
    payload = show_runset(catalog_root=catalog_dir, runset_id=runset_id)
    typer.echo(f"RUNSET {payload['runset_id']}")
    typer.echo(f"created_utc={payload['created_utc']}")
    if "name" in payload:
        typer.echo(f"name={payload['name']}")
    typer.echo(f"datasets={len(payload['datasets'])}")
    typer.echo(f"runs={len(payload['runs'])}")
    typer.echo(f"runset_entry_canonical_sha256={payload['runset_entry_canonical_sha256']}")


@runset_app.command("validate")
def runset_validate_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    runset_id: str = typer.Option(..., "--id"),
) -> None:
    ok, text = validate_runset(catalog_root=catalog_dir, runset_id=runset_id)
    typer.echo(text)
    if not ok:
        raise typer.Exit(code=1)


@runset_app.command("materialize")
def runset_materialize_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    runset_id: str = typer.Option(..., "--id"),
    runs_root: Path = typer.Option(..., "--runs-root"),
    project_out: Path = typer.Option(..., "--project-out"),
) -> None:
    result = materialize_runset(
        catalog_dir=catalog_dir,
        runset_id=runset_id,
        runs_root=runs_root,
        project_out=project_out,
    )
    typer.echo(f"RUNSET_MATERIALIZED runset_id={runset_id} out={result['output_dir']}")


@risk_app.command("run")
def risk_run_command(
    run_dir: Path = typer.Option(..., "--run"),
) -> None:
    result = write_risk_artifacts(run_dir=run_dir)
    typer.echo(f"RISK_RUN_COMPLETED run={run_dir}")
    typer.echo(f"summary={result['summary_path']}")
    typer.echo(f"manifest={result['manifest_path']}")


@risk_app.command("runset")
def risk_runset_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    runset_id: str = typer.Option(..., "--id"),
    out_dir: Path = typer.Option(..., "--out"),
) -> None:
    result = compute_runset_risk(catalog_dir=catalog_dir, runset_id=runset_id, out_dir=out_dir)
    typer.echo(f"RISK_RUNSET_COMPLETED runset_id={runset_id}")
    typer.echo(f"summary={result['summary_path']}")
    typer.echo(f"manifest={result['manifest_path']}")


@risk_app.command("sweep")
def risk_sweep_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    runset_id: str = typer.Option(..., "--runset"),
    out_dir: Path = typer.Option(..., "--out"),
) -> None:
    result = run_risk_sweep(catalog_dir=catalog_dir, runset_id=runset_id, out_dir=out_dir)
    typer.echo(f"RISK_SWEEP_COMPLETED runset_id={runset_id}")
    typer.echo(f"summary={result['summary_path']}")
    typer.echo(f"runset_manifest={result['runset_manifest_path']}")
    typer.echo(f"baseline_card={result['baseline_card_path']}")
    typer.echo(f"baseline_card_manifest={result['baseline_card_manifest_path']}")


@risk_app.command("diff")
def risk_diff_command(
    a_path: Path = typer.Option(..., "--a"),
    b_path: Path = typer.Option(..., "--b"),
    out_dir: Path = typer.Option(..., "--out"),
) -> None:
    result = write_baseline_diff_artifacts(a_path=a_path, b_path=b_path, out_dir=out_dir)
    typer.echo("RISK_DIFF_COMPLETED")
    typer.echo(f"diff={result['diff_path']}")
    typer.echo(f"manifest={result['manifest_path']}")


@risk_app.command("diff-runset")
def risk_diff_runset_command(
    baseline_root: Path = typer.Option(..., "--root"),
    a_runset_id: str = typer.Option(..., "--a"),
    b_runset_id: str = typer.Option(..., "--b"),
    label_a: str | None = typer.Option(None, "--label-a"),
    label_b: str | None = typer.Option(None, "--label-b"),
    out_dir: Path = typer.Option(..., "--out"),
) -> None:
    resolved_a = resolve_baseline(root=baseline_root, runset_id=a_runset_id, label=label_a)
    resolved_b = resolve_baseline(root=baseline_root, runset_id=b_runset_id, label=label_b)

    result = write_baseline_diff_artifacts(
        a_path=Path(resolved_a["card_path"]),
        b_path=Path(resolved_b["card_path"]),
        out_dir=out_dir,
    )
    typer.echo("RISK_DIFF_RUNSET_COMPLETED")
    typer.echo(f"a_baseline_id={resolved_a['baseline_id']}")
    typer.echo(f"b_baseline_id={resolved_b['baseline_id']}")
    typer.echo(f"diff={result['diff_path']}")
    typer.echo(f"manifest={result['manifest_path']}")


@risk_app.command("drift")
def risk_drift_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    baseline_root: Path = typer.Option(..., "--root"),
    runset_id: str = typer.Option(..., "--runset"),
    label: str = typer.Option("prod", "--label"),
    out_dir: Path = typer.Option(..., "--out"),
) -> None:
    result = run_risk_drift(
        catalog_dir=catalog_dir,
        baseline_root=baseline_root,
        runset_id=runset_id,
        label=label,
        out_dir=out_dir,
    )
    drift = result["drift"]
    typer.echo(f"RISK_DRIFT_COMPLETED runset_id={runset_id}")
    typer.echo(f"report={drift['report_path']}")
    typer.echo(f"manifest={drift['manifest_path']}")


@risk_app.command("dashboard")
def risk_dashboard_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    baseline_root: Path = typer.Option(..., "--root"),
    runsets_path: Path = typer.Option(..., "--runsets"),
    out_dir: Path = typer.Option(..., "--out"),
    label: str = typer.Option("prod", "--label"),
) -> None:
    result = run_risk_dashboard(
        catalog_dir=catalog_dir,
        baseline_root=baseline_root,
        runsets_path=runsets_path,
        out_dir=out_dir,
        label=label,
    )
    typer.echo(f"RISK_DASHBOARD_COMPLETED runsets={result['runset_count']}")
    typer.echo(f"summary={result['summary_path']}")
    typer.echo(f"manifest={result['manifest_path']}")


@ci_app.command("run")
def ci_run_command(
    config_path: Path = typer.Option(..., "--config"),
) -> None:
    result = run_ci_pipeline(config_path=config_path)
    typer.echo(f"CI_RUN_COMPLETED status={result['status']}")
    typer.echo(f"drift_count={result['drift_count']}")
    typer.echo(f"checksum_mismatch_count={result['checksum_mismatch_count']}")
    typer.echo(f"summary={result['summary_path']}")
    typer.echo(f"manifest={result['manifest_path']}")
    if result["should_fail"]:
        raise typer.Exit(code=1)


@ci_app.command("doctor")
def ci_doctor_command(
    config_path: Path = typer.Option(..., "--config"),
) -> None:
    result = run_ci_doctor(config_path=config_path)

    checks = result["checks"]
    ordered = [
        ("baseline_root_ok", checks.get("baseline_root_ok")),
        ("promotions_ok", checks.get("promotions_ok")),
        ("runsets_ok", checks.get("runsets_ok")),
        ("bundles_ok", checks.get("bundles_ok")),
        ("dashboard_ok", checks.get("dashboard_ok")),
    ]
    for key, value in ordered:
        if isinstance(value, bool):
            typer.echo(f"{key}={'PASS' if value else 'FAIL'}")
        else:
            typer.echo(f"{key}=N/A")

    typer.echo(f"failures={len(result['failures'])}")
    typer.echo(f"summary={result['summary_path']}")
    typer.echo(f"manifest={result['manifest_path']}")
    typer.echo(f"CI_DOCTOR_RESULT status={result['status']}")
    if result["status"] != "PASS":
        raise typer.Exit(code=1)


@release_app.command("notes")
def release_notes_command(
    from_ref: str = typer.Option(..., "--from"),
    to_ref: str = typer.Option(..., "--to"),
    output_format: str = typer.Option("markdown", "--format"),
) -> None:
    notes = generate_release_notes(
        repo_root=_repo_root(),
        from_ref=from_ref,
        to_ref=to_ref,
        output_format=output_format,
    )
    typer.echo(notes, nl=False)


@release_app.command("url")
def release_url_command(
    tag: str = typer.Option(..., "--tag"),
) -> None:
    url = build_new_release_url(repo_root=_repo_root(), tag=tag)
    typer.echo(url)


@release_app.command("draft")
def release_draft_command(
    from_ref: str = typer.Option(..., "--from"),
    to_ref: str = typer.Option(..., "--to"),
    out_path: Path = typer.Option(..., "--out"),
    title: str | None = typer.Option(None, "--title"),
) -> None:
    path = write_release_draft(
        repo_root=_repo_root(),
        from_ref=from_ref,
        to_ref=to_ref,
        out_path=out_path,
        title=title,
    )
    typer.echo(path.as_posix())


def _run_prune(*, mode: str, root: Path, policy_path: Path, dry_run: bool, confirm: str | None) -> None:
    policy = load_prune_policy(policy_path)
    plan = build_prune_plan(mode=mode, root=root, policy=policy)

    if not dry_run and policy["safety"]["require_dry_run_first"]:
        if not isinstance(confirm, str) or not confirm:
            raise ResearchError("prune execute requires --confirm <plan_sha256> when policy.safety.require_dry_run_first=true")
        if confirm != plan["plan_sha256"]:
            raise ResearchError("prune execute confirm hash mismatch")

    if dry_run:
        typer.echo(format_prune_report(plan=plan, result="DRY_RUN"), nl=False)
        return

    execute_prune_plan(plan=plan)
    typer.echo(format_prune_report(plan=plan, result="EXECUTED"), nl=False)


@prune_app.command("run")
def prune_run_command(
    run_dir: Path = typer.Option(..., "--run"),
    policy_path: Path = typer.Option(..., "--policy"),
    dry_run: bool = typer.Option(False, "--dry-run"),
    confirm: str | None = typer.Option(None, "--confirm"),
) -> None:
    _run_prune(mode="run", root=run_dir, policy_path=policy_path, dry_run=dry_run, confirm=confirm)


@prune_app.command("out")
def prune_out_command(
    root_dir: Path = typer.Option(..., "--root"),
    policy_path: Path = typer.Option(..., "--policy"),
    dry_run: bool = typer.Option(False, "--dry-run"),
    confirm: str | None = typer.Option(None, "--confirm"),
) -> None:
    _run_prune(mode="out", root=root_dir, policy_path=policy_path, dry_run=dry_run, confirm=confirm)


@baseline_index_app.command("refresh")
def baseline_index_refresh_command(
    baseline_root: Path = typer.Option(..., "--root"),
) -> None:
    payload = refresh_baseline_index(root=baseline_root)
    typer.echo(f"BASELINE_INDEX_REFRESHED runsets={len(payload['runsets'])}")


@baseline_index_app.command("show")
def baseline_index_show_command(
    baseline_root: Path = typer.Option(..., "--root"),
    runset_id: str | None = typer.Option(None, "--runset"),
) -> None:
    payload = show_baseline_index(root=baseline_root, runset_id=runset_id)
    typer.echo(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


@baseline_app.command("promote")
def baseline_promote_command(
    baseline_root: Path = typer.Option(..., "--root"),
    runset_id: str = typer.Option(..., "--runset"),
    baseline_id: str = typer.Option(..., "--baseline-id"),
    label: str = typer.Option(..., "--label"),
) -> None:
    payload = promote_baseline(root=baseline_root, runset_id=runset_id, baseline_id=baseline_id, label=label)
    typer.echo(f"BASELINE_PROMOTED labels={len(payload['labels'])}")


@baseline_app.command("resolve")
def baseline_resolve_command(
    baseline_root: Path = typer.Option(..., "--root"),
    runset_id: str = typer.Option(..., "--runset"),
    label: str | None = typer.Option(None, "--label"),
) -> None:
    resolved = resolve_baseline(root=baseline_root, runset_id=runset_id, label=label)
    typer.echo(f"baseline_path={resolved['card_path']}")
    typer.echo(f"baseline_id={resolved['baseline_id']}")
    if "label" in resolved:
        typer.echo(f"label={resolved['label']}")


@dataset_app.command("list")
def dataset_list_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
) -> None:
    rows = list_datasets(catalog_root=catalog_dir)
    if not rows:
        typer.echo("DATASETS 0")
        return
    typer.echo(f"DATASETS {len(rows)}")
    for row in rows:
        typer.echo(f"{row['dataset_id']} {row['kind']} {row['created_utc']} {row['entry_path']}")


@dataset_app.command("show")
def dataset_show_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    dataset_id: str = typer.Option(..., "--id"),
) -> None:
    payload = show_dataset(catalog_root=catalog_dir, dataset_id=dataset_id)
    source = payload["source"]
    fingerprint = payload["fingerprint"]
    typer.echo(f"DATASET {payload['dataset_id']}")
    typer.echo(f"kind={payload['kind']}")
    typer.echo(f"created_utc={payload['created_utc']}")
    if "tz" in payload:
        typer.echo(f"tz={payload['tz']}")
    typer.echo(f"root={source['root']}")
    typer.echo(f"file_count={source['file_count']}")
    typer.echo(f"total_bytes={source['total_bytes']}")
    typer.echo(f"files_sha256={fingerprint['files_sha256']}")
    if "canon_table_sha256" in fingerprint:
        typer.echo(f"canon_table_sha256={fingerprint['canon_table_sha256']}")
    typer.echo(f"dataset_entry_canonical_sha256={payload['dataset_entry_canonical_sha256']}")


@dataset_app.command("validate")
def dataset_validate_command(
    catalog_dir: Path = typer.Option(..., "--catalog"),
    dataset_id: str = typer.Option(..., "--id"),
) -> None:
    ok, text = validate_dataset(catalog_root=catalog_dir, dataset_id=dataset_id)
    typer.echo(text)
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
