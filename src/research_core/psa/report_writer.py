from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.util.buildmeta import get_git_commit
from research_core.util.hashing import sha256_bytes, sha256_file


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _canonical_hash(payload: dict[str, Any], self_field: str | None = None) -> str:
    clone = dict(payload)
    if isinstance(self_field, str):
        clone.pop(self_field, None)
    data = json.dumps(clone, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return sha256_bytes(data)


def _pretty_json_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def _rel(path: Path, run_dir: Path) -> str:
    return path.resolve().relative_to(run_dir.resolve()).as_posix()


def write_psa_report_artifacts(*, run_dir: Path, report_payload: dict[str, Any]) -> dict[str, Path | dict[str, Any]]:
    report_path = run_dir / "psa.report.json"
    manifest_path = run_dir / "psa.report.manifest.json"

    report_bytes = _pretty_json_bytes(report_payload)

    psa_parquet = run_dir / "psa.parquet"
    psa_manifest = run_dir / "psa.manifest.json"

    manifest: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": str(report_payload["created_utc"]),
        "git_commit": get_git_commit(_repo_root()),
        "inputs": [
            {
                "path": _rel(psa_parquet, run_dir),
                "bytes": int(psa_parquet.stat().st_size),
                "sha256": sha256_file(psa_parquet),
            },
            {
                "path": _rel(psa_manifest, run_dir),
                "bytes": int(psa_manifest.stat().st_size),
                "sha256": sha256_file(psa_manifest),
            },
        ],
        "outputs": {
            "psa.report.json": {
                "bytes": len(report_bytes),
                "sha256": sha256_bytes(report_bytes),
            }
        },
    }
    manifest["manifest_canonical_sha256"] = _canonical_hash(manifest, self_field="manifest_canonical_sha256")

    report_tmp = run_dir / "psa.report.json.tmp"
    manifest_tmp = run_dir / "psa.report.manifest.json.tmp"

    report_tmp.write_bytes(report_bytes)
    manifest_tmp.write_bytes(_pretty_json_bytes(manifest))

    report_tmp.replace(report_path)
    manifest_tmp.replace(manifest_path)

    return {
        "report": report_payload,
        "manifest": manifest,
        "report_path": report_path,
        "manifest_path": manifest_path,
    }
