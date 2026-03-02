from __future__ import annotations

from pathlib import Path


def _normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def write_task_logs(logs_dir: Path, task_id: str, stdout_text: str, stderr_text: str) -> tuple[Path, Path]:
    logs_dir.mkdir(parents=True, exist_ok=True)

    stdout_path = logs_dir / f"{task_id}.stdout.log"
    stderr_path = logs_dir / f"{task_id}.stderr.log"

    stdout_payload = _normalize_newlines(stdout_text)
    stderr_payload = _normalize_newlines(stderr_text)

    if not stdout_payload:
        stdout_payload = "<empty>\n"
    elif not stdout_payload.endswith("\n"):
        stdout_payload += "\n"

    if not stderr_payload:
        stderr_payload = "<empty>\n"
    elif not stderr_payload.endswith("\n"):
        stderr_payload += "\n"

    stdout_path.write_text(stdout_payload, encoding="utf-8", newline="\n")
    stderr_path.write_text(stderr_payload, encoding="utf-8", newline="\n")
    return stdout_path, stderr_path
