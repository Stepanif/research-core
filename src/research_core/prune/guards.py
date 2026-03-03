from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.util.types import ValidationError


def _read_json_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON while reading prune guards input: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid JSON object while reading prune guards input: {path}")
    return payload


def collect_protected_paths(*, root: Path, policy: dict[str, Any]) -> set[Path]:
    protected: set[Path] = set()

    keep = policy["keep"]
    if keep["manifests"]:
        for path in root.rglob("*.manifest.json"):
            if path.is_file():
                protected.add(path.resolve())

    if keep["contracts"]:
        for path in root.rglob("*.contract.json"):
            if path.is_file():
                protected.add(path.resolve())

    if keep["goldens"]:
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            rel = path.resolve().relative_to(root.resolve()).as_posix().lower()
            if "/golden/" in f"/{rel}" or "/goldens/" in f"/{rel}":
                protected.add(path.resolve())

    for path in root.rglob("dataset_to_runs.index.json"):
        if path.is_file():
            protected.add(path.resolve())

    for path in root.rglob("runsets.index.json"):
        if path.is_file():
            protected.add(path.resolve())
    for path in root.rglob("entries/*.json"):
        if path.is_file() and path.parent.name == "entries" and path.parent.parent.name == "runsets":
            protected.add(path.resolve())

    for name in ["projects.index.json", "projects.promotions.json"]:
        for path in root.rglob(name):
            if path.is_file():
                protected.add(path.resolve())

    for name in ["ci.summary.json", "ci.summary.manifest.json"]:
        for path in root.rglob(name):
            if path.is_file():
                protected.add(path.resolve())

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = [part.lower() for part in path.resolve().relative_to(root.resolve()).parts]
        if "doctor" in rel_parts or "verify" in rel_parts:
            protected.add(path.resolve())

    baselines = keep["baselines"]
    if baselines["keep_index"]:
        for path in root.rglob("baseline.index.json"):
            if path.is_file():
                protected.add(path.resolve())
    for path in root.rglob("baseline.promotions.json"):
        if path.is_file():
            protected.add(path.resolve())

    if baselines["promoted_only"]:
        for promotions_path in root.rglob("baseline.promotions.json"):
            if not promotions_path.is_file():
                continue
            payload = _read_json_object(promotions_path)
            labels = payload.get("labels")
            if not isinstance(labels, dict):
                raise ValidationError(f"Invalid baseline promotions labels block: {promotions_path}")
            baseline_root = promotions_path.parent

            for label_map in labels.values():
                if not isinstance(label_map, dict):
                    raise ValidationError(f"Invalid baseline promotions mapping in {promotions_path}")
                for runset_id, baseline_id in label_map.items():
                    if not isinstance(runset_id, str) or not runset_id:
                        raise ValidationError(f"Invalid runset_id in baseline promotions: {promotions_path}")
                    if not isinstance(baseline_id, str) or not baseline_id:
                        raise ValidationError(f"Invalid baseline_id in baseline promotions: {promotions_path}")

                    card_path = baseline_root / runset_id / "baseline.card.json"
                    manifest_path = baseline_root / runset_id / "baseline.card.manifest.json"
                    if not card_path.exists() or not card_path.is_file():
                        raise ValidationError(f"Promoted baseline card missing: {card_path}")
                    if not manifest_path.exists() or not manifest_path.is_file():
                        raise ValidationError(f"Promoted baseline manifest missing: {manifest_path}")

                    card_payload = _read_json_object(card_path)
                    checksums = card_payload.get("checksums")
                    if not isinstance(checksums, dict):
                        raise ValidationError(f"Invalid promoted baseline checksums in: {card_path}")
                    actual_baseline_id = checksums.get("per_run_vector_sha256")
                    if actual_baseline_id != baseline_id:
                        raise ValidationError(
                            f"Promotions ambiguity: runset_id={runset_id} in {promotions_path} points to baseline_id={baseline_id} but card has {actual_baseline_id}"
                        )

                    protected.add(card_path.resolve())
                    protected.add(manifest_path.resolve())

    return protected
