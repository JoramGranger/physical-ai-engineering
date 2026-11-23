# PyTorch model training protocol

## Data and reference behavior

Define sample/label semantics, acquisition groups, split hashes, class mapping, augmentation, and normalization. Fit learned preprocessing on the training split. Use a constant/classical baseline, then a small model before scaling.

Separate data loading, training step, validation, prediction, and metrics. State tensor shapes/dtypes and whether outputs are logits, probabilities, or coordinates. Run a forward/backward pass, inspect finite loss/gradients, and overfit a tiny clean batch before a full job.

## Training state

Make train/eval mode and gradient-enabled/disabled regions explicit. Log loss normalization, optimizer, learning-rate schedule, batch size, precision, seed, and data ordering. Save model, optimizer, scheduler, mixed-precision scaler when used, RNG state, step/epoch, class mapping, and preprocessing/config identifiers.

Check resume by comparing a continuous run with a checkpointed continuation under declared determinism conditions. Exact bitwise equivalence is not promised across devices/runtime versions; explain the expected tolerance and nondeterministic operations.

## Evaluation

Select configurations on validation only. Freeze the selection rule before using the held-out test set. Report class-wise errors, baseline comparison, sample counts, and seed variation for cheap experiments. Keep both successful and failed run records.

## HPC execution

Resolve dependencies and container/runtime compatibility before reserving expensive resources. Stage data once, log scheduler allocation and container digest, and place artifacts on an appropriate writable persistent/scratch path. Bound wall time and checkpoint before expected interruption; evaluate interrupted/resumed behavior on a small job first.

Use the [benchmark protocol](benchmarking.md) when assessing performance. Store checkpoints externally with hashes; the [experiment record](../../experiments/TEMPLATE.md) should be sufficient to reconstruct the run. The initial repository provides this protocol, not a completed trainer.
