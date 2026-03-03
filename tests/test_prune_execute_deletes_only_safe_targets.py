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


def _extract_plan_hash(output: str) -> str:
    for line in output.splitlines():
        if line.startswith("- plan_sha256: "):
            return line.split(": ", 1)[1].strip()
    raise AssertionError("missing plan hash in prune output")


def test_prune_execute_deletes_only_safe_targets(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)

    run_dir = tmp_path / "run"
    (run_dir / "observe").mkdir(parents=True, exist_ok=True)
    (run_dir / "observe" / "artifact.bin").write_bytes(b"abc")
    (run_dir / "observe" / "keep.manifest.json").write_text("{}\n", encoding="utf-8")
    (run_dir / "risk").mkdir(parents=True, exist_ok=True)
    (run_dir / "risk" / "risk.bin").write_bytes(b"x")

    policy_path = tmp_path / "policy.json"
    _write_policy(policy_path)

    runner = CliRunner()
    dry = runner.invoke(app, ["prune", "run", "--run", str(run_dir), "--policy", str(policy_path), "--dry-run"])
    assert dry.exit_code == 0, dry.stdout
    plan_hash = _extract_plan_hash(dry.stdout)

    exe = runner.invoke(
        app,
        ["prune", "run", "--run", str(run_dir), "--policy", str(policy_path), "--confirm", plan_hash],
    )
    assert exe.exit_code == 0, exe.stdout
    assert "RESULT: EXECUTED" in exe.stdout

    assert not (run_dir / "observe" / "artifact.bin").exists()
    assert not (run_dir / "risk" / "risk.bin").exists()
    assert (run_dir / "observe" / "keep.manifest.json").exists()
