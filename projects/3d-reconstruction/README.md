# Calibrated 3D Reconstruction

**Status:** proposed project; no implementation or measured results yet. **Learning months:** 4.

## Problem statement

Recover a small scene from calibrated image/depth observations and explain geometric, scale, and measurement limits.

## Learning objectives

- Use explicit camera/world transforms and consistent units.
- Triangulate/backproject valid geometry and detect degeneracy.
- Evaluate both image residuals and spatial accuracy.

## Prerequisites

Camera geometry, homogeneous coordinates, SVD/least squares, robust estimation, and image processing.

## Proposed architecture

Images plus calibration → undistortion/rectification → correspondence/depth → robust geometry → triangulation/backprojection → filtering/alignment → point-cloud artifact and evaluator

Keep inputs, configuration, implementation, evaluation, and external artifacts separate when code is introduced. Share the [system interface conventions](../../docs/system-architecture.md) and [environment contract](../../docs/environment.md).

## Technologies

Python, NumPy, OpenCV, optional point-cloud library, synthetic camera scene, optional stereo/RGB-D hardware. No hardware purchase is needed for the baseline.

## Mathematical foundations

Pinhole projection, SE(3), epipolar geometry, stereo disparity, triangulation, RANSAC, ICP assumptions, and bundle-adjustment objectives.

## Implementation milestones

1. Validate frame conventions and noise-free synthetic projections.
2. Record intrinsics/extrinsics, calibration provenance, and a scale source.
3. Build a two-view or RGB-D baseline and reject invalid/negative depth.
4. Analyze residuals, outliers, baseline sensitivity, and alignment choices.
5. Reconstruct a bounded scene and document all scale/ground-truth limitations.

## Testing strategy

- Check projection/backprojection, transform composition/inversion, and known-point triangulation.
- Inject calibration error, outliers, low baseline, repetitive texture, and missing depth.
- Hold out calibration views; evaluate geometry against synthetic truth or measured reference distances.

## Evaluation metrics

- Held-out reprojection residual distribution in pixels.
- Depth/point error in meters where independent metric truth exists; coverage/completeness with a stated threshold.
- Outlier fraction, valid-depth fraction, and runtime/memory; report monocular scale alignment explicitly.

Declare task-specific acceptance thresholds before final evaluation. These are metric requirements, not completed results or promised performance. Compare against a simple reference on identical inputs/scenarios and preserve failure runs.

## Expected deliverables

Calibration and frame record, synthetic checks, reconstruction command/configuration, artifact hash/location, error report, and degeneracy analysis.

Use the [experiment template](../../experiments/TEMPLATE.md), link progress from the [journal](../../docs/learning-journal.md), and follow [hardware commissioning gates](../../hardware/README.md) for physical work. Record provenance/licenses for all data, models, scenes, and media.

## Future improvements

- Add multi-view refinement or a robust pose-graph baseline.
- Compare a learned depth prior without confusing relative depth with calibrated metric measurements.
