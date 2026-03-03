from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.doctor.bundle_verify import verify_bundle_text
from research_core.runsets.catalog import validate_runset
from research_core.runsets.io import canonical_hash
from research_core.util.hashing import sha256_file
from research_core.util.types import ValidationError

from research_core.ci_doctor.io import read_json_object


def _failure(check: str, detail: str, runset_id: str | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "check": check,
        "detail": detail,
    }
    if isinstance(runset_id, str) and runset_id:
        payload["runset_id"] = runset_id
    return payload


def _check_baseline_root(*, baseline_root: Path, runset_ids: list[str]) -> tuple[bool, list[dict[str, Any]], list[Path]]:
    failures: list[dict[str, Any]] = []
    inputs: list[Path] = []

    index_path = baseline_root / "baseline.index.json"
    promotions_path = baseline_root / "baseline.promotions.json"
    if not index_path.exists() or not index_path.is_file():
        failures.append(_failure("verify_baseline_root", f"Missing baseline index: {index_path}"))
        return False, failures, inputs
    if not promotions_path.exists() or not promotions_path.is_file():
        failures.append(_failure("verify_baseline_root", f"Missing baseline promotions: {promotions_path}"))
        return False, failures, inputs

    index_payload = read_json_object(index_path, name="baseline index")
    promotions_payload = read_json_object(promotions_path, name="baseline promotions")
    if index_payload.get("index_version") != "v1":
        failures.append(_failure("verify_baseline_root", "Unsupported baseline index version"))
    if promotions_payload.get("promotions_version") != "v1":
        failures.append(_failure("verify_baseline_root", "Unsupported baseline promotions version"))

    runsets_block = index_payload.get("runsets")
    if not isinstance(runsets_block, dict):
        failures.append(_failure("verify_baseline_root", "Invalid baseline index runsets block"))
        runsets_block = {}

    inputs.extend([index_path, promotions_path])

    for runset_id in runset_ids:
        card_path = baseline_root / runset_id / "baseline.card.json"
        manifest_path = baseline_root / runset_id / "baseline.card.manifest.json"
        if not card_path.exists() or not card_path.is_file():
            failures.append(_failure("verify_baseline_root", f"Missing baseline card: {card_path}", runset_id))
            continue
        if not manifest_path.exists() or not manifest_path.is_file():
            failures.append(_failure("verify_baseline_root", f"Missing baseline card manifest: {manifest_path}", runset_id))
            continue

        card_payload = read_json_object(card_path, name=f"baseline card for {runset_id}")
        manifest_payload = read_json_object(manifest_path, name=f"baseline card manifest for {runset_id}")
        checksums = card_payload.get("checksums")
        if not isinstance(checksums, dict):
            failures.append(_failure("verify_baseline_root", "Invalid checksums block in baseline card", runset_id))
            continue

        baseline_id = checksums.get("per_run_vector_sha256")
        if not isinstance(baseline_id, str) or not baseline_id:
            failures.append(_failure("verify_baseline_root", "Missing checksums.per_run_vector_sha256", runset_id))
            continue

        index_entry = runsets_block.get(runset_id)
        if isinstance(index_entry, dict):
            indexed_baseline_id = index_entry.get("baseline_id")
            if isinstance(indexed_baseline_id, str) and indexed_baseline_id != baseline_id:
                failures.append(
                    _failure(
                        "verify_baseline_root",
                        f"baseline_id mismatch (index={indexed_baseline_id}, card={baseline_id})",
                        runset_id,
                    )
                )

            expected_manifest_hash = index_entry.get("manifest_canonical_sha256")
            actual_manifest_hash = canonical_hash(manifest_payload, self_field="baseline_card_manifest_canonical_sha256")
            if isinstance(expected_manifest_hash, str) and expected_manifest_hash and expected_manifest_hash != actual_manifest_hash:
                failures.append(
                    _failure(
                        "verify_baseline_root",
                        f"manifest hash mismatch (index={expected_manifest_hash}, actual={actual_manifest_hash})",
                        runset_id,
                    )
                )

        inputs.extend([card_path, manifest_path])

    return len(failures) == 0, failures, sorted(set(path.resolve() for path in inputs), key=lambda p: p.as_posix())


