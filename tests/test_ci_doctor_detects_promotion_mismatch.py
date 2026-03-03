from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def test_ci_doctor_detects_promotion_mismatch(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-ci-doctor-fail")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, baseline_root, label="prod")

    promotions_path = baseline_root / "baseline.promotions.json"
    promotions_payload = json.loads(promotions_path.read_text(encoding="utf-8"))
    promotions_payload["labels"]["prod"][runset_id] = "deadbeef" * 8
    promotions_path.write_text(
        json.dumps(promotions_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

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
    assert result.exit_code == 1, result.stdout

    summary_path = tmp_path / "doctor_out" / "ci.doctor.summary.json"
    manifest_path = tmp_path / "doctor_out" / "ci.doctor.summary.manifest.json"
    assert summary_path.exists()
    assert manifest_path.exists()

    summary_payload = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary_payload["results"]["status"] == "FAIL"
    assert any(item["check"] == "verify_promotions" for item in summary_payload["results"]["failures"])
