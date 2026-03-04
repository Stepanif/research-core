# Baseline Discovery Spec v1

## Scope

Phase 11 Step 2 adds deterministic baseline discovery under an explicit baseline root. Discovery is file-only and does not search outside the provided root.

## Baseline Root Layout

```text
<baseline_root>/
  <runset_id>/
    baseline.card.json
    baseline.card.manifest.json
  baseline.index.json
  baseline.promotions.json
```

## Baseline ID

- `baseline_id` is `checksums.per_run_vector_sha256` from `baseline.card.json`.
- It is the content address for index and promotions entries.

## baseline.index.json (v1)

```json
{
  "index_version": "v1",
  "created_utc": "<RESEARCH_CREATED_UTC>",
  "runsets": {
    "<runset_id>": {
      "baseline_id": "<per_run_vector_sha256>",
      "card_sha256": "<sha256 bytes of baseline.card.json>",
      "manifest_canonical_sha256": "<canonical hash of baseline.card.manifest.json>",
      "path": "<runset_id>/baseline.card.json"
    }
  }
}
```

Rules:
- Runset keys are sorted.
- Refresh scans only direct runset directories under `baseline_root`.
- If an existing index entry for a discovered runset has a different `baseline_id` than disk, refresh fails loud.

## baseline.promotions.json (v1)

```json
{
  "promotions_version": "v1",
  "created_utc": "<RESEARCH_CREATED_UTC>",
  "labels": {
    "<label>": {
      "<runset_id>": "<baseline_id>"
    }
  }
}
```

Rules:
- Label keys are sorted; per-label runset keys are sorted.
- Immutability: existing `(label, runset_id)` cannot be remapped to a different `baseline_id`.
- Promoting the same value is a no-op success.

## Resolution Rules

`baseline resolve --root <baseline_root> --runset <runset_id> [--label <label>]`

- Requires `<baseline_root>/<runset_id>/baseline.card.json`.
- If `baseline.index.json` exists, the runset entry must exist and match on-disk `baseline_id`.
- With `--label`:
  - requires promotions mapping for `(label, runset_id)`.
  - mapped `baseline_id` must match on-disk baseline.
- Without `--label`:
  - default label priority is fixed: `prod`, then `baseline`.
  - if no matching promotion exists, falls back to on-disk baseline card.

## Risk Wrapper

`risk diff-runset --root <baseline_root> --a <runset_id> --b <runset_id> [--label-a <label>] [--label-b <label>] --out <dir>`

- Resolves baseline cards through deterministic rules above.
- Delegates to existing `risk diff` writer path.
- Produces identical output contract to `risk diff`.
