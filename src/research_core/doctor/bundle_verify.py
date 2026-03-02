from __future__ import annotations

import json
import zipfile
from pathlib import Path
from typing import Any

from research_core.doctor.formatting import CheckItem, render_doctor_text
from research_core.util.hashing import sha256_bytes, sha256_json


def _record(section: list[CheckItem], check_id: str, ok: bool, detail: str) -> None:
    section.append(CheckItem(check_id=check_id, ok=ok, detail=detail))


def verify_bundle_text(bundle_zip_path: Path) -> tuple[str, bool]:
    required: list[CheckItem] = []
    hash_integrity: list[CheckItem] = []
    invariants: list[CheckItem] = []
    optionals: list[CheckItem] = []

    _record(required, "required.bundle_zip", bundle_zip_path.exists() and bundle_zip_path.is_file(), bundle_zip_path.as_posix())

    if not bundle_zip_path.exists() or not bundle_zip_path.is_file():
        result = [CheckItem(check_id="result", ok=False, detail="FAIL")]
        text = render_doctor_text(
            input_lines=[f"zip={bundle_zip_path.as_posix()}"],
            required=required,
            hash_integrity=hash_integrity,
            invariants=invariants,
            optionals=optionals,
            result=result,
        )
        return text, False

    with zipfile.ZipFile(bundle_zip_path, "r") as archive:
        names = set(archive.namelist())
        manifest_archive_path = "bundle/bundle.manifest.json"
        manifest_present = manifest_archive_path in names
        _record(required, "required.bundle_manifest", manifest_present, manifest_archive_path)

        if not manifest_present:
            result = [CheckItem(check_id="result", ok=False, detail="FAIL")]
            text = render_doctor_text(
                input_lines=[f"zip={bundle_zip_path.as_posix()}"],
                required=required,
                hash_integrity=hash_integrity,
                invariants=invariants,
                optionals=optionals,
                result=result,
            )
            return text, False

        manifest_payload = json.loads(archive.read(manifest_archive_path).decode("utf-8"))

        included_files = manifest_payload.get("included_files")
        if not isinstance(included_files, list):
            _record(invariants, "invariant.included_files_format", False, "invalid included_files")
            included_files = []

        for item in sorted(
            [entry for entry in included_files if isinstance(entry, dict)],
            key=lambda entry: str(entry.get("archive_path", "")),
        ):
            archive_path = item.get("archive_path")
            expected_sha = item.get("sha256")
            check_id = f"hash.file.{archive_path}"
            if not isinstance(archive_path, str) or not archive_path:
                _record(hash_integrity, check_id, False, "invalid archive_path")
                continue
            if not isinstance(expected_sha, str) or not expected_sha:
                _record(hash_integrity, check_id, False, "missing sha256")
                continue
            if archive_path not in names:
                _record(hash_integrity, check_id, False, "missing in zip")
                continue

            actual_sha = sha256_bytes(archive.read(archive_path))
            _record(hash_integrity, check_id, actual_sha == expected_sha, archive_path)

        canonical_field = manifest_payload.get("bundle_manifest_canonical_sha256")
        if isinstance(canonical_field, str) and canonical_field:
            actual_canonical = sha256_json(
                {key: value for key, value in manifest_payload.items() if key != "bundle_manifest_canonical_sha256"}
            )
            _record(
                hash_integrity,
                "hash.bundle_manifest_canonical_sha256",
                actual_canonical == canonical_field,
                "bundle/bundle.manifest.json",
            )

    all_checks = required + hash_integrity + invariants + optionals
    all_ok = all(item.ok for item in all_checks)
    result = [CheckItem(check_id="result", ok=all_ok, detail="PASS" if all_ok else "FAIL")]
    text = render_doctor_text(
        input_lines=[f"zip={bundle_zip_path.as_posix()}"],
        required=required,
        hash_integrity=hash_integrity,
        invariants=invariants,
        optionals=optionals,
        result=result,
    )
    return text, all_ok
