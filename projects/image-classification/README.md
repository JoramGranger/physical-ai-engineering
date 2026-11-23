# Reproducible Image Classification

**Status:** proposed project; no implementation or measured results yet. **Learning months:** 1–2.

## Problem statement

Classify a bounded set of visual categories while establishing reliable data splits, training diagnostics, and deployment-ready inference semantics.

## Learning objectives

- Compare classical, small-CNN, and transfer-learning baselines fairly.
- Separate optimization, generalization, and data-quality failures.
- Produce reproducible evaluation rather than a single accuracy number.

## Prerequisites

Mathematical foundations, classical ML, and PyTorch training modules. Start without a GPU on a small subset.

## Proposed architecture

Licensed images → group-aware split manifest → training-only preprocessing → baseline/CNN training → validation selection → frozen evaluation → versioned inference artifact

Keep inputs, configuration, implementation, evaluation, and external artifacts separate when code is introduced. Share the [system interface conventions](../../docs/system-architecture.md) and [environment contract](../../docs/environment.md).

## Technologies

Python, NumPy, PyTorch, optional classical-ML library, image loading, structured configuration, and a later inference adapter. Select and lock dependencies when implementation starts.

## Mathematical foundations

Cross-entropy, gradients/backpropagation, regularization, stochastic optimization, class imbalance, calibration, and sampling uncertainty.

## Implementation milestones

1. Define label taxonomy, acquisition groups, dataset license/provenance, and immutable test split.
2. Create constant/classical baselines and verify preprocessing fits training data only.
3. Debug a small CNN by overfitting a tiny batch; add checkpoint/resume.
4. Compare transfer learning with one controlled augmentation/regularization ablation.
5. Freeze model selection, evaluate, and prepare model/inference documentation.

## Testing strategy

- Check labels, split disjointness, shapes, class mapping, and preprocessing round trips.
- Test tiny-batch learning, evaluation mode, checkpoint restoration, empty/invalid input, and repeatable prediction.
- Use held-out acquisition sessions where possible; keep a small regression set of previously failed cases.

## Evaluation metrics

- Accuracy plus macro precision/recall/F1 and per-class confusion counts.
- Calibration error with binning convention and sample count; error slices by acquisition condition.
- Inference p50/p95 latency, throughput at stated batch size, peak memory, and three-seed variation for the small baseline.

Declare task-specific acceptance thresholds before final evaluation. These are metric requirements, not completed results or promised performance. Compare against a simple reference on identical inputs/scenarios and preserve failure runs.

## Expected deliverables

Data/split manifest, derivation and baseline comparison, training/evaluation commands, model card, checkpoint hash/location, error taxonomy, and a reproducible run report.

Use the [experiment template](../../experiments/TEMPLATE.md), link progress from the [journal](../../docs/learning-journal.md), and follow [hardware commissioning gates](../../hardware/README.md) for physical work. Record provenance/licenses for all data, models, scenes, and media.

## Future improvements

- Evaluate domain shift on an independently acquired session.
- Export to ONNX and compare task/output parity before edge optimization.
