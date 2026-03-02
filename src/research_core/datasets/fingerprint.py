from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def stable_root_ref(path: Path, cwd: Path | None = None) -> str:
    base = cwd or Path.cwd()
    if not path.is_absolute():
        return path.as_posix()
    if path.is_relative_to(base):
        return path.relative_to(base).as_posix()
    raise ValidationError(
        f"Dataset source path must be relative to current working directory to avoid absolute storage: {path}"
    )


def enumerate_root_files(root_dir: Path) -> list[dict[str, Any]]:
    if not root_dir.exists() or not root_dir.is_dir():
        raise ValidationError(f"Dataset root does not exist or is not a directory: {root_dir}")

    files = sorted([path for path in root_dir.rglob("*") if path.is_file()], key=lambda p: p.relative_to(root_dir).as_posix())
    out: list[dict[str, Any]] = []
    for path in files:
        stat = path.stat()
        out.append(
            {
                "path": path.relative_to(root_dir).as_posix(),
                "bytes": int(stat.st_size),
                "sha256": sha256_file(path),
            }
        )
    return out


def enumerate_specific_files(root_dir: Path, relative_files: list[str]) -> list[dict[str, Any]]:
    normalized = sorted({Path(item).as_posix() for item in relative_files})
    out: list[dict[str, Any]] = []
    for rel in normalized:
        path = root_dir / rel
        if not path.exists() or not path.is_file():
            raise ValidationError(f"Dataset required file missing: {path}")
        stat = path.stat()
        out.append(
            {
                "path": rel,
                "bytes": int(stat.st_size),
                "sha256": sha256_file(path),
            }
        )
    return out


def files_sha256(files: list[dict[str, Any]]) -> str:
    lines = [f"{item['sha256']}  {item['path']}\n" for item in sorted(files, key=lambda x: str(x["path"]))]
    return sha256_bytes("".join(lines).encode("utf-8"))


def source_counts(files: list[dict[str, Any]]) -> tuple[int, int]:
    return len(files), sum(int(item["bytes"]) for item in files)
