# Practical AI engineering track

Use three hours within each normal study week for this track. Existing backend, Linux, container, and HPC knowledge is assumed: focus on model/data correctness, GPU measurement, robot timing, and operational evidence.

| Month | Engineering outcome | Guide |
| --- | --- | --- |
| 1 | Environment/data/run contracts | [Training](gpu-computing/training.md), [experiments](../experiments/README.md) |
| 2 | Resume, profiling, GPU throughput | [GPU benchmarking](gpu-computing/benchmarking.md) |
| 3 | Inference/preprocessing contract | [Vision inference](model-serving/vision-inference.md) |
| 4 | Calibration/artifact provenance | [Experiment records](../experiments/TEMPLATE.md) |
| 5 | Telemetry, clocks, controller boundaries | [System interfaces](../docs/system-architecture.md) |
| 6 | Reproducible robotics environment | [Docker and Apptainer](containers/README.md) |
| 7 | Replay regression and estimator health | [Observability](observability.md) |
| 8 | Mission traces and simulation manifests | [Observability](observability.md) |
| 9 | Tool contracts, RAG, bounded orchestration | [Agent systems](model-serving/agent-systems.md) |
| 10 | Demonstration/policy evaluation | [Evaluation](evaluation.md) |
| 11 | ONNX parity and device profiling | [Edge deployment](edge-deployment/README.md) |
| 12 | Reproduction, rollback, release evidence | [Serving](model-serving/README.md), [evaluation](evaluation.md) |

No universal ML/container stack is installed by this repository. Training, middleware, embedded, and edge environments should have workload-specific manifests when their implementations begin.
