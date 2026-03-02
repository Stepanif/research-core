from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import pandas as pd
import typer

from research_core.canon.manifest import build_manifest, write_contract_snapshot, write_manifest
from research_core.canon.normalize import canonicalize_file
from research_core.canon.writer import write_canon_parquet
from research_core.psa.contracts import load_psa_schema_contract
from research_core.psa.engine import run_psa_v1
from research_core.psa.writer import build_psa_manifest, write_psa_log, write_psa_manifest, write_psa_parquet
from research_core.registry.dataset_registry import build_dataset_registry
from research_core.registry.run_index import build_run_index
from research_core.util.hashing import sha256_bytes
from research_core.util.io import ensure_dir
from research_core.util.types import ResearchError
from research_core.validate.canon_checks import validate_canon_file

app = typer.Typer(no_args_is_help=True)
validate_app = typer.Typer(no_args_is_help=True)
registry_app = typer.Typer(no_args_is_help=True)
app.add_typer(validate_app, name="validate")
app.add_typer(registry_app, name="registry")


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


def main() -> None:
    app()


if __name__ == "__main__":
    main()
