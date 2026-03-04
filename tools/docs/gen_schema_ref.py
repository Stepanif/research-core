from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "docs" / "reference" / "schemas"
SKIP_DIR_NAMES = {".git", ".venv", "site", "node_modules", "__pycache__"}


def _iter_schema_files() -> list[Path]:
    schema_paths: list[Path] = []
    for path in ROOT.rglob("*.schema*.json"):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        schema_paths.append(path)
    return sorted(schema_paths, key=lambda path: path.relative_to(ROOT).as_posix())


def _format_type(raw_type: object, prop: dict[str, object]) -> str:
    if isinstance(raw_type, str):
        return raw_type
    if isinstance(raw_type, list):
        return ", ".join(str(item) for item in sorted(raw_type, key=str))
    if "enum" in prop and isinstance(prop["enum"], list):
        return "enum"
    if "oneOf" in prop:
        return "oneOf"
    if "anyOf" in prop:
        return "anyOf"
    return "unknown"


def _escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def _build_schema_page(schema_path: Path, data: dict[str, object]) -> str:
    title = str(data.get("title") or schema_path.stem)
    description = str(data.get("description") or "TODO: Description not found in schema source.")
    required_list = data.get("required") if isinstance(data.get("required"), list) else []
    required_set = {str(item) for item in required_list}
    properties = data.get("properties") if isinstance(data.get("properties"), dict) else {}

    lines = [f"# {title}", "", description, "", "## Required Fields", ""]

    if required_list:
        for field_name in sorted(str(item) for item in required_list):
            lines.append(f"- `{field_name}`")
    else:
        lines.append("None")

    lines.extend(["", "## Properties", "", "| Name | Type | Required? | Description |", "|---|---|---|---|"])

    if properties:
        for prop_name in sorted(str(name) for name in properties.keys()):
            prop_value = properties.get(prop_name)
            prop = prop_value if isinstance(prop_value, dict) else {}
            prop_type = _format_type(prop.get("type"), prop)
            is_required = "yes" if prop_name in required_set else "no"
            prop_description = str(prop.get("description") or "")
            lines.append(
                "| "
                + _escape_cell(prop_name)
                + " | "
                + _escape_cell(prop_type)
                + " | "
                + is_required
                + " | "
                + _escape_cell(prop_description)
                + " |"
            )
    else:
        lines.append("| (none) | - | - | No properties found. |")

    lines.append("")
    return "\n".join(lines)


def _unique_output_name(schema_path: Path, used: set[str]) -> str:
    base = schema_path.stem
    if base not in used:
        used.add(base)
        return base

    relative_slug = schema_path.relative_to(ROOT).as_posix().replace("/", "__")
    normalized = relative_slug[:-5] if relative_slug.endswith(".json") else relative_slug
    candidate = normalized
    index = 2
    while candidate in used:
        candidate = f"{normalized}__{index}"
        index += 1
    used.add(candidate)
    return candidate


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    used_names: set[str] = set()
    generated: list[tuple[str, str, str]] = []

    for schema_path in _iter_schema_files():
        try:
            data = json.loads(schema_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            print(f"WARN: skipping {schema_path.relative_to(ROOT).as_posix()} (invalid JSON)")
            continue

        if not isinstance(data, dict):
            print(f"WARN: skipping {schema_path.relative_to(ROOT).as_posix()} (JSON root is not an object)")
            continue

        out_name = _unique_output_name(schema_path, used_names)
        title = str(data.get("title") or schema_path.stem)
        page = _build_schema_page(schema_path, data)
        (OUT_DIR / f"{out_name}.md").write_text(page, encoding="utf-8")

        generated.append((title, out_name, schema_path.relative_to(ROOT).as_posix()))

    lines = ["# Schema Reference", ""]
    if not generated:
        lines.append("TODO: No schema reference pages were generated. Verify schema files.")
    else:
        for title, out_name, relative_source in sorted(generated, key=lambda item: item[2]):
            lines.append(f"- [{title}]({out_name}.md) — source: `{relative_source}`")
    lines.append("")
    (OUT_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
