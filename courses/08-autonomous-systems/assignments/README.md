# Assignment: Estimation and mission evaluation

**Status:** specification. Implementation and measured results are future work.

## Task

This course spans the existing Month 7 filter/SLAM assignment and Month 8 navigation assignment. Use one mobile environment across both, adding only a small separately pinned PX4 SITL demonstration.

## Verification

- Keep ground truth out of estimator inputs; report trajectory drift and uncertainty diagnostics.
- Evaluate at least ten cheap simulated missions and inject command loss; report collisions, timeouts, tracking error, and failures.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
