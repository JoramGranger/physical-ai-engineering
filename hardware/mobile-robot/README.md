# Differential-drive mobile base

Begin with the [simulated mobile project](../../projects/autonomous-mobile-robot/README.md). A physical base adds electrical, mechanical, and timing uncertainties to an already tested motion model.

## Geometry and interfaces

Measure wheel radius `r` and track width `b` in meters. For left/right angular velocities `ωL`, `ωR` in radians/second, forward speed is `v = r(ωR + ωL)/2` and yaw rate is `ω = r(ωR - ωL)/b` for the declared forward/sign convention. Check equal-speed translation, opposite-speed rotation, and zero commands.

Document base/encoder/IMU/camera frames, command units, rate, limits, and timeout. Use encoders for local motion feedback and a higher-level estimator for localization; wheel odometry alone accumulates drift.

## Build sequence

1. Simulate body motion, encoder noise, controller saturation, and command expiry.
2. Review driver/power/stop design and keep wheels raised for initial direction and encoder tests.
3. Compare commanded and measured low-speed wheel response, then straight/turn motion in a bounded supervised area.
4. Validate mounting/extrinsics and replay sensor data through localization before autonomous navigation.

Log wheel geometry, payload, surface, command limits, controller gains, battery/power conditions, and observed stop distance/time. Do not transfer simulation gains unchanged without measurement. Follow the [hardware gates](../README.md).

## Evidence

Keep a geometry/interface record, simulated control report, constrained bench observations, odometry drift estimate, and separately labeled physical navigation trials. No base has been built or tested at repository initialization.
