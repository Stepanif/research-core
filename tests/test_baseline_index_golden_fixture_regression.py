from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, sweep_to_baseline_root
from research_core.cli import app


def _canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def test_baseline_index_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)

    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-baseline-index-golden")
    baseline_root = tmp_path / "baselines"
    _card_path, baseline_id = sweep_to_baseline_root(runner, tmp_path, runset_id, baseline_root)

    refresh = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh.exit_code == 0, refresh.stdout

    promote = runner.invoke(
        app,
        [
            "baseline",
            "promote",
            "--root",
            str(baseline_root),
            "--runset",
            runset_id,
            "--baseline-id",
            baseline_id,
            "--label",
            "prod",
        ],
    )
    assert promote.exit_code == 0, promote.stdout

    index_hash = _canonical_hash(baseline_root / "baseline.index.json")
    promotions_hash = _canonical_hash(baseline_root / "baseline.promotions.json")

    expected_index_hash = (repo_root / "tests" / "golden" / "baseline_index_small_sample_v1.json.sha256").read_text(encoding="utf-8").strip()
    expected_promotions_hash = (
        repo_root / "tests" / "golden" / "baseline_promotions_small_sample_v1.json.sha256"
    ).read_text(encoding="utf-8").strip()

    assert index_hash == expected_index_hash
    assert promotions_hash == expected_promotions_hash
