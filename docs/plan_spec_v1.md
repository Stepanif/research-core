# Plan Spec v1

## Purpose
Plan v1 provides deterministic task enumeration and parallel execution orchestration without changing canon/psa/observe/experiment/project semantics.

## Schema
File: `schemas/plan.schema.v1.json`

Top-level fields:
- `plan_version`: `"v1"`
- `created_utc`: required from `RESEARCH_CREATED_UTC`
- `project_id`: hash-derived from canonical project payload using existing project-id logic
- `tasks`: sorted deterministic task list

Task fields:
- `task_id`
- `kind` (`"experiment_batch"` only in v1)
- `run_dir`
- `spec_dir`
- `out_dir`
- `argv`
- `deps` (empty list in v1)
- `expected_outputs` (sorted run-relative paths)

## Hashing Rules
Task id is canonical JSON hash of task object excluding `task_id`:

`sha256(json.dumps(task_obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))`

Plan JSON is written as canonical bytes:

`json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\\n"`

## Determinism Rules
- `plan build` requires `RESEARCH_CREATED_UTC`; fail-loud when missing.
- Task ordering is stable: sort by `run_dir`, then `spec_dir`, then `task_id`.
- Batch output directory uses deterministic hash-derived batch id:
  `<run_dir>/experiments/batches/<batch_id>/`
- Spec listing used in batch id is lexicographically sorted by filename.
- No filesystem enumeration without explicit sorting.

## Execution Rules
- `plan execute --jobs N` runs tasks with max `N` workers.
- `plan execute` always runs deterministic preflight before launching tasks.
- Subprocess working directory is fixed to repository root.
- Environment passed to each subprocess includes required `RESEARCH_CREATED_UTC`.
- Per-task logs are deterministic files:
  - `<plan_dir>/logs/<task_id>.stdout.log`
  - `<plan_dir>/logs/<task_id>.stderr.log`
- No stdout/stderr streaming from running tasks; logs only.
- After each successful task, verify `expected_outputs` exist.
- Fail-loud:
  - on first failure, stop launching new tasks
  - wait for currently running tasks to complete
  - exit non-zero

### Preflight Statuses
For each task in deterministic `task_id` order:
- `READY`: `out_dir` does not exist
- `EXISTS_COMPLETE`: `out_dir` exists and all `expected_outputs` exist
- `EXISTS_INCOMPLETE`: `out_dir` exists but one or more `expected_outputs` are missing

Default mode (no flags):
- If any task is `EXISTS_COMPLETE` or `EXISTS_INCOMPLETE`, execution fails before launching tasks.

`--allow-existing` mode:
- `EXISTS_COMPLETE` tasks are skipped and reported as `SKIP_EXISTS`.
- `EXISTS_INCOMPLETE` still fails before launch.
- `READY` tasks run normally and report `RUN_OK` or `RUN_FAIL`.
