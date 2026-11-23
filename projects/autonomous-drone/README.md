# Autonomous Drone Simulation

**Status:** proposed project; no implementation or measured results yet. **Learning months:** 8, primary capstone option in 11–12.

## Problem statement

Execute a bounded aerial mission in PX4 software-in-the-loop simulation with explicit frame conventions and loss-of-command behavior.

## Learning objectives

- Understand aerial estimation/control interfaces without requiring physical flight.
- Reproduce mission and failsafe behavior from pinned simulation configuration.
- Measure tracking, mission completion, and failure recovery.

## Prerequisites

Dynamics/control basics, state estimation, coordinate transformations, planning concepts, and PX4 simulation documentation.

## Proposed architecture

Simulated vehicle/sensors → PX4 estimation/control → mission or offboard interface → bounded command source; simulator truth and vehicle logs → independent mission evaluator

Keep inputs, configuration, implementation, evaluation, and external artifacts separate when code is introduced. Share the [system interface conventions](../../docs/system-architecture.md) and [environment contract](../../docs/environment.md).

## Technologies

PX4 pinned firmware release/commit, a simulator supported by that release, supported mission/offboard client, vehicle telemetry/log analysis, and optional ROS bridge only after compatibility verification.

## Mathematical foundations

Rigid-body frames, ENU/NED and body conventions, attitude/quaternions, feedback control, trajectory constraints, estimation uncertainty, and timing.

## Implementation milestones

1. Record supported host/simulator/firmware/airframe combination separately from the mobile ROS stack.
2. Run takeoff, hold/waypoint, and landing with position/time bounds.
3. Specify command rate/timeouts and configure loss-of-link/command behavior from versioned docs.
4. Inject simulated command loss and verify expected hold/return/land transition for the chosen configuration.
5. For a primary capstone, add one bounded perception or planning component and evaluate against the reference mission.

## Testing strategy

- Verify coordinate conversion on basis vectors and validate command units/rates in a static fixture.
- Use SITL for geofence, command loss, estimator degradation where supported, and mission timeout scenarios.
- Repeat scene/seed trials and log actual mode transitions; do not infer failsafe operation merely from configuration values.

## Evaluation metrics

- Mission completion with denominator, position/trajectory RMSE, overshoot, and landing displacement.
- Mode-transition latency, geofence breaches, command-age distribution, and configured/observed loss response.
- Mission duration and inference/bridge delay if a companion component is added; label simulation measurements explicitly.

Declare task-specific acceptance thresholds before final evaluation. These are metric requirements, not completed results or promised performance. Compare against a simple reference on identical inputs/scenarios and preserve failure runs.

## Expected deliverables

Firmware/simulator manifest, airframe/mission configuration, run/evaluation instructions, SITL logs/artifact hashes, frame diagram, fault demonstration, and limitations report.

Use the [experiment template](../../experiments/TEMPLATE.md), link progress from the [journal](../../docs/learning-journal.md), and follow [hardware commissioning gates](../../hardware/README.md) for physical work. Record provenance/licenses for all data, models, scenes, and media.

## Future improvements

- Study visual-inertial localization or obstacle-aware planning in simulation.
- Consider hardware-in-the-loop as a separate commissioned project; physical flight is outside the core curriculum requirement.
