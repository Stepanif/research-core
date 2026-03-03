from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def _write_policy(path: Path) -> None:
    payload = {
        "policy_version": "v1",
        "keep": {
            "manifests": True,
            "contracts": True,
            "goldens": True,
            "baselines": {"promoted_only": True, "keep_index": True},
        },
        "delete": {
            "run_intermediates": True,
            "plan_logs": {"keep_latest_n": 3},
        },
        "safety": {
            "require_dry_run_first": True,
            "refuse_if_unrecognized_paths": True,
        },
    }
    path.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")


def test_prune_refuses_without_confirm(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    run_dir = tmp_path / "run"
    (run_dir / "risk").mkdir(parents=True, exist_ok=True)
    (run_dir / "risk" / "to_delete.bin").write_bytes(b"x")

    policy_path = tmp_path / "policy.json"
    _write_policy(policy_path)

    runner = CliRunner()
    result = runner.invoke(app, ["prune", "run", "--run", str(run_dir), "--policy", str(policy_path)])
    assert result.exit_code != 0
