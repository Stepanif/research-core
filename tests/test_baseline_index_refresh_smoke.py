from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, sweep_to_baseline_root
from research_core.cli import app


def test_baseline_index_refresh_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)

    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-baseline-index-smoke")
    baseline_root = tmp_path / "baselines"
    _card_path, baseline_id = sweep_to_baseline_root(runner, tmp_path, runset_id, baseline_root)

    refresh_1 = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh_1.exit_code == 0, refresh_1.stdout

    index_path = baseline_root / "baseline.index.json"
    assert index_path.exists()
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    assert payload["index_version"] == "v1"
    assert payload["runsets"][runset_id]["baseline_id"] == baseline_id
    assert payload["runsets"][runset_id]["path"] == f"{runset_id}/baseline.card.json"

    first_bytes = index_path.read_bytes()
    refresh_2 = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh_2.exit_code == 0, refresh_2.stdout
    assert index_path.read_bytes() == first_bytes
