from __future__ import annotations

from pathlib import Path

PILOT_OPS_VERSION = "v1"
PILOT_RUN_VERSION = "v1"
PILOT_RUNSET_KIND = "explicit_from_index"

DEFAULT_LABEL = "prod"
DEFAULT_REQUIRE_PROMOTED_BASELINE = True
DEFAULT_DOCTOR_OUT_SUBDIR = "doctor"
DEFAULT_DRIFT_OUT_SUBDIR = "drift"

PILOT_OPS_SCHEMA_PATH = Path("schemas/pilot.ops.config.schema.v1.json")
PILOT_RUN_SUMMARY_SCHEMA_PATH = Path("schemas/pilot.run.summary.schema.v1.json")

PILOT_SUMMARY_FILE = "pilot.run.summary.json"
PILOT_SUMMARY_MANIFEST_FILE = "pilot.run.summary.manifest.json"

PILOT_SUMMARY_HASH_FIELD = "pilot_run_canonical_sha256"
PILOT_MANIFEST_HASH_FIELD = "pilot_run_manifest_canonical_sha256"
