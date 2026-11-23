# Assignment: Leakage-free classical baseline

**Status:** specification. Implementation and measured results are future work.

## Task

Complete the Month 1 NumPy regression/classification assignment. Compare the hand-written learner with a trusted library and a simple tree or constant baseline. Survey other model families without turning every comparison into a separate project.

## Verification

- Assert that acquisition groups do not overlap splits and that the test set is not used for tuning.
- Report metrics, configuration, sample counts, baseline, and an explicit analysis of misclassified examples.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
