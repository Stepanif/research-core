from __future__ import annotations

import os
import subprocess
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from research_core.plan.contracts import PLAN_TASK_KIND_EXPERIMENT_BATCH, PLAN_VERSION, REQUIRED_ENV_VAR_CREATED_UTC
from research_core.plan.io import read_plan_json
from research_core.plan.logs import write_task_logs
from research_core.util.types import ValidationError


@dataclass
class TaskResult:
    task_id: str
    status: str
    exit_code: int


@dataclass
class PreflightResult:
    task_id: str
    status: str


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _require_created_utc() -> str:
    created_utc = os.environ.get(REQUIRED_ENV_VAR_CREATED_UTC)
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Plan execute requires RESEARCH_CREATED_UTC for deterministic execution")
    return created_utc


def _require_string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"Invalid or missing plan field: {key}")
    return value


def _require_list(payload: dict[str, Any], key: str) -> list[Any]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise ValidationError(f"Invalid or missing plan list field: {key}")
    return value


def _parse_run_from_argv(argv: list[str]) -> Path:
    if "--run" not in argv:
        raise ValidationError("Task argv missing --run")
    run_idx = argv.index("--run")
    if run_idx + 1 >= len(argv):
        raise ValidationError("Task argv missing value for --run")
    return Path(argv[run_idx + 1])


def _parse_out_from_argv(argv: list[str]) -> Path:
    if "--out" not in argv:
        raise ValidationError("Task argv missing --out")
    out_idx = argv.index("--out")
    if out_idx + 1 >= len(argv):
        raise ValidationError("Task argv missing value for --out")
    return Path(argv[out_idx + 1])


