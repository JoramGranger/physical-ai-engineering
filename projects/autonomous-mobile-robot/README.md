# Autonomous Mobile Robot

**Status:** proposed project; no implementation or measured results yet. **Learning months:** 5–8, primary capstone option in 11–12.

## Problem statement

Navigate a differential-drive robot between goals using perception, state estimation, planning, and closed-loop control.

## Learning objectives

- Integrate timestamped sensors and a consistent transform tree.
- Evaluate localization and navigation independently of estimator inputs.
- Demonstrate bounded recovery and stop behavior under faults.

## Prerequisites

Differential-drive model, PID, ROS 2/Gazebo, Bayesian estimation, SLAM, and planning. Months 5–8 build these incrementally.

## Proposed architecture

Camera/lidar/IMU/encoders → calibration/time alignment → perception and state estimation → map/localization → global/local planning → velocity controller → base; telemetry/evaluator observes all stages

Keep inputs, configuration, implementation, evaluation, and external artifacts separate when code is introduced. Share the [system interface conventions](../../docs/system-architecture.md) and [environment contract](../../docs/environment.md).

## Technologies

Ubuntu 24.04, ROS 2 Jazzy, Gazebo Harmonic, Nav2-compatible components, C++/Python, optional ESP32 motor/sensor adapter and edge computer. Pin all packages and bridges before integration.

## Mathematical foundations

Differential-drive kinematics, SE(2)/SE(3), EKF/particle filters, covariance, occupancy maps, graph search, collision geometry, and feedback control.

## Implementation milestones

1. Create motion model, velocity control, and sensor/command schemas.
2. Launch a simulated robot with frames, clock, sensors, and bag replay.
3. Compare wheel odometry, fused state, and a SLAM/localization baseline against independent truth.
4. Integrate navigation on fixed maps with explicit footprint and timeout rules.
5. Run frozen missions with disturbances, then optionally commission supervised physical ground operation.

## Testing strategy

- Check motion equations, frames, timestamp age, covariance sanity, and known-map planner behavior.
- Replay sensor loss, localization jumps, blocked routes, command-source loss, stale goals, and controller saturation.
- Use independent simulated ground truth only in evaluation; do not feed it into the estimator. Freeze scenes/seeds and evaluate failures as well as successes.

## Evaluation metrics

- Localization absolute/relative trajectory error, units, and alignment convention.
- Mission success with denominator/interval, collisions, minimum clearance, path length, completion time, and recovery counts.
- Tracking error, command age, sensor-to-command p50/p95 latency, message drops, and target power/memory where measurable.

Declare task-specific acceptance thresholds before final evaluation. These are metric requirements, not completed results or promised performance. Compare against a simple reference on identical inputs/scenarios and preserve failure runs.

## Expected deliverables

Robot/world descriptions, node/frame diagrams, manifests, launch/replay/evaluate commands, mission suite, fault report, and simulation/physical evidence labeled separately.

Use the [experiment template](../../experiments/TEMPLATE.md), link progress from the [journal](../../docs/learning-journal.md), and follow [hardware commissioning gates](../../hardware/README.md) for physical work. Record provenance/licenses for all data, models, scenes, and media.

## Future improvements

- Add dynamic obstacles or an evaluated high-level agent interface.
- Compare edge deployment or learned local decisions against the deterministic reference.
