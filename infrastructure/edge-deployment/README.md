# Edge AI deployment: ONNX and TensorRT

Begin with a working reference model, fixed preprocessing, and target constraints. “Edge-ready” requires measurements on the actual device; a desktop benchmark is a useful surrogate only when labeled as such.

## Export and parity

1. Freeze weights, evaluation mode, preprocessing/class mapping, representative inputs, and acceptance tolerances.
2. Export a supported component to ONNX using a release-compatible path; record exporter, opset, shapes/dynamic dimensions, and unsupported operations.
3. Validate the graph and compare runtime outputs on identical inputs, including near-threshold examples and empty/boundary cases.
4. Compare task metrics as well as tensor errors; check box scaling, NMS location, mask thresholds, and policy action normalization.

Use [ONNX documentation](https://onnx.ai/onnx/) and the installed release's [PyTorch export material](https://docs.pytorch.org/tutorials/). CPU ONNX inference is the hardware-free reference.

## TensorRT and precision

Use [TensorRT's support matrix and documentation](https://docs.nvidia.com/deeplearning/tensorrt/latest/) for the actual NVIDIA device/SDK/runtime. Build and test an engine for that target; do not assume engine portability. Record precision, input shapes, plugin versions, builder settings, and all calibration data if lower-precision calibration is used.

Choose representative calibration data from the permitted training/calibration partition, never by tuning against the held-out test set. Measure accuracy drift before accepting speed or memory improvements.

## Target validation

Measure cold start, warm p50/p95 latency, end-to-end sensor-to-output age, memory, sustained throughput, and power/thermal behavior where accessible. Record device power mode, ambient/load conditions, cooling, and test duration. Test overload, unavailable device, restart, stale requests, and rollback to the reference bundle.

Deliver a target manifest, parity report, benchmark artifacts, inference contract, and fallback/rollback instructions. If target hardware or supported export is unavailable, mark those checks pending and retain the correct reference system.
