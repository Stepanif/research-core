from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.ci.runner as ci_runner
import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, prepare_promoted_baseline_root
from research_core.cli import app
from research_core.runsets.io import canonical_hash


def test_ci_run_fail_on_drift(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-ci-fail")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, baseline_root, label="prod")

    runsets_path = tmp_path / "runsets.json"
    runsets_path.write_text(
        json.dumps({"runset_ids": [runset_id]}, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    config_path = tmp_path / "ci.json"
    config_path.write_text(
        json.dumps(
            {
                "ci_version": "v1",
                "catalog_dir": "catalog",
                "baseline_root": "baselines",
                "runsets_path": "runsets.json",
                "out_dir": "ci_out",
                "fail_on_drift": True,
                "fail_on_checksum_mismatch": True,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    def fake_dashboard(**_: object) -> dict[str, object]:
        out_dir = tmp_path / "ci_out"
        out_dir.mkdir(parents=True, exist_ok=True)
        summary = {
            "dashboard_version": "v1",
            "created_utc": "2026-01-01T00:00:00+00:00",
            "label": "prod",
            "runset_count": 1,
            "entries": [],
            "aggregates": {
                "counts": {"DRIFT": 1, "NO_DRIFT": 0},
                "checksum_mismatch_count": 0,
                "top_abs_instability_delta_5": [],
                "lowest_jaccard_5": [],
            },
        }
        summary["dashboard_canonical_sha256"] = canonical_hash(summary, self_field="dashboard_canonical_sha256")
        manifest = {
            "manifest_version": "v1",
            "created_utc": "2026-01-01T00:00:00+00:00",
            "inputs": [],
            "outputs": {"dashboard.summary.json": {"sha256": "x", "bytes": 0}},
        }
        manifest["dashboard_manifest_canonical_sha256"] = canonical_hash(
            manifest,
            self_field="dashboard_manifest_canonical_sha256",
        )
        (out_dir / "dashboard.summary.json").write_text(
            json.dumps(summary, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (out_dir / "dashboard.summary.manifest.json").write_text(
            json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        return {
            "runset_count": 1,
            "summary_path": out_dir / "dashboard.summary.json",
            "manifest_path": out_dir / "dashboard.summary.manifest.json",
        }

    monkeypatch.setattr(ci_runner, "run_risk_dashboard", fake_dashboard)

    result = runner.invoke(app, ["ci", "run", "--config", "ci.json"])
    assert result.exit_code == 1
