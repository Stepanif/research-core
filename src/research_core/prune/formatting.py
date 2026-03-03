from __future__ import annotations

from pathlib import Path
from typing import Any


def format_prune_report(*, plan: dict[str, Any], result: str) -> str:
    policy = plan["policy"]
    lines: list[str] = []
    root_path = plan["root"]
    root_display = root_path.as_posix()
    try:
        root_display = root_path.resolve().relative_to(Path.cwd().resolve()).as_posix() or "."
    except Exception:  # noqa: BLE001
        root_display = root_path.as_posix()

    lines.append("PRUNE v1")
    lines.append("INPUT")
    lines.append(f"- mode: {plan['mode']}")
    lines.append(f"- root: {root_display}")
    lines.append("POLICY SUMMARY")
    lines.append(f"- keep.manifests: {policy['keep']['manifests']}")
    lines.append(f"- keep.contracts: {policy['keep']['contracts']}")
    lines.append(f"- keep.goldens: {policy['keep']['goldens']}")
    lines.append(f"- delete.run_intermediates: {policy['delete']['run_intermediates']}")
    lines.append(f"- delete.plan_logs.keep_latest_n: {policy['delete']['plan_logs']['keep_latest_n']}")
    lines.append(f"- safety.require_dry_run_first: {policy['safety']['require_dry_run_first']}")
    lines.append(f"- safety.refuse_if_unrecognized_paths: {policy['safety']['refuse_if_unrecognized_paths']}")
    lines.append(f"PROTECTED PATHS (count={plan['protected_count']})")
    lines.append("DELETE CANDIDATES")
    for item in plan["delete_candidates"]:
        lines.append(f"- {item['relative_path']} | bytes={item['bytes']}")
    if not plan["delete_candidates"]:
        lines.append("- (none)")
    lines.append("TOTALS")
    lines.append(f"- candidates: {plan['total_candidates']}")
    lines.append(f"- bytes: {plan['total_bytes']}")
    lines.append(f"- plan_sha256: {plan['plan_sha256']}")
    lines.append(f"RESULT: {result}")
    return "\n".join(lines) + "\n"
