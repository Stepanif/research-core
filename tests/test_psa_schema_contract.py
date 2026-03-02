from __future__ import annotations

import json
from pathlib import Path


def test_psa_schema_required_columns_present() -> None:
    payload = json.loads(Path("schemas/psa.schema.v1.json").read_text(encoding="utf-8"))
    assert payload["psa_version"] == "v1"
    required_columns = payload["required_columns"]
    assert "ts" in required_columns
    assert "instrument" in required_columns
    assert "tf" in required_columns
    assert "open" in required_columns
    assert "close" in required_columns
    assert "a" in required_columns
