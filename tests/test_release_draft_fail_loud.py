from __future__ import annotations

from pathlib import Path

import pytest

from research_core.release.draft import write_release_draft
from research_core.release.url import build_new_release_url
from research_core.util.types import ValidationError


def test_release_url_missing_origin_fail_loud(monkeypatch: object) -> None:
    import research_core.release.url as release_url

    def _fake_run(*_: object, **__: object) -> object:
        raise release_url.subprocess.CalledProcessError(returncode=1, cmd=["git", "config"], stderr="no origin")

    monkeypatch.setattr(release_url.subprocess, "run", _fake_run)

    with pytest.raises(ValidationError):
        build_new_release_url(repo_root=Path("."), tag="phase17-v1")


def test_release_draft_missing_template_fail_loud(tmp_path: Path) -> None:
    with pytest.raises(ValidationError):
        write_release_draft(
            repo_root=Path(__file__).parent.parent,
            from_ref="phase16-v1.1-docs",
            to_ref="phase17-v1",
            out_path=tmp_path / "release.md",
            template_path=tmp_path / "missing.md",
        )