def _check_promotions(*, baseline_root: Path, runset_ids: list[str], label: str) -> tuple[bool, list[dict[str, Any]], list[Path]]:
    failures: list[dict[str, Any]] = []
    inputs: list[Path] = []

    promotions_path = baseline_root / "baseline.promotions.json"
    if not promotions_path.exists() or not promotions_path.is_file():
        return False, [_failure("verify_promotions", f"Missing baseline promotions: {promotions_path}")], []

    promotions_payload = read_json_object(promotions_path, name="baseline promotions")
    labels = promotions_payload.get("labels")
    if not isinstance(labels, dict):
        return False, [_failure("verify_promotions", "Invalid promotions labels block")], [promotions_path]

    label_map = labels.get(label)
    if not isinstance(label_map, dict):
        return False, [_failure("verify_promotions", f"Missing promotions label mapping: {label}")], [promotions_path]

    inputs.append(promotions_path)

    for runset_id in runset_ids:
        mapped = label_map.get(runset_id)
        if not isinstance(mapped, str) or not mapped:
            failures.append(_failure("verify_promotions", f"Missing promotion for label={label}", runset_id))
            continue

        card_path = baseline_root / runset_id / "baseline.card.json"
        if not card_path.exists() or not card_path.is_file():
            failures.append(_failure("verify_promotions", f"Missing baseline card: {card_path}", runset_id))
            continue
        card_payload = read_json_object(card_path, name=f"baseline card for {runset_id}")
        checksums = card_payload.get("checksums")
        if not isinstance(checksums, dict):
            failures.append(_failure("verify_promotions", "Invalid checksums block in baseline card", runset_id))
            continue
        actual = checksums.get("per_run_vector_sha256")
        if mapped != actual:
            failures.append(
                _failure(
                    "verify_promotions",
                    f"Promotion baseline mismatch (promotion={mapped}, card={actual})",
                    runset_id,
                )
            )

        inputs.append(card_path)

    return len(failures) == 0, failures, sorted(set(path.resolve() for path in inputs), key=lambda p: p.as_posix())


def _check_runsets(*, catalog_dir: Path, runset_ids: list[str]) -> tuple[bool, list[dict[str, Any]], list[Path]]:
    failures: list[dict[str, Any]] = []
    inputs: list[Path] = []

    index_path = catalog_dir / "runsets" / "runsets.index.json"
    links_path = catalog_dir / "links" / "dataset_to_runs.index.json"
    if index_path.exists() and index_path.is_file():
        inputs.append(index_path)
    if links_path.exists() and links_path.is_file():
        inputs.append(links_path)

    for runset_id in runset_ids:
        entry_path = catalog_dir / "runsets" / "entries" / f"{runset_id}.json"
        if entry_path.exists() and entry_path.is_file():
            inputs.append(entry_path)
        ok, text = validate_runset(catalog_root=catalog_dir, runset_id=runset_id)
        if not ok:
            failures.append(_failure("verify_runsets", text, runset_id))

    return len(failures) == 0, failures, sorted(set(path.resolve() for path in inputs), key=lambda p: p.as_posix())


def _check_bundles(*, bundles: list[dict[str, Path]]) -> tuple[bool, list[dict[str, Any]], list[Path]]:
    failures: list[dict[str, Any]] = []
    inputs: list[Path] = []

    for item in bundles:
        zip_path = item["zip"]
        inputs.append(zip_path)
        text, ok = verify_bundle_text(zip_path)
        if not ok:
            failures.append(_failure("verify_bundles", text.strip() or f"Bundle verify failed: {zip_path}"))

    return len(failures) == 0, failures, sorted(set(path.resolve() for path in inputs), key=lambda p: p.as_posix())


