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


def _write_pilot_ops_config(tmp_path: Path, *, dataset_id: str, out_dir: str, file_name: str) -> Path:
    path = tmp_path / file_name
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


def test_pilot_run_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-pilot-det", run_ref="run")
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, tmp_path / "baselines", label="prod")

    config_one = _write_pilot_ops_config(tmp_path, dataset_id=dataset_id, out_dir="pilot_run_one", file_name="pilot.one.json")
    one = runner.invoke(app, ["pilot", "run", "--config", str(config_one)])
    assert one.exit_code == 0, one.stdout

    config_two = _write_pilot_ops_config(tmp_path, dataset_id=dataset_id, out_dir="pilot_run_two", file_name="pilot.two.json")
    two = runner.invoke(app, ["pilot", "run", "--config", str(config_two)])
    assert two.exit_code == 0, two.stdout

    summary_one = tmp_path / "pilot_run_one" / "pilot.run.summary.json"
    summary_two = tmp_path / "pilot_run_two" / "pilot.run.summary.json"
    manifest_one = tmp_path / "pilot_run_one" / "pilot.run.summary.manifest.json"
    manifest_two = tmp_path / "pilot_run_two" / "pilot.run.summary.manifest.json"

    assert hashlib.sha256(summary_one.read_bytes()).hexdigest() == hashlib.sha256(summary_two.read_bytes()).hexdigest()
    assert _manifest_canonical_hash(manifest_one) == _manifest_canonical_hash(manifest_two)
