from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def test_ci_doctor_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-ci-doctor-smoke")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, baseline_root, label="prod")

    runsets_path = tmp_path / "runsets.json"
    runsets_path.write_text(
        json.dumps({"runset_ids": [runset_id]}, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    config_path = tmp_path / "doctor.json"
    config_path.write_text(
        json.dumps(
            {
                "doctor_version": "v1",
                "catalog_dir": "catalog",
                "baseline_root": "baselines",
                "runsets_path": "runsets.json",
                "out_dir": "doctor_out",
                "label": "prod",
                "checks": {
                    "verify_baseline_root": True,
                    "verify_promotions": True,
                    "verify_runsets": True,
                    "verify_bundles": False,
                    "verify_dashboard": False,
                },
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    result = runner.invoke(app, ["ci", "doctor", "--config", "doctor.json"])
    assert result.exit_code == 0, result.stdout

    assert (tmp_path / "doctor_out" / "ci.doctor.summary.json").exists()
    assert (tmp_path / "doctor_out" / "ci.doctor.summary.manifest.json").exists()
