# Prune Runs Safely

Pruning is destructive. Use the plan-first workflow below every time.

## Truth sources

- [Prune Spec v1](../reference/contracts/v1/prune_spec_v1.md)
- [Prune Operator Playbook v1](../prune_playbook.md)

## How pruning works in this repo

Supported commands from contract + CLI help:

```text
prune run --run <run_dir> --policy <policy.json> [--dry-run] [--confirm <plan_sha256>]
prune out --root <exec_outputs_root> --policy <policy.json> [--dry-run] [--confirm <plan_sha256>]
```

CLI options (from `python -m research_core.cli prune run --help` and
`python -m research_core.cli prune out --help`) confirm:

- `prune run`: `--run`, `--policy`, optional `--dry-run`, optional `--confirm`
- `prune out`: `--root`, `--policy`, optional `--dry-run`, optional `--confirm`

Policy file requirements (`policy.json`) from spec:

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
- Optional: `keep.ci_outputs.keep_latest_n`

## Safe procedure

### 1. Identify target scope

Choose one scope:

- Single run directory with `prune run --run <run_dir> ...`
- Output root with `prune out --root <exec_outputs_root> ...`

Playbook examples use `exec_outputs` as prune root.

### 2. Dry-run first (required by policy safety)

PowerShell examples:

```powershell
python -m research_core.cli prune run --run exec_outputs/run_001 --policy docs/examples/prune_policy_default.json --dry-run
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_default.json --dry-run
```

Dry-run output is deterministic and includes `plan_sha256`.

### 3. Apply with explicit confirm token

Use the `plan_sha256` from the dry-run report:

```powershell
python -m research_core.cli prune run --run exec_outputs/run_001 --policy docs/examples/prune_policy_default.json --confirm <plan_sha256>
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_default.json --confirm <plan_sha256>
```

### 4. Verify protected outputs remain

From `Prune Spec v1`, these are protected and must remain:

- `*.manifest.json`
- `*.contract.json` when `keep.contracts=true`
- baseline indexes/promotions
- promoted baseline card + manifest referenced by `baseline.promotions.json`
- `dataset_to_runs.index.json`
- runset catalog index + entries
- `projects.index.json` and `projects.promotions.json`
- `ci.summary.json` and `ci.summary.manifest.json`
- doctor/verify outputs (audit)

## Recovery / audit

The prune contract defines deterministic report sections in dry-run and execute:

- `PRUNE v1`
- `INPUT`
- `POLICY SUMMARY`
- `PROTECTED PATHS`
- `DELETE CANDIDATES`
- `TOTALS`
- `RESULT: DRY_RUN` or `RESULT: EXECUTED`

Use that output as your audit trail, including `plan_sha256`.

## Do not prune these

Never prune protected artifacts listed in `Prune Spec v1`:

- Manifest and contract anchors (`*.manifest.json`, contract files when enabled)
- Baseline promotion/index anchors and promoted baseline artifacts
- Lineage and runset indexes/entries
- Project indexes/promotions
- CI/doctor audit outputs
