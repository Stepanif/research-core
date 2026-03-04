from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "docs" / "reference" / "cli"

COMMANDS: list[tuple[str, str, list[str]]] = [
    ("CLI Overview", "overview", ["-m", "research_core.cli", "--help"]),
    ("CLI Canon", "canon", ["-m", "research_core.cli", "canon", "--help"]),
    ("CLI Risk", "risk", ["-m", "research_core.cli", "risk", "--help"]),
    ("CLI Risk Run", "risk_run", ["-m", "research_core.cli", "risk", "run", "--help"]),
    (
        "CLI Risk Runset",
        "risk_runset",
        ["-m", "research_core.cli", "risk", "runset", "--help"],
    ),
]

MISSING_MARKERS = (
    "invalid choice",
    "No such command",
    "unrecognized arguments",
    "is not a package",
    "No module named",
)


def _run_help(args: list[str]) -> str | None:
    env = os.environ.copy()
    src_path = str(ROOT / "src")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = src_path if not existing else f"{src_path}{os.pathsep}{existing}"

    cmd = [sys.executable, *args]
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )

    combined = "\n".join(part for part in (result.stdout.strip(), result.stderr.strip()) if part).strip()

    if result.returncode == 0 and combined:
        return combined

    if any(marker in combined for marker in MISSING_MARKERS):
        print(f"WARN: skipping {' '.join(cmd)} (command not available)")
        return None

    print(f"WARN: skipping {' '.join(cmd)} (help invocation failed)")
    return None


def _write_page(title: str, slug: str, help_text: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUT_DIR / f"{slug}.md"
    content = f"# {title}\n\n```text\n{help_text.rstrip()}\n```\n"
    target.write_text(content, encoding="utf-8")


def _write_index(pages: list[tuple[str, str]]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = ["# CLI Reference", ""]
    if not pages:
        lines.append("TODO: No CLI help pages were generated. Verify available commands.")
    else:
        for title, slug in pages:
            lines.append(f"- [{title}]({slug}.md)")
    lines.append("")
    (OUT_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    generated_pages: list[tuple[str, str]] = []
    for title, slug, args in COMMANDS:
        help_text = _run_help(args)
        if help_text is None:
            continue
        _write_page(title, slug, help_text)
        generated_pages.append((title, slug))

    _write_index(generated_pages)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
