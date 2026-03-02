from __future__ import annotations

RUN_REQUIRED_FILES: tuple[str, ...] = (
    "canon.parquet",
    "canon.manifest.json",
    "psa.parquet",
    "psa.manifest.json",
    "observe/observe.summary.json",
    "observe/observe.summary.manifest.json",
    "observe/observe.profile.json",
    "observe/observe.profile.manifest.json",
)

PROJECT_REQUIRED_FILES: tuple[str, ...] = (
    "project.summary.json",
    "project.manifest.json",
    "README_PROJECT.txt",
)

SECTION_ORDER: tuple[str, ...] = (
    "INPUT",
    "REQUIRED FILES",
    "HASH INTEGRITY",
    "INVARIANTS",
    "OPTIONALS",
    "RESULT",
)
