from __future__ import annotations

from pathlib import Path

from research_core.release.draft import write_release_draft
from tests._release_helpers import init_release_fixture_repo


def test_release_draft_smoke(tmp_path: Path) -> None:
    repo_root = init_release_fixture_repo(tmp_path / "repo", ["phase16-v1.1-docs", "phase17-v1"])
    template_path = tmp_path / "RELEASE_TEMPLATE.md"
    template_path.write_text(
        "## Summary\n\n- \n\n## Tags / Anchors\n\n- \n",
        encoding="utf-8",
    )

    out_path = tmp_path / "release.md"
    path = write_release_draft(
        repo_root=repo_root,
        from_ref="phase16-v1.1-docs",
        to_ref="phase17-v1",
        out_path=out_path,
        template_path=template_path,
    )

    assert path.exists()
    payload = path.read_text(encoding="utf-8")
    assert "# phase17-v1 — Release" in payload
    assert "Release notes: phase16-v1.1-docs..phase17-v1" in payload
    assert "## Validation" in payload
    assert "- [ ] `pytest -q`" in payload
