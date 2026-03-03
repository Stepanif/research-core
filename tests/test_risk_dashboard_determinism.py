from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset_at, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def _manifest_canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    data = {key: value for key, value in payload.items() if key != "dashboard_manifest_canonical_sha256"}
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def test_risk_dashboard_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_a, _run_dir_a, canon_hash_a = build_small_run_with_dataset_at(
        runner,
        tmp_path,
        run_dir_name="run_a",
        raw_root_name="raw_a",
    )
    dataset_b, _run_dir_b, canon_hash_b = build_small_run_with_dataset_at(
        runner,
        tmp_path,
        run_dir_name="run_b",
        raw_dataset_id=dataset_a,
        instrument="NQ",
    )
    runset_a = create_runset(runner, tmp_path, dataset_a, canon_hash_a, "runset-dashboard-det-a", run_ref="run_a")
    runset_b = create_runset(runner, tmp_path, dataset_b, canon_hash_b, "runset-dashboard-det-b", run_ref="run_b")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_a, baseline_root, label="prod")
    prepare_promoted_baseline_root(runner, tmp_path, runset_b, baseline_root, label="prod")

    runsets_path = tmp_path / "runsets.json"
    runsets_path.write_text(
        json.dumps({"runset_ids": [runset_a, runset_b]}, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    one = runner.invoke(
        app,
        [
            "risk",
            "dashboard",
            "--catalog",
            "catalog",
            "--root",
            "baselines",
            "--runsets",
            str(runsets_path),
            "--out",
            "dashboard_out_1",
        ],
    )
    assert one.exit_code == 0, one.stdout

    two = runner.invoke(
        app,
        [
            "risk",
            "dashboard",
            "--catalog",
            "catalog",
            "--root",
            "baselines",
            "--runsets",
            str(runsets_path),
            "--out",
            "dashboard_out_2",
        ],
    )
    assert two.exit_code == 0, two.stdout

    summary_1 = tmp_path / "dashboard_out_1" / "dashboard.summary.json"
    summary_2 = tmp_path / "dashboard_out_2" / "dashboard.summary.json"
    manifest_1 = tmp_path / "dashboard_out_1" / "dashboard.summary.manifest.json"
    manifest_2 = tmp_path / "dashboard_out_2" / "dashboard.summary.manifest.json"

    assert hashlib.sha256(summary_1.read_bytes()).hexdigest() == hashlib.sha256(summary_2.read_bytes()).hexdigest()
    assert _manifest_canonical_hash(manifest_1) == _manifest_canonical_hash(manifest_2)
