# Aerial robotics: simulation first

The required aerial work is [PX4 SITL](../../projects/autonomous-drone/README.md). Physical flight hardware is not needed for curriculum completion.

## Simulation baseline

Use the [versioned PX4 documentation](https://docs.px4.io/v1.17/en/) to select a compatible host, simulator, firmware, and airframe. Record exact commits/versions and mission/failsafe parameters. Keep this environment separate from the ground ROS stack until bridge/simulator compatibility is demonstrated.

Begin with takeoff, hold/waypoint, and landing. Define command rates, frame conventions, position/velocity bounds, timeouts, and expected mode transitions. Test coordinate conversion on basis vectors before commanding a mission; world NED/ENU and body-frame conventions require separate attention.

## Fault experiment

Stop the command source in simulation and log the actual response: mode transition, timing, and final state. Compare with the configured behavior rather than assuming a failsafe triggered. Repeat for mission timeout and a supported geofence case.

Keep vehicle logs, scene/seed, configuration, ground truth, and evaluation linked through an experiment ID. Preserve unsuccessful missions. Report simulation tracking/error/latency measurements explicitly as simulated.

## Physical extension

Hardware-in-the-loop or physical flight requires a separate platform, operating procedure, commissioning plan, and applicable local requirements. No physical-flight commands, airframe wiring, or readiness claim is supplied at initialization.
