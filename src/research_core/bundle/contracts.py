from __future__ import annotations

from pathlib import Path

BUNDLE_VERSION = "v1"
BUNDLE_ROOT = "bundle"
FIXED_ZIP_DATETIME = (1980, 1, 1, 0, 0, 0)

REQUIRED_RUN_FILES: list[tuple[str, str]] = [
    ("canon.parquet", "run/canon.parquet"),
    ("canon.manifest.json", "run/canon.manifest.json"),
    ("psa.parquet", "run/psa.parquet"),
    ("psa.manifest.json", "run/psa.manifest.json"),
    ("observe/observe.summary.json", "run/observe/observe.summary.json"),
    ("observe/observe.summary.manifest.json", "run/observe/observe.summary.manifest.json"),
    ("observe/observe.profile.json", "run/observe/observe.profile.json"),
    ("observe/observe.profile.manifest.json", "run/observe/observe.profile.manifest.json"),
]

OPTIONAL_RUN_FILES: list[tuple[str, str]] = [
    ("psa.log", "run/psa.log"),
]

REGISTRY_ENTRY_ARCHIVE_PATH = "registry/registry_entry.json"
BUNDLE_MANIFEST_ARCHIVE_PATH = "bundle.manifest.json"
README_ARCHIVE_PATH = "README_BUNDLE.txt"


def bundle_archive_path(relative_path: str) -> str:
    return f"{BUNDLE_ROOT}/{relative_path}"


def run_required_paths(run_dir: Path) -> list[tuple[Path, str]]:
    return [(run_dir / relative_disk, bundle_archive_path(relative_archive)) for relative_disk, relative_archive in REQUIRED_RUN_FILES]


def run_optional_paths(run_dir: Path) -> list[tuple[Path, str]]:
    return [(run_dir / relative_disk, bundle_archive_path(relative_archive)) for relative_disk, relative_archive in OPTIONAL_RUN_FILES]
