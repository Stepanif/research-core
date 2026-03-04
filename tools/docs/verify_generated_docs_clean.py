from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _run_script(script_name: str) -> None:
    cmd = [sys.executable, str(ROOT / "tools" / "docs" / script_name)]
    subprocess.run(cmd, cwd=ROOT, check=True)


def main() -> int:
    _run_script("gen_cli_ref.py")
    _run_script("gen_schema_ref.py")
    _run_script("gen_artifact_catalog.py")

    diff = subprocess.run(
        [
            "git",
            "diff",
            "--name-only",
            "--",
            "docs/reference/cli",
            "docs/reference/schemas",
            "docs/reference/artifacts",
            ":(exclude)docs/reference/artifacts/catalog.v1.yml",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if diff.stdout.strip():
        print("Generated docs drift detected:")
        print(diff.stdout.strip())
        return 1

    print("Generated docs are clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
