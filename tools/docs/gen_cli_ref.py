from __future__ import annotations

import os
import re
import subprocess
import sys
import textwrap
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

TABLE_TOP_RE = re.compile(r"^\+- (?P<title>.*?) -+\+$")
TABLE_BOTTOM_RE = re.compile(r"^\+-+\+$")
WRAPPED_OPTION_TABLE_WIDTH = 75


def _normalize_text(text: str) -> str:
    normalized_lines = [line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while normalized_lines and normalized_lines[-1] == "":
        normalized_lines.pop()
    return "\n".join(normalized_lines)


def _normalize_wrapped_option_rows(title: str, row_lines: list[str]) -> list[str] | None:
    if title != "Options":
        return None

    row_contents = [line[1:-1].rstrip() for line in row_lines]
    continuation_indents = [
        len(content) - len(content.lstrip(" "))
        for content in row_contents
        if content.strip() and not content.lstrip().startswith(("-", "*"))
    ]
    if not continuation_indents:
        return None

    desc_start = min(continuation_indents)
    inner_width = WRAPPED_OPTION_TABLE_WIDTH - 2
    desc_width = inner_width - desc_start
    if desc_width < 8:
        return None

    logical_rows: list[list[str]] = []
    for content in row_contents:
        left = content[:desc_start].rstrip()
        right = content[desc_start:].strip()
        if left.strip():
            logical_rows.append([left.strip(), right])
        elif logical_rows and right:
            logical_rows[-1][1] = f"{logical_rows[-1][1]} {right}".strip()
        else:
            return None

    normalized_rows: list[str] = []
    for left, right in logical_rows:
        wrapped = textwrap.wrap(right, width=desc_width) or [""]
        left_segment = f" {left}".ljust(desc_start)
        normalized_rows.append(f"|{left_segment}{wrapped[0].ljust(desc_width)}|")
        for continuation in wrapped[1:]:
            normalized_rows.append(f"|{' ' * desc_start}{continuation.ljust(desc_width)}|")

    return normalized_rows


def _normalize_help_tables(text: str) -> str:
    lines = text.split("\n")
    normalized: list[str] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        top_match = TABLE_TOP_RE.match(line)
        if not top_match:
            normalized.append(line)
            index += 1
            continue

        row_lines: list[str] = []
        scan_index = index + 1
        while scan_index < len(lines) and lines[scan_index].startswith("|") and lines[scan_index].endswith("|"):
            row_content = lines[scan_index][1:-1].rstrip()
            row_lines.append(f"|{row_content} |")
            scan_index += 1

        if not row_lines or scan_index >= len(lines) or not TABLE_BOTTOM_RE.match(lines[scan_index]):
            normalized.append(line)
            index += 1
            continue

        normalized_option_rows = _normalize_wrapped_option_rows(top_match.group("title"), row_lines)
        if normalized_option_rows is not None:
            title_prefix = f"+- {top_match.group('title')} "
            top_dashes = "-" * max(1, WRAPPED_OPTION_TABLE_WIDTH - len(title_prefix) - 1)
            bottom_dashes = "-" * max(1, WRAPPED_OPTION_TABLE_WIDTH - 2)
            normalized.append(f"{title_prefix}{top_dashes}+")
            normalized.extend(normalized_option_rows)
            normalized.append(f"+{bottom_dashes}+")
            index = scan_index + 1
            continue

        title_prefix = f"+- {top_match.group('title')} "
        target_width = max(
            max(len(row) for row in row_lines),
            len(title_prefix) + 2,
        )
        top_dashes = "-" * max(1, target_width - len(title_prefix) - 1)
        bottom_dashes = "-" * max(1, target_width - 2)

        normalized.append(f"{title_prefix}{top_dashes}+")
        normalized.extend(row_lines)
        normalized.append(f"+{bottom_dashes}+")
        index = scan_index + 1

    return "\n".join(normalized)


def _write_normalized(path: Path, content: str) -> None:
    path.write_text(_normalize_text(content) + "\n", encoding="utf-8", newline="\n")


def _run_help(args: list[str]) -> str | None:
    env = os.environ.copy()
    src_path = str(ROOT / "src")
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = src_path if not existing else f"{src_path}{os.pathsep}{existing}"
    env["TERM"] = "dumb"
    env["NO_COLOR"] = "1"
    env["COLUMNS"] = "80"

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

    combined = _normalize_help_tables(_normalize_text("\n".join(part for part in (result.stdout, result.stderr) if part)))

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
    content = f"# {title}\n\n```text\n{_normalize_text(help_text)}\n```"
    _write_normalized(target, content)


def _write_index(pages: list[tuple[str, str]]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        "# CLI Reference",
        "",
        "This section is generated by tools/docs/gen_cli_ref.py",
        "",
    ]
    if not pages:
        lines.append("TODO: No CLI help pages were generated. Verify available commands.")
    else:
        for title, slug in sorted(pages, key=lambda item: item[1]):
            lines.append(f"- [{title}]({slug}.md)")
    _write_normalized(OUT_DIR / "index.md", "\n".join(lines))


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
