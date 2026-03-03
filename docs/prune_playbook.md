# Prune Operator Playbook v1

## Purpose

`prune` is a deterministic retention tool for controlling artifact growth while preserving auditability and immutability anchors.

At a high level, operators should treat `prune` as **plan-first, execute-second**.

What `prune` will never delete in v1:
- manifest artifacts (`*.manifest.json`)
- baseline index/promotions anchors (`baseline.index.json`, `baseline.promotions.json`)
- promoted baseline card + manifest referenced by promotions
- lineage links (`dataset_to_runs.index.json`)
- runset catalog index + entries
- project indexes/promotions (`projects.index.json`, `projects.promotions.json`)

## Quickstart

1. Run dry-run first and capture `plan_sha256`.
2. Review protected count, candidate list, and totals.
3. Execute with `--confirm <plan_sha256>`.

Dry-run:

```text
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_default.json --dry-run
```

Execute:

```text
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_default.json --confirm <plan_sha256>
```

## Policy files

Prune policy JSON must conform to:

```text
schemas/prune.policy.schema.v1.json
```

Use examples:
- `docs/examples/prune_policy_default.json`
- `docs/examples/prune_policy_aggressive.json`

## Protected artifacts

Protected sets include:
- baseline promotions/index and promoted baseline artifacts
- manifest files and contract files (when keep policy enables them)
- lineage links (`catalog/links/dataset_to_runs.index.json`)
- runset catalog (`runsets.index.json`, `runsets/entries/*.json`)
- project index/promotions
- CI summaries/manifests when present in prune root

If a directory contains protected files, v1 planning avoids unsafe directory deletion and only proposes safe file-level candidates.

## Interpreting output

Prune report is deterministic text with sections:
- `PRUNE v1`
- `INPUT`
- `POLICY SUMMARY`
- `PROTECTED PATHS`
- `DELETE CANDIDATES`
- `TOTALS`
- `RESULT: DRY_RUN|EXECUTED`

`plan_sha256` is the execution confirmation token when dry-run-first safety is enabled.

## Common failures

- **Confirm hash mismatch**
  - Cause: `--confirm` does not match current computed plan hash.
  - Action: rerun dry-run and use the latest printed `plan_sha256`.

- **Attempt to delete protected path**
  - Cause: candidate overlaps protected artifact set.
  - Action: adjust policy scope/root; do not bypass protections.

- **Unrecognized paths refusal**
  - Cause: safety policy rejects unexpected candidate classes.
  - Action: inspect root layout and narrow prune target.

- **Baseline promotions guard failures**
  - Cause: promotions reference missing or mismatched baseline card/manifests.
  - Action: repair baseline root integrity before pruning.

## Recommended operational cadence

- **Weekly**: dry-run review on active environments.
- **Monthly**: execute with confirmed plan hash after review.
- Keep cadence deterministic by using stable policy files and explicit roots.

## Example commands

### PowerShell

```powershell
python -m research_core.cli prune run --run exec_outputs/run_001 --policy docs/examples/prune_policy_default.json --dry-run
python -m research_core.cli prune run --run exec_outputs/run_001 --policy docs/examples/prune_policy_default.json --confirm <plan_sha256>
```

```powershell
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_aggressive.json --dry-run
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_aggressive.json --confirm <plan_sha256>
```

### Bash

```bash
python -m research_core.cli prune run --run exec_outputs/run_001 --policy docs/examples/prune_policy_default.json --dry-run
python -m research_core.cli prune run --run exec_outputs/run_001 --policy docs/examples/prune_policy_default.json --confirm <plan_sha256>
```

```bash
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_aggressive.json --dry-run
python -m research_core.cli prune out --root exec_outputs --policy docs/examples/prune_policy_aggressive.json --confirm <plan_sha256>
```
