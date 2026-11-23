# Assignment: Calibrated reconstruction baseline

**Status:** specification. Implementation and measured results are future work.

## Task

Complete the Month 4 reconstruction pipeline with documented calibration, robust correspondence filtering, triangulation/backprojection, and residual analysis. Use synthetic data first and a small real scene only if available.

## Verification

- Check known projections and reject invalid depth, tiny disparity, and inconsistent calibration.
- Report reprojection and depth error separately, with coordinate frame, units, alignment, and scale source.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