def _check_dashboard(*, summary_path: Path, manifest_path: Path) -> tuple[bool, list[dict[str, Any]], list[Path]]:
    failures: list[dict[str, Any]] = []
    inputs: list[Path] = [summary_path, manifest_path]

    if not summary_path.exists() or not summary_path.is_file():
        return False, [_failure("verify_dashboard", f"Missing dashboard summary: {summary_path}")], inputs
    if not manifest_path.exists() or not manifest_path.is_file():
        return False, [_failure("verify_dashboard", f"Missing dashboard manifest: {manifest_path}")], inputs

    manifest_payload = read_json_object(manifest_path, name="dashboard manifest")
    outputs = manifest_payload.get("outputs")
    if not isinstance(outputs, dict):
        failures.append(_failure("verify_dashboard", "Invalid dashboard manifest outputs block"))
    else:
        item = outputs.get("dashboard.summary.json")
        if not isinstance(item, dict):
            failures.append(_failure("verify_dashboard", "Missing outputs.dashboard.summary.json"))
        else:
            expected_sha = item.get("sha256")
            if isinstance(expected_sha, str) and expected_sha:
                actual_sha = sha256_file(summary_path)
                if expected_sha != actual_sha:
                    failures.append(
                        _failure(
                            "verify_dashboard",
                            f"Dashboard summary sha mismatch (manifest={expected_sha}, actual={actual_sha})",
                        )
                    )

    expected_manifest_hash = manifest_payload.get("dashboard_manifest_canonical_sha256")
    if isinstance(expected_manifest_hash, str) and expected_manifest_hash:
        actual_manifest_hash = canonical_hash(manifest_payload, self_field="dashboard_manifest_canonical_sha256")
        if expected_manifest_hash != actual_manifest_hash:
            failures.append(
                _failure(
                    "verify_dashboard",
                    f"Dashboard manifest canonical hash mismatch (manifest={expected_manifest_hash}, actual={actual_manifest_hash})",
                )
            )

    return len(failures) == 0, failures, sorted(set(path.resolve() for path in inputs), key=lambda p: p.as_posix())


def run_ci_doctor_checks(*, config: dict[str, Any], runset_ids: list[str]) -> dict[str, Any]:
    checks_cfg = config["checks"]
    failures: list[dict[str, Any]] = []
    inputs: list[Path] = []

    baseline_ok = True
    promotions_ok = True
    runsets_ok = True
    bundles_ok: bool | None = None
    dashboard_ok: bool | None = None

    if checks_cfg["verify_baseline_root"]:
        baseline_ok, errs, check_inputs = _check_baseline_root(baseline_root=config["baseline_root"], runset_ids=runset_ids)
        failures.extend(errs)
        inputs.extend(check_inputs)

    if checks_cfg["verify_promotions"]:
        promotions_ok, errs, check_inputs = _check_promotions(
            baseline_root=config["baseline_root"],
            runset_ids=runset_ids,
            label=config["label"],
        )
        failures.extend(errs)
        inputs.extend(check_inputs)

    if checks_cfg["verify_runsets"]:
        runsets_ok, errs, check_inputs = _check_runsets(catalog_dir=config["catalog_dir"], runset_ids=runset_ids)
        failures.extend(errs)
        inputs.extend(check_inputs)

    if checks_cfg["verify_bundles"]:
        bundles_ok, errs, check_inputs = _check_bundles(bundles=config["bundles"])
        failures.extend(errs)
        inputs.extend(check_inputs)

    if checks_cfg["verify_dashboard"]:
        dashboard_cfg = config["dashboard"]
        if not isinstance(dashboard_cfg, dict):
            failures.append(_failure("verify_dashboard", "Dashboard configuration is required when verify_dashboard=true"))
            dashboard_ok = False
        else:
            dashboard_ok, errs, check_inputs = _check_dashboard(
                summary_path=dashboard_cfg["summary_path"],
                manifest_path=dashboard_cfg["manifest_path"],
            )
            failures.extend(errs)
            inputs.extend(check_inputs)

    failures_sorted = sorted(
        failures,
        key=lambda item: (
            str(item.get("check", "")),
            str(item.get("runset_id", "")),
            str(item.get("detail", "")),
        ),
    )

    status = "PASS" if not failures_sorted else "FAIL"

    return {
        "status": status,
        "failures": failures_sorted,
        "checks": {
            "baseline_root_ok": baseline_ok,
            "promotions_ok": promotions_ok,
            "runsets_ok": runsets_ok,
            "bundles_ok": bundles_ok,
            "dashboard_ok": dashboard_ok,
        },
        "inputs": sorted(set(path.resolve() for path in inputs), key=lambda p: p.as_posix()),
    }
