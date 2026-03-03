from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def _write_pilot_ops_config(tmp_path: Path, *, dataset_id: str, out_dir: str) -> Path:
    path = tmp_path / "pilot.ops.json"
    path.write_text(
        json.dumps(
            {
                "pilot_ops_version": "v1",
                "catalog_dir": "catalog",
                "datasets_path": "datasets.pilot.json",
                "baseline_root": "baselines",
                "label": "prod",
                "out_dir": out_dir,
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


def test_pilot_run_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-pilot-smoke", run_ref="run")
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, tmp_path / "baselines", label="prod")

    config_path = _write_pilot_ops_config(tmp_path, dataset_id=dataset_id, out_dir="pilot_run")
    result = runner.invoke(app, ["pilot", "run", "--config", str(config_path)])
    assert result.exit_code == 0, result.stdout
    assert "PILOT_RUN status=PASS" in result.stdout

    assert (tmp_path / "pilot_run" / "pilot.run.summary.json").exists()
    assert (tmp_path / "pilot_run" / "pilot.run.summary.manifest.json").exists()
    assert (tmp_path / "pilot_run" / "drift" / runset_id / "drift.report.json").exists()
    assert (tmp_path / "pilot_run" / "doctor" / "ci.doctor.summary.json").exists()
