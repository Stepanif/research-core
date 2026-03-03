from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def _manifest_canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    data = {key: value for key, value in payload.items() if key != "ci_manifest_canonical_sha256"}
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def test_ci_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-ci-golden")

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
                "label": "prod",
                "fail_on_drift": False,
                "fail_on_checksum_mismatch": True,
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    result = runner.invoke(app, ["ci", "run", "--config", "ci.json"])
    assert result.exit_code == 0, result.stdout

    summary_path = tmp_path / "ci_out" / "ci.summary.json"
    manifest_path = tmp_path / "ci_out" / "ci.summary.manifest.json"
    summary_hash = hashlib.sha256(summary_path.read_bytes()).hexdigest()
    manifest_hash = _manifest_canonical_hash(manifest_path)

    expected_summary_hash = (repo_root / "tests" / "golden" / "ci_small_sample_v1.summary.json.sha256").read_text(encoding="utf-8").strip()
    expected_manifest_hash = (repo_root / "tests" / "golden" / "ci_small_sample_v1.manifest.json.sha256").read_text(encoding="utf-8").strip()

    assert summary_hash == expected_summary_hash
    assert manifest_hash == expected_manifest_hash
