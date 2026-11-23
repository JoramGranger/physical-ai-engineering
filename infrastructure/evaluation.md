# Evaluation and evidence

Define the claim before choosing the metric. A classifier, depth estimator, task planner, and autonomous mission need different protocols even when they share a model.

## Protocol

Freeze data/session/episode splits, scenes, seeds, baselines, task definitions, and acceptance thresholds before final evaluation. Keep preprocessing/tuning/calibration data separate from held-out tests. Ground truth must be independent of algorithm inputs.

Use a simple baseline and an ablation that tests a concrete assumption. Compare on identical scenarios where feasible. Report denominators, failures, units, and repeated-run variation; do not silently exclude timeouts or invalid inputs. Distinguish simulated, replay, bench, and physical trials.

## Statistics

Report counts with rates. For mission success, include an interval method and sample size; a small number of successful missions does not establish rare-failure reliability. For latency, define warmup, timing boundary, load, sample count, and p50/p95. For trajectory/depth metrics, state alignment, scale, frames, and missing-data treatment.

## Release evidence

Link source/config commit, dirty-tree status, environment, data/model/scene hashes, command, hardware, raw artifacts, summary metrics, and known limitations. Reproduce one representative case from a clean checkout with documented external artifacts before marking a roadmap milestone complete.

Use the [experiment template](../experiments/TEMPLATE.md) and [curriculum rubric](../docs/curriculum.md#assessment-policy). Metric requirements are plans until populated with actual measurements.
