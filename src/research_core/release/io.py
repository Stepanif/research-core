from __future__ import annotations

import subprocess
from pathlib import Path

from research_core.util.types import ValidationError


def resolve_commit(repo_root: Path, ref: str) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", f"{ref}^{{commit}}"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip() if isinstance(exc.stderr, str) else ""
        raise ValidationError(f"Invalid git ref: {ref}. {stderr}".strip()) from exc
    sha = result.stdout.strip()
    if not sha:
        raise ValidationError(f"Unable to resolve git ref: {ref}")
    return sha


def list_commit_subjects(repo_root: Path, from_sha: str, to_sha: str) -> list[tuple[str, str]]:
    try:
        result = subprocess.run(
            ["git", "log", "--reverse", "--no-merges", "--pretty=format:%H|%s", f"{from_sha}..{to_sha}"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip() if isinstance(exc.stderr, str) else ""
        raise ValidationError(f"Unable to list commits for range {from_sha}..{to_sha}. {stderr}".strip()) from exc

    lines = [line for line in result.stdout.splitlines() if line.strip()]
    commits: list[tuple[str, str]] = []
    for line in lines:
        parts = line.split("|", 1)
        if len(parts) != 2:
            continue
        sha, subject = parts[0].strip(), parts[1].strip()
        if not sha or not subject:
            continue
        commits.append((sha, subject))
    return commits
