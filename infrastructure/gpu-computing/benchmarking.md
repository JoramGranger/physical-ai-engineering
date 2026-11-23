# GPU benchmarking protocol

Ask one question per benchmark: model-only latency, training throughput, end-to-end service latency, or scaling efficiency. These require different timing boundaries.

1. Record device, driver/runtime, framework/build, power mode, precision, batch/shape, model/data hashes, CPU threads, and background workload.
2. Validate outputs against the reference before performance tuning. Include a realistic input and a bounded synthetic input to separate data bottlenecks.
3. Warm up allocation, kernels, and compilation; report cold-start behavior separately.
4. For asynchronous GPU work, use device events or synchronize around host timing. State exactly what is included; host enqueue time is not GPU execution time.
5. Measure repeated samples after warmup and report count, p50/p95 latency, throughput, peak memory, and variation. Distinguish batched throughput from single-request latency.
6. Profile decode/loading, host-to-device transfer, kernels, synchronization, and postprocessing. Change one variable at a time and retest output parity.

## Scaling experiment

Compare one device with a small multi-device run only when the model/data pipeline justifies it. Report global versus per-device batch size, communication overhead, data-loader behavior, learning-rate changes, and time to a stated validation target. Raw examples/second alone does not measure learning efficiency.

Use the [PyTorch profiling material](https://docs.pytorch.org/tutorials/) matching the installed release. On a CPU-only host, profile the CPU reference and document GPU benchmarking as pending; do not invent device results.

## Result table template

| Run | Hardware/runtime | Shape/batch/precision | Timing boundary | Samples | p50/p95 | Throughput | Peak memory | Parity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Leave this table empty until measurements exist. Attach raw timing artifacts and configuration through the [experiment record](../../experiments/TEMPLATE.md).
