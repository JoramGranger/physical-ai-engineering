# Robot Arm Modeling and Control

**Status:** proposed project; no implementation or measured results yet. **Learning months:** 5–6, reuse in 10–12.

## Problem statement

Model and control a small manipulator with bounded joints and reproducible trajectories before attempting vision-guided tasks.

## Learning objectives

- Verify kinematics/Jacobians and reason about workspace/singularities.
- Tune a discrete controller under saturation, disturbances, and timing changes.
- Expose a bounded high-level motion interface.

## Prerequisites

Rigid-body transforms, derivatives, ODEs, C++ for robotics, and the robotics/control course. ROS integration follows the Month 6 module.

## Proposed architecture

Joint/goal request → limit/workspace validation → trajectory generation → joint controller → simulated plant → joint sensing → controller feedback and evaluator

Keep inputs, configuration, implementation, evaluation, and external artifacts separate when code is introduced. Share the [system interface conventions](../../docs/system-architecture.md) and [environment contract](../../docs/environment.md).

## Technologies

C++ controller, Python analysis, a small arm simulator, then ROS 2/Gazebo or compatible manipulation tools. Optional physical arm enters only after simulated limits and constrained commissioning.

## Mathematical foundations

Forward/inverse kinematics, SE(3), manipulator Jacobian, singularities, dynamics, PID, anti-windup, and trajectory smoothness.

## Implementation milestones

1. Derive a two-link model and check known poses/Jacobians.
2. Define joint, velocity, torque/current, and workspace constraints.
3. Implement a discrete simulation controller and compare saturation/timestep cases.
4. Integrate the robot model and command/state interface with replay logs.
5. Run bounded reach trajectories and prepare a later perception interface.

## Testing strategy

- Use analytic poses, finite-difference Jacobians, unreachable goals, and near-singular configurations.
- Simulate sensor dropout, stale commands, saturation, joint limits, and disturbance forces.
- For physical work, begin with power-limited individual joints and an independently accessible stop; record each commissioning gate.

## Evaluation metrics

- Joint and end-effector tracking RMSE with units.
- Rise time, overshoot, steady-state error, settling definition, and command-limit violations.
- Reach success denominator and controller timing distribution; distinguish simulated from physical evidence.

Declare task-specific acceptance thresholds before final evaluation. These are metric requirements, not completed results or promised performance. Compare against a simple reference on identical inputs/scenarios and preserve failure runs.

## Expected deliverables

Model derivation, controller/build configuration, trajectory fixtures, limit/fallback specification, plots, simulation report, and optional commissioning records.

Use the [experiment template](../../experiments/TEMPLATE.md), link progress from the [journal](../../docs/learning-journal.md), and follow [hardware commissioning gates](../../hardware/README.md) for physical work. Record provenance/licenses for all data, models, scenes, and media.

## Future improvements

- Study model-based or impedance control on a compatible platform.
- Add hand-eye calibration and bounded vision-guided pick/place.
