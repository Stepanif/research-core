from __future__ import annotations

from pathlib import Path

from research_core.release.contracts import RELEASE_NOTES_ALLOWED_FORMATS, RELEASE_NOTES_DEFAULT_FORMAT
from research_core.release.io import list_commit_subjects, resolve_commit
from research_core.util.types import ValidationError


def generate_release_notes(*, repo_root: Path, from_ref: str, to_ref: str, output_format: str = RELEASE_NOTES_DEFAULT_FORMAT) -> str:
    if output_format not in RELEASE_NOTES_ALLOWED_FORMATS:
        raise ValidationError(f"Unsupported release notes format: {output_format}")
    if not isinstance(from_ref, str) or not from_ref:
        raise ValidationError("release notes requires --from")
    if not isinstance(to_ref, str) or not to_ref:
        raise ValidationError("release notes requires --to")

    from_sha = resolve_commit(repo_root, from_ref)
    to_sha = resolve_commit(repo_root, to_ref)
    commits = list_commit_subjects(repo_root, from_sha, to_sha)

    header = f"Release notes: {from_ref}..{to_ref}"
    if output_format == "text":
        body = [subject for _, subject in commits]
    else:
        body = [f"- {subject}" for _, subject in commits]

    if not body:
        if output_format == "text":
            body = ["(no commits)"]
        else:
            body = ["- (no commits)"]

    return "\n".join([header, "", *body]) + "\n"
