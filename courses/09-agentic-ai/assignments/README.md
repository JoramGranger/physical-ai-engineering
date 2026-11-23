# Assignment: Bounded simulated task planner

**Status:** specification. Implementation and measured results are future work.

## Task

Complete the Month 9 tool/RAG planner assignment using a mocked or local model when API access is unavailable. Compare to a scripted planner on the same predeclared tasks. No vendor API dependency is assumed at initialization.

## Verification

- Include stale observations, malformed arguments, inaccessible objects, retrieved instructions, and exhausted budgets.
- Log rejected as well as accepted calls; demonstrate that the executor independently enforces limits.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
