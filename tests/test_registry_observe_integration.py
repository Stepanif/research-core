from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _build_run(runner: CliRunner, run_dir: Path) -> None:
    canon = runner.invoke(
        app,
        [
            "canon",
            "--in",
            "tests/fixtures/raw_small_sample.txt",
            "--out",
            str(run_dir),
            "--instrument",
            "ES",
            "--tf",
            "1min",
            "--schema",
            "schemas/canon.schema.v1.json",
            "--colmap",
            "schemas/colmap.raw_vendor_v1.json",
        ],
    )
    assert canon.exit_code == 0, canon.stdout

    psa = runner.invoke(app, ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)])
    assert psa.exit_code == 0, psa.stdout

    summary = runner.invoke(app, ["observe", "summary", "--run", str(run_dir)])
    assert summary.exit_code == 0, summary.stdout

    profile = runner.invoke(app, ["observe", "profile", "--run", str(run_dir)])
    assert profile.exit_code == 0, profile.stdout


def test_registry_refresh_includes_observe_and_is_stable(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    refresh_1 = runner.invoke(app, ["registry", "refresh", "--run", str(run_dir)])
    assert refresh_1.exit_code == 0, refresh_1.stdout

    index_path = run_dir.parent / "index.json"
    before_bytes = index_path.read_bytes()
    before_canonical = hashlib.sha256(
        json.dumps(json.loads(index_path.read_text(encoding="utf-8")), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()

    payload = json.loads(index_path.read_text(encoding="utf-8"))
    run_entry = payload["runs"][0]
    observe = run_entry.get("observe", {})
    assert "summary" in observe
    assert "profile" in observe
    assert observe["summary"]["manifest_path"] == "observe/observe.summary.manifest.json"
    assert observe["profile"]["manifest_path"] == "observe/observe.profile.manifest.json"

    refresh_2 = runner.invoke(app, ["registry", "refresh", "--run", str(run_dir)])
    assert refresh_2.exit_code == 0, refresh_2.stdout

    after_bytes = index_path.read_bytes()
    after_canonical = hashlib.sha256(
        json.dumps(json.loads(index_path.read_text(encoding="utf-8")), sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()

    assert before_bytes == after_bytes
    assert before_canonical == after_canonical
