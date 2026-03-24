# ResearchCore

ResearchCore is a validation-first research lab built to force candidate logic through reproducible evidence before it earns trust. It is modular research infrastructure with a current proving ground in market-system logic, spanning everything from small labels and formulas to larger state-machine and experiment-driven workflows.

The point is not to decorate ideas with better language. The point is to push them through canonical data, artifact generation, validation, analysis, and comparison until they either survive cross-checking or fail cleanly. ResearchCore exists because that standard was hard to find in existing tools, and because building it became part of learning how to use AI-assisted tools to reach beyond solo-builder limits without lowering the bar for rigor.

## Why ResearchCore exists

ResearchCore exists to close the gap between intuition and evidence. I wanted a serious way to test my own logic, but the available tools were too weak, too expensive, too generic, or too misaligned with the kind of workflow I actually needed. This repo is the result: a lab for turning candidate logic into something concrete enough to validate, compare, reject, or keep.

That need shaped the project from the beginning. ResearchCore is not built to reward narrative confidence, aesthetic outputs, or vague “it looks promising” conclusions. It is built to expose bugs, weak assumptions, bad data, hidden drift, and false positives before they harden into belief. If an idea survives that process, it earns more than enthusiasm — it earns evidence.

## What enters the lab

ResearchCore is designed to accept logic at multiple scales.

Small units can include:
- labels
- formulas
- feature transforms
- simple measurements such as change in volume
- bar-level or sequence-level annotations

Larger units can include:
- rule sets
- experiment configurations
- state-transition systems
- model-based logic
- extraction logic for candidate setups
- downstream harness and profiling workflows

The point is to make candidate logic testable without requiring everything to begin as a full strategy.

## The research pathway

ResearchCore is organized around a pathway rather than a single command.

`logic -> canonical data -> artifacts -> validation -> analysis -> comparison -> extraction -> harness -> optimization`

### 1. Logic
A candidate idea enters the lab as something explicit enough to run: a label, formula, rule set, state machine, experiment definition, or other structured logic component.

### 2. Canonical data
Inputs are pushed onto canonicalized data so that downstream outputs are traceable and comparable. The goal is to remove ambiguity about what data a result actually came from.

### 3. Artifacts
Runs produce structured artifacts rather than just terminal output: manifests, summaries, reports, bundles, indexes, dashboards, and other machine-checkable outputs.

### 4. Validation
Artifacts are checked for reproducibility, drift, schema consistency, and other forms of integrity. This is where attractive outputs start earning or losing trust.

### 5. Analysis
Results are examined in a structured way rather than treated as self-explanatory. The goal is to understand what happened, not just whether a number looks good.

### 6. Comparison
Candidate logic is compared against baselines, alternate runs, prior artifacts, and expected outputs. This is where false confidence tends to get exposed.

### 7. Extraction
Promising structure can be extracted into more focused components, candidate trade setups, or downstream research objects.

### 8. Harness
Extracted logic can be run through more explicit testing and evaluation harnesses.

### 9. Optimization
Only after the earlier stages are credible does optimization become meaningful.

## Outputs

ResearchCore is built to produce outputs that can be inspected, compared, and revisited.

Canonical output types include:
- reports
- summaries
- dashboards
- manifests
- bundles
- comparisons against baselines
- validated experiment records
- decision-support artifacts

The lab is meant to leave a trail. The artifact history matters as much as the final result.

## Validation standard

Validation is the governing law of ResearchCore. Attractive outputs are not enough. “Fire” results are not enough. If a result cannot be reproduced, cross-checked, and traced back through the data, artifacts, and workflow that produced it, it does not count as real.

That standard shapes the entire lab. Logic is pushed through canonical data, deterministic workflows, explicit artifacts, drift checks, comparisons, and downstream evaluation before it is allowed to claim credibility. The goal is not to produce impressive-looking results quickly. The goal is to make candidate logic earn trust slowly, visibly, and under conditions that make failure obvious.

**Nothing counts as real in ResearchCore until the results can be cross-checked and validated.**

## Repository structure

ResearchCore is infrastructure-first. The repo is organized around workflows, contracts, artifacts, and validation rather than a single monolithic application.

Important surfaces currently include:
- `src/research_core/` — core implementation
- `.github/workflows/` — CI and docs workflows
- `tools/docs/` — documentation generators and verification tools
- `docs/` — user-facing and generated documentation
- `tests/` — validation surface, including regression and golden checks
- `tests/golden/` — canonical expected hashes and fixtures for stable outputs

The exact layout will continue to evolve, but the governing idea is stable: logic goes in, evidence-bearing artifacts come out, and the pathway between them stays inspectable.

## Development and verification

ResearchCore is meant to be worked on through explicit generation and validation, not guesswork.

Typical local verification includes:

```bash
python tools/docs/gen_cli_ref.py
python tools/docs/gen_schema_ref.py
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
python -m pytest -q
```

Generated documentation and golden files are treated as canonical artifacts. If they change, that change should be intentional and reviewable.

## AI-assisted development

ResearchCore is also part of a broader effort to learn how to use AI-assisted tools to build systems that would otherwise require a larger team. AI is used here as leverage for iteration, explanation, debugging, and refinement — not as the standard of truth.

That distinction matters. AI can accelerate structure, surface options, and compress build cycles, but it does not make a result real. In ResearchCore, trust is still earned the hard way: through explicit artifacts, reproducible workflows, and outputs that can be checked against the process that created them. The role of AI is to expand what can be built; the role of validation is to decide what can be believed.

## Roadmap

### Validation-First Public Foundation
Make the repo publicly legible and coherent.
- README and docs polish
- public-facing workflow stability
- architecture clarity
- explicit validation and artifact policy

### Research Pathway Completion
Make the full lab pathway explicit and usable.
- clearer logic ingestion patterns
- stronger canonical dataset flow
- better artifact generation, validation, and comparison flow
- clearer extraction, harness, and risk stages
- stronger human-readable end reports

### Registry / Database Foundation
Build the memory layer of the lab.
- dataset registry
- logic registry
- run/result ledger
- artifact/result history
- decisions about what belongs in filesystem artifacts versus persistent records
- possible tick-data aggregation and timeframe-rebuild support

### Team and Ecosystem Readiness
Prepare the lab to support broader use later.
- cleaner contributor surface
- clearer repo boundaries
- modular expansion without turning the project into a junk drawer

## Scope and boundaries

ResearchCore is not an empty shell for optimism, narrative-first system talk, or unvalidated monetization stories. It is not here to make ideas feel serious. It is here to make them survive serious conditions.

The repo should continue to grow, but it should grow as a lab: modular, inspectable, deterministic where it matters, and intolerant of results that cannot be checked.