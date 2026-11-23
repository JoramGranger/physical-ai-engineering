# Vision-Guided Manipulation

**Status:** proposed project; no implementation or measured results yet. **Learning months:** 9–10, primary capstone option in 11–12.

## Problem statement

Ground a bounded object request in calibrated perception and execute a checked manipulation trajectory in simulation.

## Learning objectives

- Connect image/depth estimates to robot coordinates with an error budget.
- Separate task planning from geometric planning and low-level control.
- Compare scripted and learned/task-agent decisions under the same constraints.

## Prerequisites

Arm model/controller, camera calibration, 3D perception, ROS interfaces, and bounded agent planning. Learned-policy extensions require the embodied-AI module.

## Proposed architecture

Camera/depth → object/pose estimate → camera-to-robot transform → task request validator → grasp/trajectory planning → bounded arm executor → outcome verification; agent proposes tasks through schemas

Keep inputs, configuration, implementation, evaluation, and external artifacts separate when code is introduced. Share the [system interface conventions](../../docs/system-architecture.md) and [environment contract](../../docs/environment.md).

## Technologies

Python/C++, OpenCV/PyTorch, ROS 2, compatible manipulation planning/simulation, optional MoveIt 2, mocked/local LLM interface, and optional small behavior-cloning/RL model. Verify selected package support for the ROS release.

## Mathematical foundations

SE(3), camera/hand-eye calibration, pose uncertainty, inverse kinematics, collision geometry, grasp constraints, task graphs, and policy losses when used.

## Implementation milestones

1. Define object IDs, target workspace, camera/robot frames, and pose/observation age limits.
2. Validate pixel/depth-to-robot conversion on synthetic known points.
3. Build a scripted simulated pick/place or reach-and-verify baseline with failure results.
4. Add a schema-constrained task planner; compare against the scripted baseline.
5. Evaluate clutter/pose/noise cases and optionally compare a small learned policy before any physical progression.

## Testing strategy

- Check transform direction, calibration perturbations, unreachable goals, collision constraints, and gripper/joint limits.
- Reject unknown objects, stale observations, duplicate requests, malformed arguments, and out-of-workspace goals.
- Evaluate held-out object poses and failed grasp/outcome checks; learned decisions must pass the same executor constraints.

## Evaluation metrics

- Object-pose translation/rotation error with frame and symmetry convention.
- Task/grasp success denominators, placement error, cycle time, invalid-request rejections, and collisions/limit violations.
- Planning/inference latency and performance versus pose noise; distinguish failed perception from failed execution.

Declare task-specific acceptance thresholds before final evaluation. These are metric requirements, not completed results or promised performance. Compare against a simple reference on identical inputs/scenarios and preserve failure runs.

## Expected deliverables

Calibration/frame record, schemas, task/executor state machine, simulation scene, baseline comparison, held-out evaluation, failure traces, and optional physical commissioning record.

Use the [experiment template](../../experiments/TEMPLATE.md), link progress from the [journal](../../docs/learning-journal.md), and follow [hardware commissioning gates](../../hardware/README.md) for physical work. Record provenance/licenses for all data, models, scenes, and media.

## Future improvements

- Evaluate hand-eye calibration on a real constrained platform.
- Extend to varied objects or a pretrained VLA only after action and data compatibility checks.
