from __future__ import annotations

from pathlib import Path

from research_core.release.notes import generate_release_notes
from research_core.util.io import ensure_dir
from research_core.util.types import ValidationError


_TEMPLATE_TITLE_TOKEN = "{{TITLE}}"
_TEMPLATE_NOTES_TOKEN = "{{RELEASE_NOTES}}"
_TEMPLATE_VALIDATION_TOKEN = "{{VALIDATION_BLOCK}}"


def _validation_block() -> str:
    return "\n".join(
        [
            "## Validation",
            "",
            "- [ ] `pytest -q`",
            "- [ ] `pytest -q`",
            "",
        ]
    )


def _render_body(*, template: str, title: str, notes: str) -> str:
    body = template

    if _TEMPLATE_TITLE_TOKEN in body:
        body = body.replace(_TEMPLATE_TITLE_TOKEN, title)
    else:
        body = f"# {title}\n\n{body}"

    if _TEMPLATE_NOTES_TOKEN in body:
        body = body.replace(_TEMPLATE_NOTES_TOKEN, notes.rstrip("\n"))
    else:
        body = body.rstrip("\n") + "\n\n## Generated Notes\n\n" + notes.rstrip("\n") + "\n"

    validation = _validation_block().rstrip("\n")
    if _TEMPLATE_VALIDATION_TOKEN in body:
        body = body.replace(_TEMPLATE_VALIDATION_TOKEN, validation)
    elif "## Validation" not in body:
        body = body.rstrip("\n") + "\n\n" + validation + "\n"

    return body.rstrip("\n") + "\n"


def write_release_draft(
    *,
    repo_root: Path,
    from_ref: str,
    to_ref: str,
    out_path: Path,
    title: str | None = None,
    template_path: Path | None = None,
) -> Path:
    if not isinstance(from_ref, str) or not from_ref:
        raise ValidationError("release draft requires --from")
    if not isinstance(to_ref, str) or not to_ref:
        raise ValidationError("release draft requires --to")

    resolved_title = title if isinstance(title, str) and title else f"{to_ref} — Release"
    template_file = template_path if isinstance(template_path, Path) else repo_root / ".github" / "RELEASE_TEMPLATE.md"
    if not template_file.exists() or not template_file.is_file():
        raise ValidationError(f"Missing release template: {template_file}")

    template = template_file.read_text(encoding="utf-8")
    notes = generate_release_notes(repo_root=repo_root, from_ref=from_ref, to_ref=to_ref, output_format="markdown")
    body = _render_body(template=template, title=resolved_title, notes=notes)

    ensure_dir(out_path.parent)
    out_path.write_text(body, encoding="utf-8")
    return out_path
