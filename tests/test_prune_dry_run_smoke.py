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
            "ci_outputs": {"keep_latest_n": 5},
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


def test_prune_dry_run_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    run_dir = tmp_path / "run"
    (run_dir / "experiments" / "batches" / "batch-a" / "tmp.bin").parent.mkdir(parents=True, exist_ok=True)
    (run_dir / "experiments" / "batches" / "batch-a" / "tmp.bin").write_bytes(b"abc")
    (run_dir / "observe").mkdir(parents=True, exist_ok=True)
    (run_dir / "observe" / "artifact.json").write_text("{}\n", encoding="utf-8")
    (run_dir / "observe" / "keep.manifest.json").write_text("{}\n", encoding="utf-8")
    (run_dir / "risk").mkdir(parents=True, exist_ok=True)
    (run_dir / "risk" / "risk.tmp").write_text("x\n", encoding="utf-8")
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)
    for index in range(5):
        (run_dir / "logs" / f"run{index}.log").write_text(f"{index}\n", encoding="utf-8")

    policy_path = tmp_path / "policy.json"
    _write_policy(policy_path)

    runner = CliRunner()
    one = runner.invoke(app, ["prune", "run", "--run", str(run_dir), "--policy", str(policy_path), "--dry-run"])
    two = runner.invoke(app, ["prune", "run", "--run", str(run_dir), "--policy", str(policy_path), "--dry-run"])

    assert one.exit_code == 0, one.stdout
    assert two.exit_code == 0, two.stdout
    assert one.stdout == two.stdout
    assert "PRUNE v1" in one.stdout
    assert "RESULT: DRY_RUN" in one.stdout
