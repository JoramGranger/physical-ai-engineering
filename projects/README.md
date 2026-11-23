# Engineering projects

All seven projects are **specifications** at initialization. No implementation, trained model, hardware build, or experimental result is claimed. Start with the monthly core assignment, then expand only when its assessment passes.

| Project | Learning months | Primary evidence |
| --- | --- | --- |
| [Reproducible Image Classification](image-classification/README.md) | 1–2 | Data/split manifest |
| [Object Detection and Tracking](object-detection-tracking/README.md) | 3 | Annotation/split manifest |
| [Calibrated 3D Reconstruction](3d-reconstruction/README.md) | 4 | Calibration and frame record |
| [Robot Arm Modeling and Control](robotic-arm/README.md) | 5–6, reuse in 10–12 | Model derivation |
| [Autonomous Mobile Robot](autonomous-mobile-robot/README.md) | 5–8, primary capstone option in 11–12 | Robot/world descriptions |
| [Vision-Guided Manipulation](vision-guided-manipulation/README.md) | 9–10, primary capstone option in 11–12 | Calibration/frame record |
| [Autonomous Drone Simulation](autonomous-drone/README.md) | 8, primary capstone option in 11–12 | Firmware/simulator manifest |

## Capstone scope

Choose one primary platform by Month 8 and integrate it in depth during Months 11–12. Reuse the earlier arm, mobile, and PX4 simulations for smaller demonstrations of the other two. Simulation-only completion is valid when hardware is unavailable; explicitly state which physical claims remain untested.

A capstone combines calibrated perception, estimated state, constrained planning, closed-loop control, observability, and an evaluated fallback. An agent or learned policy is an optional decision layer, not a prerequisite for a capable autonomous system.
