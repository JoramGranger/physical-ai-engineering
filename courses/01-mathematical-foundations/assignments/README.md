# Assignment: Gradient and conditioning audit

**Status:** specification. Implementation and measured results are future work.

## Task

Produce the derivation and numerical-verification component of the Month 1 ML assignment. Compare a well-conditioned and rank-deficient design matrix; use the same loss normalization in every implementation.

## Verification

- Check the derivative at multiple non-optimal parameter vectors and use absolute tolerance for near-zero components.
- Compare fitted predictions and residuals, not just coefficients, when solutions are non-unique.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
