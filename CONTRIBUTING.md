# Contributing

Contributions should improve an engineering decision or a learner's ability to demonstrate a skill. Prefer a small, complete derivation, assignment, or reproducible experiment over a large set of unfinished lessons.

## Workflow

1. Open an issue describing the learning objective or observed defect, then work on a focused branch.
2. Read the relevant course/project README and keep material in its established directory.
3. Add original explanations, assumptions, verification steps, and resource attribution.
4. Run the documentation checks below and any checks required by executable code you introduce.
5. Open a PR using the template, linking evidence and identifying remaining limitations.

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

The validator checks required structure, documentation sections, local Markdown destinations, and heading fragments. It ignores links in fenced code blocks and does not make network requests. Its supported link syntax and limits are documented in [scripts/README.md](scripts/README.md). External resources are reviewed through the [catalog](docs/resources.md), avoiding flaky network checks in CI.

## Placement and authorship

- `courses/`: concepts, study plans, original exercises, assignments, and notes.
- `projects/`: system architecture, milestones, implementation, tests, and evaluation plans.
- `experiments/`: hypotheses, configurations, measurements, and decisions.
- `hardware/`: interfaces, wiring records, calibration, commissioning, and device constraints.
- `infrastructure/`: reproducible training, inference, serving, and deployment procedures.

Use relative links for repository files and descriptive labels for external sources. State units, coordinate frames, transform direction, tensor shapes, and timestamp semantics. Label every measured claim with its run record. Label planned targets as proposed.

Link to university materials; do not copy course solutions, lecture decks, book PDFs, datasets, or restricted content. These documents are an independent learning plan, not affiliated university courseware. Obtain permission before including third-party assets or identifiable recordings. External content retains its original license.

## Reproducibility and review

For code, supply exact setup/run commands, dependency versions, minimal test data or a licensed acquisition path, and a meaningful test of the underlying behavior. Record seeds and hardware; explain nondeterminism. Keep data and model artifacts out of Git and reference their hashes/locations instead.

For physical experiments, describe the simulation evidence and constrained bench procedure before motion tests. Use the [hardware gates](hardware/README.md). A review should be able to distinguish simulation, bench measurements, and physical autonomous trials.

Update the curriculum/resource catalog when a prerequisite or link changes. Never mark roadmap work complete based on a specification alone.
