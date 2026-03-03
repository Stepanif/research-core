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
    clone = {key: value for key, value in payload.items() if key != "pilot_run_manifest_canonical_sha256"}
    data = json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


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


def test_pilot_run_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-pilot-golden", run_ref="run")
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, tmp_path / "baselines", label="prod")

    config_path = _write_pilot_ops_config(tmp_path, dataset_id=dataset_id)
    result = runner.invoke(app, ["pilot", "run", "--config", str(config_path)])
    assert result.exit_code == 0, result.stdout

    summary_path = tmp_path / "pilot_run" / "pilot.run.summary.json"
    manifest_path = tmp_path / "pilot_run" / "pilot.run.summary.manifest.json"

    summary_hash = hashlib.sha256(summary_path.read_bytes()).hexdigest()
    manifest_hash = _manifest_canonical_hash(manifest_path)

    expected_summary_hash = (
        repo_root / "tests" / "golden" / "pilot_run_small_sample_v1.summary.json.sha256"
    ).read_text(encoding="utf-8").strip()
    expected_manifest_hash = (
        repo_root / "tests" / "golden" / "pilot_run_small_sample_v1.manifest.json.sha256"
    ).read_text(encoding="utf-8").strip()

    assert summary_hash == expected_summary_hash
    assert manifest_hash == expected_manifest_hash
