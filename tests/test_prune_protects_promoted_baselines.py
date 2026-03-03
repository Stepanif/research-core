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


def test_prune_protects_promoted_baselines(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)

    root = tmp_path / "exec_outputs"
    baseline_root = root / "baseline_root"
    runset_id = "runset-a"
    baseline_id = "abc123"

    (baseline_root / runset_id).mkdir(parents=True, exist_ok=True)
    (baseline_root / "baseline.index.json").write_text('{"index_version":"v1","created_utc":"x","runsets":{}}\n', encoding="utf-8")
    (baseline_root / "baseline.promotions.json").write_text(
        json.dumps(
            {
                "promotions_version": "v1",
                "created_utc": "x",
                "labels": {"prod": {runset_id: baseline_id}},
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    (baseline_root / runset_id / "baseline.card.json").write_text(
        json.dumps(
            {
                "card_version": "v1",
                "checksums": {"per_run_vector_sha256": baseline_id},
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    (baseline_root / runset_id / "baseline.card.manifest.json").write_text("{}\n", encoding="utf-8")

    run_dir = root / "run-1"
    (run_dir / "risk").mkdir(parents=True, exist_ok=True)
    (run_dir / "risk" / "tmp.bin").write_bytes(b"x")

    policy_path = tmp_path / "policy.json"
    _write_policy(policy_path)

    runner = CliRunner()
    result = runner.invoke(app, ["prune", "out", "--root", str(root), "--policy", str(policy_path), "--dry-run"])
    assert result.exit_code == 0, result.stdout
    assert "baseline_root/runset-a/baseline.card.json" not in result.stdout
    assert "run-1/risk/tmp.bin" in result.stdout
