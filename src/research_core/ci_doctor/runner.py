from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.ci_doctor.checks import run_ci_doctor_checks
from research_core.ci_doctor.config import load_ci_doctor_config
from research_core.ci_doctor.io import read_runset_ids
from research_core.ci_doctor.writer import write_ci_doctor_artifacts
from research_core.util.buildmeta import get_created_utc


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="ci doctor requires RESEARCH_CREATED_UTC")


def run_ci_doctor(*, config_path: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    config = load_ci_doctor_config(config_path)
    runset_ids = read_runset_ids(config["runsets_path"])

    checks_result = run_ci_doctor_checks(config=config, runset_ids=runset_ids)
    status = checks_result["status"]

    artifacts = write_ci_doctor_artifacts(
        created_utc=created_utc,
        config_path=config_path,
        runsets_path=config["runsets_path"],
        out_dir=config["out_dir"],
        label=config["label"],
        runset_count=len(runset_ids),
        checks=checks_result["checks"],
        status=status,
        failures=checks_result["failures"],
        catalog_dir=config["catalog_dir"],
        baseline_root=config["baseline_root"],
        input_paths=checks_result["inputs"],
    )

    return {
        "status": status,
        "summary_path": artifacts["summary_path"],
        "manifest_path": artifacts["manifest_path"],
        "checks": checks_result["checks"],
        "failures": checks_result["failures"],
    }
