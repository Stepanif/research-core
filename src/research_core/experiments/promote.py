from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.util.io import read_json
from research_core.util.types import ValidationError


def _promotions_path(run_dir: Path) -> Path:
    return run_dir / "experiments" / "promotions.json"


def _load_or_init_promotions(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"promotions_version": "v1", "labels": {}}

    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid promotions payload: {path}")
    if payload.get("promotions_version") != "v1":
        raise ValidationError(f"Unsupported promotions_version in {path}")
    labels = payload.get("labels")
    if not isinstance(labels, dict):
        raise ValidationError(f"Invalid promotions labels block in {path}")
    return payload


def promote_experiment_label(run_dir: Path, exp_id: str, label: str) -> dict[str, Any]:
    manifest_path = run_dir / "experiments" / exp_id / "exp.manifest.json"
    if not manifest_path.exists():
        raise ValidationError(f"Cannot promote missing experiment exp_id={exp_id}: {manifest_path}")

    path = _promotions_path(run_dir)
    payload = _load_or_init_promotions(path)
    labels = payload["labels"]

    existing = labels.get(label)
    if existing is not None and existing != exp_id:
        raise ValidationError(
            f"Promotion immutability violation for label={label}: existing exp_id={existing} differs from requested exp_id={exp_id}"
        )

    labels[label] = exp_id
    output = {
        "promotions_version": "v1",
        "labels": {key: labels[key] for key in sorted(labels.keys())},
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(output, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return output
