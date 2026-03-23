from __future__ import annotations

import subprocess
from pathlib import Path


def init_release_fixture_repo(repo_root: Path, tags: list[str]) -> Path:
    repo_root.mkdir(parents=True, exist_ok=True)

    def _run(args: list[str]) -> None:
        subprocess.run(args, cwd=repo_root, check=True, capture_output=True, text=True)

    _run(["git", "init"])
    _run(["git", "config", "user.name", "Research Core Tests"])
    _run(["git", "config", "user.email", "research-core-tests@example.invalid"])

    history_path = repo_root / "history.txt"
    for index, tag in enumerate(tags, start=1):
        history_path.write_text("\n".join(tags[:index]) + "\n", encoding="utf-8")
        _run(["git", "add", "history.txt"])
        _run(["git", "commit", "-m", f"release fixture {tag}"])
        _run(["git", "tag", tag])

    return repo_root