from __future__ import annotations

import json
import os
import zipfile
from pathlib import Path
from typing import Any

from research_core.bundle.contracts import (
    BUNDLE_MANIFEST_ARCHIVE_PATH,
    BUNDLE_VERSION,
    FIXED_ZIP_DATETIME,
    README_ARCHIVE_PATH,
    REGISTRY_ENTRY_ARCHIVE_PATH,
    bundle_archive_path,
    run_optional_paths,
    run_required_paths,
)
from research_core.bundle.hashing import canonical_json_sha256
from research_core.registry.observe_registry import build_registry_run_entry
from research_core.util.hashing import sha256_bytes
from research_core.util.io import read_json
from research_core.util.types import ValidationError


def _read_required_run_files(run_dir: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    for disk_path, archive_path in run_required_paths(run_dir):
        if not disk_path.exists():
            raise ValidationError(f"Missing required bundle input file: {disk_path}")
        files[archive_path] = disk_path.read_bytes()

    for disk_path, archive_path in run_optional_paths(run_dir):
        if disk_path.exists():
            files[archive_path] = disk_path.read_bytes()

    return files


def _run_ref_from_manifests(run_dir: Path, created_utc: str) -> dict[str, str]:
    canon_manifest = read_json(run_dir / "canon.manifest.json")
    psa_manifest = read_json(run_dir / "psa.manifest.json")

    session_policy = canon_manifest.get("session_policy")
    instrument = canon_manifest.get("instrument")
    tf = canon_manifest.get("tf")

    psa_session = psa_manifest.get("session", {})
    tz = psa_session.get("tz")
    rth_start = psa_session.get("rth_start")
    rth_end = psa_session.get("rth_end")

    required = {
        "instrument": instrument,
        "tf": tf,
        "session_policy": session_policy,
        "tz": tz,
        "rth_start": rth_start,
        "rth_end": rth_end,
    }
    missing = [key for key, value in required.items() if not isinstance(value, str) or not value]
    if missing:
        raise ValidationError(f"Missing required run_ref fields for bundle export: {missing}")

    return {
        "instrument": instrument,
        "tf": tf,
        "session_policy": session_policy,
        "tz": tz,
        "rth_start": rth_start,
        "rth_end": rth_end,
        "created_utc": created_utc,
    }


def _registry_entry_json_bytes(run_dir: Path) -> bytes:
    entry = build_registry_run_entry(run_dir)
    serialized = json.dumps(entry, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    return serialized.encode("utf-8")


def _readme_bytes(created_utc: str, included_files: list[dict[str, Any]]) -> bytes:
    lines = [
        "Research Core Audit Bundle",
        "",
        "Purpose: deterministic reproducibility package for a single run.",
        f"Created UTC: {created_utc}",
        "",
        "Included files (archive_path, sha256):",
    ]
    for item in included_files:
        lines.append(f"- {item['archive_path']} {item['sha256']}")
    lines.extend(
        [
            "",
            "Determinism rules:",
            "- Stable archive paths and lexicographic file order",
            "- Fixed zip timestamps (1980-01-01T00:00:00)",
            "- Canonical JSON hash for bundle.manifest.json",
            "",
            "Verification:",
            "sha256sum bundle.zip",
        ]
    )
    return ("\n".join(lines) + "\n").encode("utf-8")


def _bundle_manifest_payload(created_utc: str, run_ref: dict[str, str], included_bytes: dict[str, bytes], registry_entry_bytes: bytes) -> dict[str, Any]:
    included_files = [
        {
            "archive_path": archive_path,
            "bytes": len(content),
            "sha256": sha256_bytes(content),
        }
        for archive_path, content in sorted(included_bytes.items(), key=lambda item: item[0])
    ]

    payload: dict[str, Any] = {
        "bundle_version": BUNDLE_VERSION,
        "created_utc": created_utc,
        "run_ref": run_ref,
        "included_files": included_files,
        "registry_entry_sha256": sha256_bytes(registry_entry_bytes),
    }
    payload["bundle_manifest_canonical_sha256"] = canonical_json_sha256(payload)
    return payload


def _zip_write_bytes(zip_file: zipfile.ZipFile, archive_path: str, payload: bytes) -> None:
    info = zipfile.ZipInfo(filename=archive_path)
    info.date_time = FIXED_ZIP_DATETIME
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zip_file.writestr(info, payload)


def export_bundle(run_dir: Path, bundle_zip_path: Path) -> Path:
    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not created_utc:
        canon_manifest = read_json(run_dir / "canon.manifest.json")
        created_utc = canon_manifest.get("created_utc")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Bundle export requires deterministic created_utc (RESEARCH_CREATED_UTC or canon.manifest created_utc)")

    included = _read_required_run_files(run_dir)
    run_ref = _run_ref_from_manifests(run_dir, created_utc=created_utc)

    registry_entry_bytes = _registry_entry_json_bytes(run_dir)
    included[bundle_archive_path(REGISTRY_ENTRY_ARCHIVE_PATH)] = registry_entry_bytes

    manifest_payload = _bundle_manifest_payload(
        created_utc=created_utc,
        run_ref=run_ref,
        included_bytes=included,
        registry_entry_bytes=registry_entry_bytes,
    )
    manifest_bytes = (json.dumps(manifest_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")
    included[bundle_archive_path(BUNDLE_MANIFEST_ARCHIVE_PATH)] = manifest_bytes

    readme_bytes = _readme_bytes(created_utc=created_utc, included_files=manifest_payload["included_files"])
    included[bundle_archive_path(README_ARCHIVE_PATH)] = readme_bytes

    bundle_zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(bundle_zip_path, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for archive_path in sorted(included.keys()):
            _zip_write_bytes(archive, archive_path=archive_path, payload=included[archive_path])

    return bundle_zip_path
