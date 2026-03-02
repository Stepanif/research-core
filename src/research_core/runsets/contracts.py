from __future__ import annotations

RUNSET_VERSION = "v1"
RUNSET_INDEX_VERSION = "v1"
REQUIRED_ENV_VAR_CREATED_UTC = "RESEARCH_CREATED_UTC"

DEFAULT_REQUIRED_ARTIFACTS = {
    "canon": True,
    "psa": True,
    "observe": True,
    "experiments": False,
}

DEFAULT_POLICY = {
    "allow_materialize_missing": False,
    "require_lineage_links": True,
    "require_bidirectional": True,
}
