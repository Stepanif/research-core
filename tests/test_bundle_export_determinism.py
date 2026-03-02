from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _build_run(runner: CliRunner, run_dir: Path) -> None:
    for args in [
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
        ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)],
        ["observe", "summary", "--run", str(run_dir)],
        ["observe", "profile", "--run", str(run_dir)],
        ["registry", "refresh", "--run", str(run_dir)],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout


def _manifest_hash_inside_bundle(bundle_path: Path) -> str:
    with zipfile.ZipFile(bundle_path, "r") as archive:
        manifest = json.loads(archive.read("bundle/bundle.manifest.json").decode("utf-8"))
    canonical = json.dumps(manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def test_bundle_export_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    out1 = tmp_path / "bundle1.zip"
    out2 = tmp_path / "bundle2.zip"

    r1 = runner.invoke(app, ["bundle", "export", "--run", str(run_dir), "--out", str(out1)])
    assert r1.exit_code == 0, r1.stdout
    r2 = runner.invoke(app, ["bundle", "export", "--run", str(run_dir), "--out", str(out2)])
    assert r2.exit_code == 0, r2.stdout

    sha1 = hashlib.sha256(out1.read_bytes()).hexdigest()
    sha2 = hashlib.sha256(out2.read_bytes()).hexdigest()
    assert sha1 == sha2

    manifest_hash1 = _manifest_hash_inside_bundle(out1)
    manifest_hash2 = _manifest_hash_inside_bundle(out2)
    assert manifest_hash1 == manifest_hash2
