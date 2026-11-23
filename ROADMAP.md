# 12-month roadmap

This roadmap tracks demonstrated skills, not time spent watching courses. All items begin **planned**. Update a checkbox only when its linked evidence exists; the [journal](docs/learning-journal.md) records dates and assessment decisions.

## Capacity and scope

Commit **15–18 hours per week**, approximately **780–936 hours across 52 weeks**. Each learning month has four core weeks. Place one additional review/recovery week after Months 2, 4, 8, and 12, for 48 core weeks plus four buffer weeks. These are learning blocks, not fixed calendar dates.

A normal 16.5-hour week allocates 4 hours to lectures/reading, 3 to mathematics/exercises, 5 to the main project, 3 to the engineering track, and 1.5 to evaluation/journaling. Hardware work uses project hours. Buffer weeks address failed assessments, reproduce work, and absorb setup delays.

Select readings by topic; completing every listed university course is outside this time budget. Keep one core assignment and one evidence package per month. Extension topics are optional.

## Milestones

| Month | Primary study | Required evidence and gate | Parallel engineering outcome |
| --- | --- | --- | --- |
| 1 | Linear algebra, calculus, probability, classical ML | Correct gradient checks; leakage-free regression/classification baseline | Versioned environment, dataset manifest, run record |
| 2 | Backpropagation, PyTorch, optimization | Tiny-batch overfit diagnostic; held-out classifier and error analysis | Checkpoints, GPU timing, resumable training |
| 3 | OpenCV, detection, segmentation, tracking | Sequence-separated benchmark and documented failure cases | Inference contract, offline latency profile |
| 4 | Calibration, stereo, depth, 3D reconstruction | Frame-consistent reconstruction with residuals and scale discussion | Versioned calibration and data pipeline |
| 5 | Kinematics, dynamics, PID, robotics C++ | Simulation control benchmark; sensor/motor bench protocol | C++ build discipline, telemetry schema |
| 6 | ROS 2, Gazebo, robot integration | Reproducible launch, frame tree, bag replay, stale-command stop | Docker/Apptainer plan, integration tests |
| 7 | Localization, fusion, VO, SLAM | Estimated trajectory versus independent simulation ground truth | Replay regression suite and uncertainty diagnostics |
| 8 | Planning, mobile navigation, PX4 | Mobile mission suite plus aerial SITL smoke test and loss-of-link test | Pinned simulator manifests and telemetry |
| 9 | LLM systems, tools, RAG, task planning | Schema-constrained planner evaluated against scripted baseline | Tool traces, retrieval evaluation, bounded execution |
| 10 | VLM/VLA, RL, imitation learning | Small simulated policy comparison on held-out episodes | Policy/data versioning and rollout evaluation |
| 11 | Capstone integration, edge AI | One primary system completes frozen validation scenarios | ONNX parity, target-device profile, service contract |
| 12 | Capstone validation and publication | Reproducible release candidate, failure report, video evidence | Reliability/latency report and deployment runbook |

Detailed objectives, resources, weekly assignments, and assessment criteria are in the [curriculum](docs/curriculum.md).

## Progress record

- [ ] M01 — mathematical and ML baseline reviewed
- [ ] M02 — classifier evidence package reviewed
- [ ] M03 — perception benchmark reviewed
- [ ] M04 — reconstruction evidence package reviewed
- [ ] M05 — robot modeling and control reviewed
- [ ] M06 — ROS 2 simulation integration reviewed
- [ ] M07 — localization and mapping reviewed
- [ ] M08 — navigation and aerial simulation reviewed
- [ ] M09 — bounded agent planner reviewed
- [ ] M10 — simulated learned policy reviewed
- [ ] M11 — capstone integration gate passed
- [ ] M12 — capstone release evidence reviewed

## Capstone choice and dependencies

Choose one primary platform by the end of Month 8: [mobile robot](projects/autonomous-mobile-robot/README.md), [vision-guided manipulation](projects/vision-guided-manipulation/README.md), or [drone simulation](projects/autonomous-drone/README.md). Develop that platform in depth in Months 11–12. Retain a small simulated demonstration for each other platform, reusing the arm model from Month 5 and PX4 scene from Month 8. Three full physical builds are beyond the core scope.

Mathematics → ML/deep learning → perception; geometry + control → ROS integration → estimation/planning. Agentic and learned policies depend on the deterministic interfaces and fallback controllers built earlier. Edge optimization begins only after a measurable reference implementation exists.

If a gate fails, use the next buffer week and reduce extensions. Keep the frozen test set, model assumptions, and physical commissioning requirements intact. A simulation-only capstone satisfies the core path when hardware is unavailable; report that limitation explicitly.
