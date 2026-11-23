# Assignment: Measured deployment candidate

**Status:** specification. Implementation and measured results are future work.

## Task

Complete the Month 11 capstone deployment component. Use CPU ONNX as the hardware-free baseline; attempt TensorRT only on a compatible NVIDIA target. Record unsupported export operations rather than claiming parity.

## Verification

- Report task-metric parity, latency percentiles, peak memory, warmup, workload, and device/runtime manifest.
- Exercise stale requests, overload, restart, artifact version mismatch, and fallback/rollback behavior.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
