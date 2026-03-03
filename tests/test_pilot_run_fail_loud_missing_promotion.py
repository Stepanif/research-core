from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset
from research_core.cli import app


def _write_pilot_ops_config(tmp_path: Path, *, dataset_id: str) -> Path:
    path = tmp_path / "pilot.ops.json"
    path.write_text(
        json.dumps(
            {
                "pilot_ops_version": "v1",
                "catalog_dir": "catalog",
                "datasets_path": "datasets.pilot.json",
                "baseline_root": "baselines",
                "label": "prod",
                "out_dir": "pilot_run",
                "runset_kind": "explicit_from_index",
                "require_promoted_baseline": True,
                "doctor_out_subdir": "doctor",
                "drift_out_subdir": "drift",
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    datasets_path = tmp_path / "datasets.pilot.json"
    datasets_path.write_text(
        json.dumps(
            {
                "catalog_dir": "catalog",
                "datasets": [
                    {
                        "instrument": "ES",
                        "tf": "1min",
                        "dataset_id": dataset_id,
                    }
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def test_pilot_run_fail_loud_missing_promotion(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-pilot-fail", run_ref="run")

    config_path = _write_pilot_ops_config(tmp_path, dataset_id=dataset_id)
    result = runner.invoke(app, ["pilot", "run", "--config", str(config_path)])

    assert result.exit_code == 1, result.stdout
    assert "PILOT_RUN status=FAIL" in result.stdout
    assert "baseline promote" in result.stdout
    assert "--label prod" in result.stdout

    summary = json.loads((tmp_path / "pilot_run" / "pilot.run.summary.json").read_text(encoding="utf-8"))
    assert summary["results"]["status"] == "FAIL"
