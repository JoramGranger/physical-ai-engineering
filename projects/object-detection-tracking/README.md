# Object Detection and Tracking

**Status:** proposed project; no implementation or measured results yet. **Learning months:** 3.

## Problem statement

Detect and maintain object identities in video, including missed detections, occlusions, and changing camera conditions.

## Learning objectives

- Preserve image/box/mask coordinates through preprocessing.
- Distinguish frame-level detection quality from sequence-level identity quality.
- Measure full pipeline latency and explicit failure cases.

## Prerequisites

Classifier baseline, CNN inference concepts, OpenCV, IoU, and elementary state prediction/assignment.

## Proposed architecture

Video source → timestamp/decode → preprocessing → detector → box rescaling/NMS → motion prediction and association → tracks/events → offline evaluator

Keep inputs, configuration, implementation, evaluation, and external artifacts separate when code is introduced. Share the [system interface conventions](../../docs/system-architecture.md) and [environment contract](../../docs/environment.md).

## Technologies

Python, OpenCV, PyTorch detector baseline, assignment/Kalman components, optional FastAPI inference wrapper after offline correctness. Record model-weight license and release.

## Mathematical foundations

Convolution, coordinate transforms, IoU, confidence thresholds, Kalman prediction/update, assignment cost, and precision/recall.

## Implementation milestones

1. Define classes, annotation convention, sequence-separated splits, and a small manually checked subset.
2. Run a fixed detector baseline and validate resizing/letterboxing.
3. Implement prediction/association, track creation/deletion, and missed-frame handling.
4. Add a bounded segmentation evaluation on a labeled subset.
5. Compare difficult sequences and profile capture-to-output timing.

## Testing strategy

- Use synthetic boxes for coordinate inversion and hand-computed IoU/matching tests.
- Test empty frames, duplicates, border objects, crossing tracks, occlusion, and changing resolution.
- Replay a frozen annotated sequence; verify timestamps and track lifecycle after dropped frames.

## Evaluation metrics

- Detection AP at declared IoU thresholds, class counts, and confidence operating point.
- Segmentation mean IoU on the declared subset; identity switches and IDF1 with matching convention.
- End-to-end p50/p95 latency, dropped-frame rate, and queue depth under declared input rate.

Declare task-specific acceptance thresholds before final evaluation. These are metric requirements, not completed results or promised performance. Compare against a simple reference on identical inputs/scenarios and preserve failure runs.

## Expected deliverables

Annotation/split manifest, detector/tracker architecture, metric definitions, evaluation report, representative failure clips outside Git, and inference contract.

Use the [experiment template](../../experiments/TEMPLATE.md), link progress from the [journal](../../docs/learning-journal.md), and follow [hardware commissioning gates](../../hardware/README.md) for physical work. Record provenance/licenses for all data, models, scenes, and media.

## Future improvements

- Compare stronger association or appearance embeddings on the same frozen sequences.
- Integrate calibrated depth and assess metric object localization.
