# Assignment: Detection, segmentation, and tracking audit

**Status:** specification. Implementation and measured results are future work.

## Task

Build one offline detector/tracker baseline and a small segmentation evaluation as the Month 3 assignment. Annotate a bounded sequence subset and split by session, keeping annotation and metric conventions explicit.

## Verification

- Test empty frames, border objects, occlusions, and coordinate round trips.
- Report AP with explicit thresholds, segmentation mean IoU, identity errors, stage latency, and sample count.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
