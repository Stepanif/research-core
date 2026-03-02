from __future__ import annotations

BASELINE_CARD_FILE = "baseline.card.json"
BASELINE_CARD_MANIFEST_FILE = "baseline.card.manifest.json"
BASELINE_INDEX_FILE = "baseline.index.json"
BASELINE_PROMOTIONS_FILE = "baseline.promotions.json"

BASELINE_CARD_VERSION = "v1"
BASELINE_INDEX_VERSION = "v1"
BASELINE_PROMOTIONS_VERSION = "v1"

BASELINE_MANIFEST_SELF_HASH_FIELD = "baseline_card_manifest_canonical_sha256"
DEFAULT_LABEL_PRIORITY: tuple[str, ...] = ("prod", "baseline")