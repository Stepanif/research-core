# Prune Spec v1

## Purpose

`prune` manages artifact retention deterministically while preserving audit and immutability anchors.

## Commands

```text
prune run --run <run_dir> --policy <policy.json> [--dry-run] [--confirm <plan_sha256>]
prune out --root <exec_outputs_root> --policy <policy.json> [--dry-run] [--confirm <plan_sha256>]
```

## Policy (`policy.json`) v1

Required fields:
- `policy_version: "v1"`
- `keep.manifests: true`
- `keep.contracts`
- `keep.goldens`
- `keep.baselines.promoted_only: true`
- `keep.baselines.keep_index: true`
- `delete.run_intermediates`
- `delete.plan_logs.keep_latest_n`
- `safety.require_dry_run_first: true`
- `safety.refuse_if_unrecognized_paths: true`

Optional:
- `keep.ci_outputs.keep_latest_n`

## Deterministic Output

Both dry-run and execute print deterministic text:
- `PRUNE v1`
- `INPUT`
- `POLICY SUMMARY`
- `PROTECTED PATHS`
- `DELETE CANDIDATES` (sorted, with bytes)
- `TOTALS`
- `RESULT: DRY_RUN` or `RESULT: EXECUTED`

The report includes `plan_sha256`, which is used as `--confirm` token for execute when dry-run-first safety is enabled.

## Protected Artifacts (v1)

Never deleted:
- `*.manifest.json`
- `*.contract.json` when `keep.contracts=true`
- baseline indexes/promotions
- promoted baseline card + manifest referenced by `baseline.promotions.json`
- `dataset_to_runs.index.json`
- runset catalog index + entries
- `projects.index.json` and `projects.promotions.json`
- `ci.summary.json` and `ci.summary.manifest.json`
- doctor/verify outputs (audit)

## Deletable Targets (v1)

If enabled and not protected:
- run intermediates under `experiments/batches`, `observe`, `risk`
- log files under `logs/*.log` except latest N by deterministic path ordering

Planner is deterministic and fail-loud on unsafe ambiguity (for example, promotions pointing to missing/mismatched baseline cards).
