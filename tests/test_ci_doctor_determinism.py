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
    data = {key: value for key, value in payload.items() if key != "ci_doctor_manifest_canonical_sha256"}
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def test_ci_doctor_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-ci-doctor-det")

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
                },
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    one = runner.invoke(app, ["ci", "doctor", "--config", "doctor.json"])
    assert one.exit_code == 0, one.stdout

    summary_path = tmp_path / "doctor_out" / "ci.doctor.summary.json"
    manifest_path = tmp_path / "doctor_out" / "ci.doctor.summary.manifest.json"
    hash_1 = hashlib.sha256(summary_path.read_bytes()).hexdigest()
    manifest_hash_1 = _manifest_canonical_hash(manifest_path)

    two = runner.invoke(app, ["ci", "doctor", "--config", "doctor.json"])
    assert two.exit_code == 0, two.stdout

    hash_2 = hashlib.sha256(summary_path.read_bytes()).hexdigest()
    manifest_hash_2 = _manifest_canonical_hash(manifest_path)

    assert hash_1 == hash_2
    assert manifest_hash_1 == manifest_hash_2
