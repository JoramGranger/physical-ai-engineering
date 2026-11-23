# Hardware and simulation progression

The goal is disciplined integration, not early hardware complexity. Simulation is the required route for autonomous motion; physical builds are optional until equipment, supervision, and commissioning evidence are available.

| Stage | Activity | Evidence required before progression | Hardware-free alternative |
| --- | --- | --- | --- |
| 1 | ESP32 sensor acquisition | Board/SDK record, stable timestamped readings, units and wiring review | Synthetic sensor stream and protocol fixture |
| 2 | Camera perception | Capture/calibration record, replayable images, offline error analysis | Recorded or simulated camera |
| 3 | Basic motor control | Driver/power design, current/velocity limits, watchdog, accessible stop | Simulated motor/encoder plant |
| 4 | Differential-drive base | Raised-wheel checks, odometry/control comparison, supervised bounded motion | Gazebo base |
| 5 | Localization/navigation | Independent simulation evaluation and fault handling | ROS 2/Gazebo/Nav2 mission suite |
| 6 | Vision-guided arm | Model/limit checks, calibrated frames, constrained supervised reach | Simulated arm and scene |
| 7 | Edge inference | Output parity, timing/power/thermal report, fallback behavior | CPU ONNX runtime with explicit limits |
| 8 | Aerial autonomy | PX4 SITL mission and observed fault transitions | Full core requirement remains simulation |

## Functional equipment plan

Begin with an ESP32 development board, a documented sensor module, USB/serial interface, and a camera if available. Add encoder-equipped motors, a correctly rated driver, a differential-drive chassis, appropriate power regulation, and an independently accessible motor-power stop only when the motor stage begins. An arm, depth camera/lidar, and edge computer are later options, not initial requirements.

Choose actual parts against voltage/current, interface, driver support, mounting, and budget constraints. No specific pinout, electrical rating, vendor price, or purchase recommendation is implied here. Log the selected revisions and datasheets before wiring.

## Commissioning gates

1. **Model:** simulate commanded motion, sensor behavior, saturation, and command loss.
2. **Electrical:** document power domains, ground/reference, logic compatibility, driver ratings, protection, and stop/isolation path before energizing actuators.
3. **Constrained bench:** use a low-energy setup, bounded command duration, raised wheels or constrained joint range, and an accessible independent stop. Confirm direction, units, and watchdog response.
4. **Supervised motion:** use a clear bounded area/workspace and explicit speed/current limits; log observations and deviations.
5. **Autonomous trial:** carry over the validated limits and fault responses; assess each new operating condition separately.

Record date, exact configuration, test command, observed stop behavior, evidence, and pass/revise decision. Passing software tests does not establish electrical or mechanical readiness. Physical drone flight is a separate project beyond this curriculum's required SITL work.

Device guides: [ESP32](esp32/README.md), [sensors](sensors/README.md), [mobile base](mobile-robot/README.md), [arm](robotic-arm/README.md), [aerial simulation](aerial-robotics/README.md).
