from __future__ import annotations

from pathlib import Path

from research_core.util.types import ValidationError


def materialize_runset(*, catalog_dir: Path, runset_id: str, runs_root: Path, project_out: Path) -> dict[str, str]:
    raise ValidationError(
        "runset materialize is not implemented in phase8 step1; use runset create/list/show/validate"
    )
