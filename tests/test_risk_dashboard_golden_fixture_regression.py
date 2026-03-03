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


def test_risk_dashboard_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent

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
    runset_a = create_runset(runner, tmp_path, dataset_a, canon_hash_a, "runset-dashboard-golden-a", run_ref="run_a")
    runset_b = create_runset(runner, tmp_path, dataset_b, canon_hash_b, "runset-dashboard-golden-b", run_ref="run_b")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_a, baseline_root, label="prod")
    prepare_promoted_baseline_root(runner, tmp_path, runset_b, baseline_root, label="prod")

    runsets_path = tmp_path / "runsets.json"
    runsets_path.write_text(
        json.dumps({"runset_ids": [runset_b, runset_a]}, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    result = runner.invoke(
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
            "dashboard_out",
        ],
    )
    assert result.exit_code == 0, result.stdout

    summary_path = tmp_path / "dashboard_out" / "dashboard.summary.json"
    manifest_path = tmp_path / "dashboard_out" / "dashboard.summary.manifest.json"
    summary_hash = hashlib.sha256(summary_path.read_bytes()).hexdigest()
    manifest_hash = _manifest_canonical_hash(manifest_path)

    expected_summary_hash = (
        repo_root / "tests" / "golden" / "dashboard_small_sample_v1.summary.json.sha256"
    ).read_text(encoding="utf-8").strip()
    expected_manifest_hash = (
        repo_root / "tests" / "golden" / "dashboard_small_sample_v1.manifest.json.sha256"
    ).read_text(encoding="utf-8").strip()

    assert summary_hash == expected_summary_hash
    assert manifest_hash == expected_manifest_hash
