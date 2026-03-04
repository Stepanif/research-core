from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT_DIR = ROOT / "docs" / "reference" / "artifacts"
CATALOG_PATH = ARTIFACT_DIR / "catalog.v1.yml"
GENERATED_NOTE = (
    "Generated from docs/reference/artifacts/catalog.v1.yml "
    "by tools/docs/gen_artifact_catalog.py"
)


def _normalize_text(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def _write_normalized(path: Path, content: str) -> None:
    path.write_text(_normalize_text(content) + "\n", encoding="utf-8", newline="\n")


def _load_catalog() -> list[dict[str, object]]:
    raw = yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("Catalog root must be a mapping.")
    stages = raw.get("stages")
    if not isinstance(stages, list):
        raise ValueError("Catalog must contain a 'stages' list.")
    normalized: list[dict[str, object]] = []
    for stage in stages:
        if isinstance(stage, dict):
            normalized.append(stage)
    return sorted(normalized, key=lambda item: str(item.get("stage") or ""))


def _render_schema_link(schema_value: str) -> str:
    if schema_value.startswith("TODO"):
        return schema_value
    return f"[{schema_value}]({schema_value})"


def _render_stage_page(stage: dict[str, object]) -> str:
    stage_key = str(stage.get("stage") or "TODO: stage")
    stage_name = str(stage.get("name") or stage_key)
    outputs = stage.get("outputs") if isinstance(stage.get("outputs"), list) else []
    tools = stage.get("tools") if isinstance(stage.get("tools"), list) else []
    todos = stage.get("todos") if isinstance(stage.get("todos"), list) else []

    lines = [f"# {stage_name}", "", GENERATED_NOTE, "", f"- Stage Key: `{stage_key}`"]

    if tools:
        lines.append("- Tools:")
        for tool in tools:
            if isinstance(tool, dict):
                cli_value = str(tool.get("cli") or "TODO: missing tool")
                lines.append(f"  - `{cli_value}`")

    lines.extend([
        "",
        "## Outputs",
        "",
        "| Output ID | Path Template | Type | Schema | Description |",
        "|---|---|---|---|---|",
    ])

    if outputs:
        output_dicts = [item for item in outputs if isinstance(item, dict)]
        for output in sorted(output_dicts, key=lambda item: str(item.get("id") or "")):
            output_id = str(output.get("id") or "TODO")
            path_template = str(output.get("path_template") or "TODO")
            output_type = str(output.get("type") or "TODO")
            schema = _render_schema_link(str(output.get("schema") or "TODO"))
            description = str(output.get("description") or "TODO")
            lines.append(
                "| "
                + output_id.replace("|", "\\|")
                + " | "
                + path_template.replace("|", "\\|")
                + " | "
                + output_type.replace("|", "\\|")
                + " | "
                + schema.replace("|", "\\|")
                + " | "
                + description.replace("|", "\\|")
                + " |"
            )
    else:
        lines.append("| TODO | TODO | TODO | TODO | TODO: No confirmed outputs added yet. |")

    for output in sorted((item for item in outputs if isinstance(item, dict)), key=lambda item: str(item.get("id") or "")):
        output_id = str(output.get("id") or "TODO")
        invariants = output.get("invariants") if isinstance(output.get("invariants"), list) else []
        verification = output.get("verification") if isinstance(output.get("verification"), list) else []
        if invariants:
            lines.extend(["", f"## Invariants: {output_id}", ""])
            for item in invariants:
                lines.append(f"- {str(item)}")
        if verification:
            lines.extend(["", f"## Verification: {output_id}", ""])
            for item in verification:
                lines.append(f"- {str(item)}")

    if todos:
        lines.extend(["", "## TODO", ""])
        for item in todos:
            lines.append(f"- {str(item)}")

    return "\n".join(lines)


def _render_index(stages: list[dict[str, object]]) -> str:
    lines = ["# Artifacts Reference", "", GENERATED_NOTE, "", "| Stage | Name | Outputs | Page |", "|---|---|---:|---|"]
    for stage in stages:
        stage_key = str(stage.get("stage") or "TODO")
        stage_name = str(stage.get("name") or stage_key)
        outputs = stage.get("outputs") if isinstance(stage.get("outputs"), list) else []
        output_count = len([item for item in outputs if isinstance(item, dict)])
        lines.append(f"| `{stage_key}` | {stage_name} | {output_count} | [{stage_key}.md]({stage_key}.md) |")
    return "\n".join(lines)


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    stages = _load_catalog()

    for stage in stages:
        stage_key = str(stage.get("stage") or "")
        if not stage_key:
            continue
        _write_normalized(ARTIFACT_DIR / f"{stage_key}.md", _render_stage_page(stage))

    _write_normalized(ARTIFACT_DIR / "index.md", _render_index(stages))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
