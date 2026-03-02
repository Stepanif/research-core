from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def _extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def _canonical_sha(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _build_raw_tree(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "a.txt").write_text("alpha\n", encoding="utf-8")
    (root / "b.txt").write_text("beta\n", encoding="utf-8")


def test_dataset_catalog_determinism(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()

    a = tmp_path / "a"
    b = tmp_path / "b"
    a.mkdir(parents=True, exist_ok=True)
    b.mkdir(parents=True, exist_ok=True)

    _build_raw_tree(a / "raw")
    _build_raw_tree(b / "raw")

    monkeypatch.chdir(a)
    reg_a = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "small raw"])
    assert reg_a.exit_code == 0, reg_a.stdout
    dataset_id_a = _extract_dataset_id(reg_a.stdout)

    monkeypatch.chdir(b)
    reg_b = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "small raw"])
    assert reg_b.exit_code == 0, reg_b.stdout
    dataset_id_b = _extract_dataset_id(reg_b.stdout)

    assert dataset_id_a == dataset_id_b

    entry_hash_a = _canonical_sha(a / "catalog" / "entries" / f"{dataset_id_a}.json")
    entry_hash_b = _canonical_sha(b / "catalog" / "entries" / f"{dataset_id_b}.json")
    index_hash_a = _canonical_sha(a / "catalog" / "datasets.index.json")
    index_hash_b = _canonical_sha(b / "catalog" / "datasets.index.json")

    assert entry_hash_a == entry_hash_b
    assert index_hash_a == index_hash_b


def test_dataset_golden_hashes_regression(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.chdir(tmp_path)

    raw_root = tmp_path / "raw"
    _build_raw_tree(raw_root)

    runner = CliRunner()
    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "small raw"])
    assert reg.exit_code == 0, reg.stdout
    dataset_id = _extract_dataset_id(reg.stdout)

    entry_hash = _canonical_sha(tmp_path / "catalog" / "entries" / f"{dataset_id}.json")
    index_hash = _canonical_sha(tmp_path / "catalog" / "datasets.index.json")

    repo_root = Path(__file__).parent.parent
    expected_entry_hash = (repo_root / "tests" / "golden" / "dataset_small_raw_v1.entry.json.sha256").read_text(encoding="utf-8").strip()
    expected_index_hash = (repo_root / "tests" / "golden" / "dataset_small_raw_v1.index.json.sha256").read_text(encoding="utf-8").strip()

    assert entry_hash == expected_entry_hash
    assert index_hash == expected_index_hash
