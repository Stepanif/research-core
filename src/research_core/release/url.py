from __future__ import annotations

import re
import subprocess
from pathlib import Path

from research_core.util.types import ValidationError


def _read_origin_url(repo_root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            cwd=str(repo_root),
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = exc.stderr.strip() if isinstance(exc.stderr, str) else ""
        raise ValidationError(f"Missing git origin remote URL. {stderr}".strip()) from exc
    origin = result.stdout.strip()
    if not origin:
        raise ValidationError("Missing git origin remote URL")
    return origin


def normalize_github_repo_https_url(origin_url: str) -> str:
    value = origin_url.strip()
    https_match = re.fullmatch(r"https://github\.com/([^/]+)/([^/]+?)(?:\.git)?", value)
    if https_match:
        owner, repo = https_match.group(1), https_match.group(2)
        return f"https://github.com/{owner}/{repo}"

    ssh_match = re.fullmatch(r"git@github\.com:([^/]+)/([^/]+?)(?:\.git)?", value)
    if ssh_match:
        owner, repo = ssh_match.group(1), ssh_match.group(2)
        return f"https://github.com/{owner}/{repo}"

    raise ValidationError(f"Unsupported origin URL (expected GitHub https/ssh): {origin_url}")


def build_new_release_url(*, repo_root: Path, tag: str) -> str:
    if not isinstance(tag, str) or not tag:
        raise ValidationError("release url requires --tag")
    origin = _read_origin_url(repo_root)
    base = normalize_github_repo_https_url(origin)
    return f"{base}/releases/new?tag={tag}"
