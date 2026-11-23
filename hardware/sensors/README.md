# Sensors, calibration, and time

Treat sensor output as a measurement with units, calibration, timing, and uncertainty. Hardware collection begins only after the interface is documented; offline replay should work before closed-loop use.

| Sensor | Record | Calibration/check | Common failure |
| --- | --- | --- | --- |
| Camera | Model, resolution, intrinsics, distortion, exposure, frame/time | Held-out calibration views and reprojection residuals | Blur, exposure shift, wrong resized intrinsics |
| Stereo/RGB-D | Baseline/extrinsics, depth scale, valid range/mask | Known distances and frame conversion | Invalid depth, reflective surfaces, scale mismatch |
| Wheel encoders | Counts/revolution definition, sign, wheel radius | Measured travel and direction checks | Slip, missed counts, radius error |
| IMU | Axis/frame, units, rate, bias, timestamp | Stationary bias/noise and axis orientation checks | Drift, vibration, gravity/sign confusion |
| Lidar/range | Frame, angular convention, range/invalid values | Known geometry and extrinsic alignment | Reflective/transparent surfaces, occlusion |

## Calibration record

Store small text calibration files with schema version, units, transform direction, acquisition conditions/date, device serial/revision if appropriate, method, residuals, and raw-data hash/location. Keep raw recordings outside Git. Recalibrate after mounting, focus/resolution, or hardware changes that invalidate the model.

## Synchronization experiment

Create a common observable event in two streams, estimate delay/jitter, and compare against stated capture clocks. Inject a delay in replay and observe its effect on state estimation. Log capture time, host receipt time, sequence ID, and dropped samples separately. Do not infer accurate synchronization from similar arrival times.

In simulation, perturb bias, noise, latency, dropout, and extrinsics independently before combining them. Keep simulator ground truth out of algorithm inputs and retain it only in the evaluator.
