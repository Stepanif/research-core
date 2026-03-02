from __future__ import annotations

from dataclasses import dataclass

from research_core.doctor.contracts import SECTION_ORDER


@dataclass(frozen=True)
class CheckItem:
    check_id: str
    ok: bool
    detail: str


def _sorted_checks(checks: list[CheckItem]) -> list[CheckItem]:
    return sorted(checks, key=lambda item: item.check_id)


def render_doctor_text(
    input_lines: list[str],
    required: list[CheckItem],
    hash_integrity: list[CheckItem],
    invariants: list[CheckItem],
    optionals: list[CheckItem],
    result: list[CheckItem],
) -> str:
    sections = {
        "INPUT": [CheckItem(check_id=line, ok=True, detail="") for line in sorted(input_lines)],
        "REQUIRED FILES": _sorted_checks(required),
        "HASH INTEGRITY": _sorted_checks(hash_integrity),
        "INVARIANTS": _sorted_checks(invariants),
        "OPTIONALS": _sorted_checks(optionals),
        "RESULT": _sorted_checks(result),
    }

    lines: list[str] = ["RESEARCH DOCTOR v1"]
    for section_name in SECTION_ORDER:
        lines.append(section_name)
        section_items = sections.get(section_name, [])
        if not section_items:
            lines.append("- none")
            continue

        for item in section_items:
            if section_name == "INPUT":
                lines.append(f"- {item.check_id}")
                continue
            status = "OK" if item.ok else "FAIL"
            if item.detail:
                lines.append(f"- {item.check_id} [{status}] {item.detail}")
            else:
                lines.append(f"- {item.check_id} [{status}]")

    return "\n".join(lines)
