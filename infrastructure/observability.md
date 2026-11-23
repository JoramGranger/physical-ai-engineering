# AI and autonomy observability

Instrument the question you need to answer: was a failure caused by perception, state estimation, planning, control, communication, or deployment?

| Layer | Signals | Diagnostic use |
| --- | --- | --- |
| Data/sensors | Sequence gaps, capture age, calibration ID, invalid values | Detect dropout, staleness, schema/calibration mismatch |
| Perception | Confidence/error slices, detections/masks, model version, stage timing | Separate model quality from preprocessing/load effects |
| Estimation | Residuals, covariance, localization health, frame/clock state | Identify drift, bad noise models, timing errors |
| Planning/control | Goal/plan ID, rejection reason, tracking error, saturation, command expiry | Explain infeasible plans, slow response, fallback transitions |
| Agents/policies | Tool/action traces, evidence IDs, budgets, termination, reward and success | Explain decision errors and unsafe/invalid requests rejected by executor |
| Runtime | Queue depth, p50/p95, dropped work, memory, device health, power/temperature | Explain latency and resource bottlenecks |

Correlate a run, observation, task, and model/config version across layers. Preserve timestamp clock semantics. Avoid claiming a cross-device duration from unsynchronized clocks. Keep raw media/telemetry outside Git and commit summaries plus artifact hashes.

In the first implementation, structured logs and an offline report are sufficient. Add metrics/traces/dashboard infrastructure when it resolves a real operational question. Thresholds should follow the mission/control budget, not a generic service default.

Create one end-to-end fault trace showing input, detection/estimate, decision, command, fallback, and observed outcome. Use it during monthly review and retain unsuccessful runs.
