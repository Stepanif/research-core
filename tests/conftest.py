from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def _pin_build_metadata(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setenv("RESEARCH_GIT_COMMIT", "TEST")
