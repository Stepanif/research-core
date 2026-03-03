from __future__ import annotations

from pathlib import Path

import research_core.release.url as release_url


class _Result:
    def __init__(self, stdout: str) -> None:
        self.stdout = stdout


def test_release_url_parsing_https(monkeypatch: object) -> None:
    def _fake_run(*_: object, **__: object) -> _Result:
        return _Result("https://github.com/OWNER/REPO.git\n")

    monkeypatch.setattr(release_url.subprocess, "run", _fake_run)
    url = release_url.build_new_release_url(repo_root=Path("."), tag="phase17-v1")
    assert url == "https://github.com/OWNER/REPO/releases/new?tag=phase17-v1"


def test_release_url_parsing_ssh(monkeypatch: object) -> None:
    def _fake_run(*_: object, **__: object) -> _Result:
        return _Result("git@github.com:OWNER/REPO.git\n")

    monkeypatch.setattr(release_url.subprocess, "run", _fake_run)
    url = release_url.build_new_release_url(repo_root=Path("."), tag="phase17-v1")
    assert url == "https://github.com/OWNER/REPO/releases/new?tag=phase17-v1"
