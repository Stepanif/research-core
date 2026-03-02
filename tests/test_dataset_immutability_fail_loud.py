from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def _extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def test_dataset_immutability_fail_loud(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.chdir(tmp_path)

    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    (raw_root / "a.txt").write_text("alpha\n", encoding="utf-8")
    (raw_root / "b.txt").write_text("beta\n", encoding="utf-8")

    runner = CliRunner()
    reg1 = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw"])
    assert reg1.exit_code == 0, reg1.stdout
    dataset_id_1 = _extract_dataset_id(reg1.stdout)

    (raw_root / "a.txt").write_text("alpha-mutated\n", encoding="utf-8")

    validate_old = runner.invoke(app, ["dataset", "validate", "--catalog", "catalog", "--id", dataset_id_1])
    assert validate_old.exit_code != 0
    assert "FAIL" in validate_old.stdout

    reg2 = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw"])
    assert reg2.exit_code == 0, reg2.stdout
    dataset_id_2 = _extract_dataset_id(reg2.stdout)
    assert dataset_id_2 != dataset_id_1
