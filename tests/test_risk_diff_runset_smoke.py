from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, sweep_to_baseline_root
from research_core.cli import app


def test_risk_diff_runset_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)

    runset_a = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-risk-diff-runset-a")
    runset_b = create_runset(
        runner,
        tmp_path,
        dataset_id,
        canon_hash,
        "runset-risk-diff-runset-b",
        allow_materialize_missing=True,
    )

    baseline_root = tmp_path / "baselines"
    card_a, _baseline_id_a = sweep_to_baseline_root(runner, tmp_path, runset_a, baseline_root)
    card_b, _baseline_id_b = sweep_to_baseline_root(runner, tmp_path, runset_b, baseline_root)

    refresh = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh.exit_code == 0, refresh.stdout

    direct = runner.invoke(
        app,
        ["risk", "diff", "--a", str(card_a), "--b", str(card_b), "--out", str(tmp_path / "diff_direct")],
    )
    assert direct.exit_code == 0, direct.stdout

    via_runset = runner.invoke(
        app,
        [
            "risk",
            "diff-runset",
            "--root",
            str(baseline_root),
            "--a",
            runset_a,
            "--b",
            runset_b,
            "--out",
            str(tmp_path / "diff_runset"),
        ],
    )
    assert via_runset.exit_code == 0, via_runset.stdout

    direct_diff = (tmp_path / "diff_direct" / "baseline.diff.json").read_bytes()
    direct_manifest = (tmp_path / "diff_direct" / "baseline.diff.manifest.json").read_bytes()
    runset_diff = (tmp_path / "diff_runset" / "baseline.diff.json").read_bytes()
    runset_manifest = (tmp_path / "diff_runset" / "baseline.diff.manifest.json").read_bytes()

    assert runset_diff == direct_diff
    assert runset_manifest == direct_manifest
