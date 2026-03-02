from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.observe.contracts import OBSERVE_MANIFEST_VERSION, OBSERVE_TOOL_VERSION
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.io import canonical_json_bytes


def write_observe_summary(path: Path, payload: dict[str, Any]) -> None:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    path.write_text(serialized, encoding="utf-8")


def write_observe_profile(path: Path, payload: dict[str, Any]) -> None:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    path.write_text(serialized, encoding="utf-8")


def _manifest_input_files(run_dir: Path) -> list[dict[str, Any]]:
    required = [
        run_dir / "canon.parquet",
        run_dir / "canon.manifest.json",
        run_dir / "psa.parquet",
        run_dir / "psa.manifest.json",
    ]
    optional = [run_dir / "psa.log"]

    files = required + [path for path in optional if path.exists()]
    files = sorted(files, key=lambda path: path.name)
    return [
        {
            "path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in files
    ]


def _manifest_input_files_profile(run_dir: Path) -> list[dict[str, Any]]:
    required = [
        run_dir / "psa.parquet",
        run_dir / "psa.manifest.json",
        run_dir / "canon.manifest.json",
    ]
    optional = [run_dir / "psa.log"]

    files = required + [path for path in optional if path.exists()]
    files = sorted(files, key=lambda path: path.name)
    return [
        {
            "path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in files
    ]


def build_observe_manifest(run_dir: Path, observe_summary_path: Path) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "manifest_version": OBSERVE_MANIFEST_VERSION,
        "tool_version": OBSERVE_TOOL_VERSION,
        "input_files": _manifest_input_files(run_dir),
        "output_files": {
            "observe.summary.json": {
                "path": observe_summary_path.name,
                "bytes": observe_summary_path.stat().st_size,
                "sha256": sha256_file(observe_summary_path),
            }
        },
    }
    payload["canonical_json_sha256"] = sha256_bytes(canonical_json_bytes(payload))
    return payload


def build_observe_profile_manifest(run_dir: Path, observe_profile_path: Path) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "manifest_version": OBSERVE_MANIFEST_VERSION,
        "tool_version": OBSERVE_TOOL_VERSION,
        "input_files": _manifest_input_files_profile(run_dir),
        "output_files": {
            "observe.profile.json": {
                "path": observe_profile_path.name,
                "bytes": observe_profile_path.stat().st_size,
                "sha256": sha256_file(observe_profile_path),
            }
        },
    }
    payload["canonical_json_sha256"] = sha256_bytes(canonical_json_bytes(payload))
    return payload


def write_observe_manifest(path: Path, payload: dict[str, Any]) -> None:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    path.write_text(serialized, encoding="utf-8")


def write_observe_profile_manifest(path: Path, payload: dict[str, Any]) -> None:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    path.write_text(serialized, encoding="utf-8")
