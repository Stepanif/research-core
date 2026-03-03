from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from research_core.prune.contracts import PRUNE_OUTPUT_VERSION
from research_core.prune.guards import collect_protected_paths
from research_core.util.types import ValidationError


def _candidate_paths_for_run(root: Path, policy: dict[str, Any]) -> list[Path]:
    candidates: list[Path] = []
    delete = policy["delete"]

    if delete["run_intermediates"]:
        targets = [
            root / "experiments" / "batches",
            root / "observe",
            root / "risk",
        ]
        for target in targets:
            if not target.exists() or not target.is_dir():
                continue
            for path in sorted([p for p in target.rglob("*") if p.is_file()], key=lambda p: p.as_posix()):
                candidates.append(path)

    keep_latest_n = delete["plan_logs"]["keep_latest_n"]
    log_files = sorted([p for p in root.rglob("logs/*.log") if p.is_file()], key=lambda p: p.as_posix())
    if len(log_files) > keep_latest_n:
        candidates.extend(log_files[: len(log_files) - keep_latest_n])

    return sorted(set(path.resolve() for path in candidates), key=lambda p: p.as_posix())


def _candidate_paths_for_out(root: Path, policy: dict[str, Any]) -> list[Path]:
    candidates: list[Path] = []
    delete = policy["delete"]

    if delete["run_intermediates"]:
        for target in sorted(root.rglob("experiments/batches"), key=lambda p: p.as_posix()):
            if target.is_dir():
                candidates.extend(sorted([p for p in target.rglob("*") if p.is_file()], key=lambda p: p.as_posix()))
        for name in ["observe", "risk"]:
            for target in sorted(root.rglob(name), key=lambda p: p.as_posix()):
                if target.is_dir():
                    candidates.extend(sorted([p for p in target.rglob("*") if p.is_file()], key=lambda p: p.as_posix()))

    keep_latest_n = delete["plan_logs"]["keep_latest_n"]
    log_files = sorted([p for p in root.rglob("logs/*.log") if p.is_file()], key=lambda p: p.as_posix())
    if len(log_files) > keep_latest_n:
        candidates.extend(log_files[: len(log_files) - keep_latest_n])

    keep_ci = policy["keep"]["ci_outputs"]
    if isinstance(keep_ci, dict):
        keep_n = keep_ci["keep_latest_n"]
        ci_summary_paths = sorted([p for p in root.rglob("ci.summary.json") if p.is_file()], key=lambda p: p.as_posix())
        if len(ci_summary_paths) > keep_n:
            stale = ci_summary_paths[: len(ci_summary_paths) - keep_n]
            for summary_path in stale:
                candidates.append(summary_path)
                manifest_path = summary_path.with_name("ci.summary.manifest.json")
                if manifest_path.exists() and manifest_path.is_file():
                    candidates.append(manifest_path)

    return sorted(set(path.resolve() for path in candidates), key=lambda p: p.as_posix())


def build_prune_plan(*, mode: str, root: Path, policy: dict[str, Any]) -> dict[str, Any]:
    if mode not in {"run", "out"}:
        raise ValidationError(f"Unsupported prune mode: {mode}")
    if not root.exists() or not root.is_dir():
        raise ValidationError(f"Prune root does not exist: {root}")

    protected_paths = collect_protected_paths(root=root, policy=policy)
    raw_candidates = _candidate_paths_for_run(root, policy) if mode == "run" else _candidate_paths_for_out(root, policy)

    safe_candidates: list[dict[str, Any]] = []
    for path in raw_candidates:
        if path.resolve() in protected_paths:
            continue
        if not path.exists() or not path.is_file():
            continue
        safe_candidates.append(
            {
                "path": path.resolve(),
                "relative_path": path.resolve().relative_to(root.resolve()).as_posix(),
                "bytes": int(path.stat().st_size),
            }
        )

    safe_candidates = sorted(safe_candidates, key=lambda item: str(item["relative_path"]))

    if policy["safety"]["refuse_if_unrecognized_paths"]:
        for item in safe_candidates:
            rel = str(item["relative_path"])
            if rel.endswith(".manifest.json"):
                raise ValidationError(f"Unsafe candidate includes manifest file: {rel}")

    plan_payload = {
        "version": PRUNE_OUTPUT_VERSION,
        "mode": mode,
        "root": root.resolve().as_posix(),
        "policy": {
            "keep": policy["keep"],
            "delete": policy["delete"],
            "safety": policy["safety"],
        },
        "protected_count": len(protected_paths),
        "delete_candidates": [{"path": item["relative_path"], "bytes": item["bytes"]} for item in safe_candidates],
    }
    plan_sha256 = hashlib.sha256(
        json.dumps(plan_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()

    return {
        "version": PRUNE_OUTPUT_VERSION,
        "mode": mode,
        "root": root.resolve(),
        "policy": policy,
        "protected_count": len(protected_paths),
        "delete_candidates": safe_candidates,
        "total_candidates": len(safe_candidates),
        "total_bytes": sum(int(item["bytes"]) for item in safe_candidates),
        "plan_sha256": plan_sha256,
    }
