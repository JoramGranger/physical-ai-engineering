# Assignment: Reproducible classifier training

**Status:** specification. Implementation and measured results are future work.

## Task

Implement the Month 2 classifier workflow with checkpointing, a validation-only model-selection rule, and one controlled regularization or augmentation ablation. Use the same data contract as Month 1.

## Verification

- Compare analytic/autograd gradients and show tiny-batch learning before full training.
- Report class-wise metrics, held-out evaluation, seed variation, throughput, and exact resume conditions.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