def _resolve_task_path(value: str, plan_dir: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (plan_dir / path).resolve()


def _task_run_dir(task: dict[str, Any], plan_dir: Path) -> Path:
    run_dir_value = _require_string(task, "run_dir")
    return _resolve_task_path(run_dir_value, plan_dir)


def _task_out_dir(task: dict[str, Any], plan_dir: Path) -> Path:
    out_dir_value = _require_string(task, "out_dir")
    return _resolve_task_path(out_dir_value, plan_dir)


def _expected_output_missing(task: dict[str, Any], plan_dir: Path) -> list[str]:
    run_dir = _task_run_dir(task, plan_dir)
    expected_outputs = [str(item) for item in _require_list(task, "expected_outputs")]
    return [
        rel_path
        for rel_path in sorted(expected_outputs)
        if not (run_dir / rel_path).exists()
    ]


def _preflight(tasks: list[dict[str, Any]], plan_dir: Path) -> list[PreflightResult]:
    results: list[PreflightResult] = []
    for task in tasks:
        task_id = _require_string(task, "task_id")
        out_dir = _task_out_dir(task, plan_dir)
        if not out_dir.exists():
            results.append(PreflightResult(task_id=task_id, status="READY"))
            continue

        missing = _expected_output_missing(task, plan_dir)
        if missing:
            results.append(PreflightResult(task_id=task_id, status="EXISTS_INCOMPLETE"))
        else:
            results.append(PreflightResult(task_id=task_id, status="EXISTS_COMPLETE"))
    return results


def _execute_task(task: dict[str, Any], repo_root: Path, logs_dir: Path, env: dict[str, str], plan_dir: Path) -> TaskResult:
    task_id = _require_string(task, "task_id")
    argv_raw = _require_list(task, "argv")
    argv = [str(item) for item in argv_raw]

    process = subprocess.run(
        argv,
        cwd=str(repo_root),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    status = "RUN_OK" if process.returncode == 0 else "RUN_FAIL"
    exit_code = int(process.returncode)

    if status == "RUN_OK":
        missing = _expected_output_missing(task, plan_dir)
        if missing:
            status = "RUN_FAIL"
            exit_code = 101
            stderr_text = process.stderr + ("\n" if process.stderr and not process.stderr.endswith("\n") else "")
            process_stderr = stderr_text + f"Missing expected outputs: {missing}\n"
            write_task_logs(logs_dir=logs_dir, task_id=task_id, stdout_text=process.stdout, stderr_text=process_stderr)
            return TaskResult(task_id=task_id, status=status, exit_code=exit_code)

    write_task_logs(logs_dir=logs_dir, task_id=task_id, stdout_text=process.stdout, stderr_text=process.stderr)
    return TaskResult(task_id=task_id, status=status, exit_code=exit_code)


def _validate_plan(payload: dict[str, Any], created_utc: str) -> list[dict[str, Any]]:
    plan_version = _require_string(payload, "plan_version")
    if plan_version != PLAN_VERSION:
        raise ValidationError(f"Unsupported plan_version: {plan_version}")

    plan_created_utc = _require_string(payload, "created_utc")
    if plan_created_utc != created_utc:
        raise ValidationError(
            f"RESEARCH_CREATED_UTC mismatch for plan execute: env={created_utc} plan={plan_created_utc}"
        )

    _require_string(payload, "project_id")
    tasks = _require_list(payload, "tasks")

    validated: list[dict[str, Any]] = []
    for item in tasks:
        if not isinstance(item, dict):
            raise ValidationError("Invalid task entry in plan (must be object)")
        kind = _require_string(item, "kind")
        if kind != PLAN_TASK_KIND_EXPERIMENT_BATCH:
            raise ValidationError(f"Unsupported task kind in plan v1: {kind}")

        _require_string(item, "task_id")
        _require_string(item, "run_dir")
        _require_string(item, "spec_dir")
        _require_string(item, "out_dir")
        deps = _require_list(item, "deps")
        if deps:
            raise ValidationError("Plan v1 requires empty deps for all tasks")
        _require_list(item, "argv")
        _require_list(item, "expected_outputs")
        validated.append(item)

    return validated


def execute_plan(plan_path: Path, jobs: int, allow_existing: bool = False) -> tuple[list[str], bool]:
    if jobs < 1:
        raise ValidationError("plan execute --jobs must be >= 1")
    if not plan_path.exists() or not plan_path.is_file():
        raise ValidationError(f"Plan file does not exist: {plan_path}")

    created_utc = _require_created_utc()
    payload = read_plan_json(plan_path)
    if not isinstance(payload, dict):
        raise ValidationError("Invalid plan payload (must be object)")

    tasks = _validate_plan(payload, created_utc=created_utc)
    task_ids = [str(task["task_id"]) for task in tasks]
    if len(task_ids) != len(set(task_ids)):
        raise ValidationError("Plan contains duplicate task_id entries")

    plan_dir = plan_path.parent
    logs_dir = plan_dir / "logs"
    repo_root = _repo_root()

    env = dict(os.environ)
    env[REQUIRED_ENV_VAR_CREATED_UTC] = created_utc

    preflight_results = _preflight(tasks=tasks, plan_dir=plan_dir)
    preflight_lines = [f"preflight,{item.task_id},{item.status}" for item in preflight_results]

    has_incomplete = any(item.status == "EXISTS_INCOMPLETE" for item in preflight_results)
    has_existing_complete = any(item.status == "EXISTS_COMPLETE" for item in preflight_results)

    if has_incomplete:
        return preflight_lines, False

    if not allow_existing and has_existing_complete:
        return preflight_lines, False

    preflight_map = {item.task_id: item.status for item in preflight_results}
    task_order = list(tasks)

    remaining = [
        task
        for task in task_order
        if not (allow_existing and preflight_map.get(str(task["task_id"])) == "EXISTS_COMPLETE")
    ]

    results: dict[str, TaskResult] = {}
    running: dict[Future[TaskResult], dict[str, Any]] = {}
    failure_detected = False

    if allow_existing:
        for task in task_order:
            task_id = str(task["task_id"])
            if preflight_map.get(task_id) == "EXISTS_COMPLETE":
                results[task_id] = TaskResult(task_id=task_id, status="SKIP_EXISTS", exit_code=0)

    with ThreadPoolExecutor(max_workers=jobs) as pool:
        while remaining and not failure_detected and len(running) < jobs:
            task = remaining.pop(0)
            future = pool.submit(_execute_task, task, repo_root, logs_dir, env, plan_dir)
            running[future] = task

        while running:
            done, _ = wait(set(running.keys()), return_when=FIRST_COMPLETED)
            for future in done:
                task = running.pop(future)
                result = future.result()
                results[result.task_id] = result
                if result.status != "RUN_OK":
                    failure_detected = True

            while remaining and not failure_detected and len(running) < jobs:
                task = remaining.pop(0)
                future = pool.submit(_execute_task, task, repo_root, logs_dir, env, plan_dir)
                running[future] = task

    for task in remaining:
        task_id = str(task["task_id"])
        results[task_id] = TaskResult(task_id=task_id, status="RUN_FAIL", exit_code=-1)

    summary_lines = preflight_lines + [
        f"{task_id},{results[task_id].status},{results[task_id].exit_code}"
        for task_id in sorted(str(task["task_id"]) for task in task_order)
    ]
    all_ok = all(
        results[task_id].status in {"RUN_OK", "SKIP_EXISTS"}
        for task_id in sorted(str(task["task_id"]) for task in task_order)
    )
    return summary_lines, all_ok
