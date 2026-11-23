# Computer vision inference contract

Training and inference must share an explicit interpretation of images. Record color order, range, dtype, normalization, crop/resize/letterbox, interpolation, channel layout, and class mapping. For geometry, update intrinsics and box/mask coordinates consistently with preprocessing.

## Reference fixture

Use a small licensed/original image set covering blank inputs, image borders, multiple sizes, low confidence, and a known object/box/mask. Record expected shapes and a numerical/task-level tolerance. Compare original framework, service, and exported runtime on identical inputs; preprocessing differences often dominate numerical runtime differences.

For detectors, state whether NMS runs inside or outside the exported graph and document threshold/max-detection settings. For masks, state resolution, interpolation, and threshold. For tracks, define identity creation/deletion and behavior under missing/out-of-order frames.

## Timing and load

Timestamp capture, host receipt, queue entry/start, preprocessing completion, model completion, and response. Use a clock mapping when measuring across devices. Test one image first, then realistic arrival rate and bounded batching. Report input age, queue depth, dropped frames, and p50/p95 latency alongside AP/IoU/tracking quality.

Use [OpenCV](https://docs.opencv.org/4.x/) and [PyTorch tutorials](https://docs.pytorch.org/tutorials/) matching installed versions. Define output units/frame and reject stale observations before robot use. Reuse the [system contracts](../../docs/system-architecture.md).
