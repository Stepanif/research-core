from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def _canonical_hash_excluding(path: Path, exclude_field: str) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    data = {k: v for k, v in payload.items() if k != exclude_field}
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def test_risk_run_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()

    run_dir = tmp_path / "run"
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

    first = runner.invoke(app, ["risk", "run", "--run", str(run_dir)])
    assert first.exit_code == 0, first.stdout

    summary_path = run_dir / "risk" / "risk.summary.json"
    manifest_path = run_dir / "risk" / "risk.summary.manifest.json"

    summary_hash_1 = hashlib.sha256(summary_path.read_bytes()).hexdigest()
    manifest_hash_1 = _canonical_hash_excluding(manifest_path, "risk_manifest_canonical_sha256")

    second = runner.invoke(app, ["risk", "run", "--run", str(run_dir)])
    assert second.exit_code == 0, second.stdout

    summary_hash_2 = hashlib.sha256(summary_path.read_bytes()).hexdigest()
    manifest_hash_2 = _canonical_hash_excluding(manifest_path, "risk_manifest_canonical_sha256")

    assert summary_hash_1 == summary_hash_2
    assert manifest_hash_1 == manifest_hash_2
