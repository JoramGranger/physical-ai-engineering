# Physical AI engineering curriculum

This is an independent self-study plan for an experienced software engineer. It builds mathematical and experimental judgment alongside algorithms and physical-system integration. Programming fundamentals, web frameworks, Linux basics, and introductory container tutorials are outside scope.

## Study contract

Use **15–18 hours weekly**. A typical week is 4 hours of lectures/reading, 3 of mathematical exercises, 5 of project work, 3 of practical AI engineering, and 1.5 of evaluation/journaling. Each month below has four core weeks (60–72 hours). Add review weeks after Months 2, 4, 8, and 12, giving 52 weeks and 780–936 hours overall. Start dates are chosen by the learner.

Each month has one core programming assignment. Smaller exercises support it; they are not additional large projects. University resources are selective references: study the named subject areas in public notes/lectures, rather than attempting entire courses concurrently. Topic labels below are study selections, not asserted lecture titles or numbers. Consult the [resource verification register](resources.md) for access limitations and book availability.

The engineering track uses your backend/HPC experience to make experiments reproducible and deployable. Its three weekly hours are included in the commitment. Start hardware with sensors and constrained motor work; use simulation for autonomy before physical commissioning. Hardware-free alternatives preserve every required learning objective.

## Assessment policy

At each month end, assess mathematical reasoning (30 points), implementation/correctness (25), evaluation/reproducibility (25), and technical explanation (20). A pass requires **70/100**, all required deliverables, a reproducible small run, and the specific gate below. A high aggregate score cannot compensate for data leakage, unexplained frame/unit errors, or missing stop/fallback behavior in an autonomous system.

Numerical targets below are **proposed assessment targets**, not measured results or universal performance guarantees. Set task-dependent thresholds before evaluating, freeze the validation protocol, and explain justified changes in the journal. Use held-out tests only after decisions are frozen. Record failures and remediation; use a buffer week before proceeding when a gate fails.

For experiments, record versions, data/scene hashes, seeds, hardware, sample counts, units, uncertainty, and failure cases using the [run template](../experiments/TEMPLATE.md). A video complements evaluation; it does not replace it.

## Month 1 — Mathematical foundations and classical ML

### Learning objectives

Translate a learning problem into vectors, a loss function, and an evaluation protocol. Derive gradients and explain generalization before selecting a complex model.

### Mathematical concepts

Vector spaces, matrix rank, eigenvectors/SVD, projections, least squares; partial derivatives, gradients, chain rule; conditional probability, Bayes' rule, expectations, covariance, maximum likelihood; convexity and gradient descent.

### Topics and subtopics

Linear/logistic regression, regularization, bias/variance, normalization, cross-validation, class imbalance, decision-tree baselines. Recognize when correlated examples require group/time-based splits.

### University lectures

Select regression, classification, and statistical-learning material from [Stanford CS229](https://see.stanford.edu/Course/CS229). Use its mathematical prerequisites as a diagnostic rather than restarting programming study.

### Recommended textbooks

[Mathematics for Machine Learning](https://mml-book.github.io/): linear algebra, vector calculus, probability, and optimization by topic.

### Practical exercises

Solve a rank-deficient least-squares problem with QR/SVD; derive logistic loss gradients; check central differences at several step sizes; demonstrate leakage by fitting normalization before versus after a split.

### Programming assignment

Implement vectorized linear and logistic regression in NumPy. Compare with an established library baseline using the same split and features. Produce loss curves, a confusion matrix, and an error taxonomy; keep the test split untouched during tuning.

### Hardware or simulation

Generate synthetic noisy distance/sensor observations with known parameters. If available, capture ESP32 sensor readings with timestamps and units; synthetic data is the complete alternative.

### Projects and weekly sequence

Prepare the dataset/split contract for [image classification](../projects/image-classification/README.md). W1: diagnostic and least squares. W2: probability and logistic model. W3: baseline comparisons. W4: evaluation and review.

### Parallel AI engineering

Create an isolated environment and run manifest; version configuration and data hashes. Separate training, prediction, and evaluation interfaces. Follow the [training guide](../infrastructure/gpu-computing/training.md).

### Expected deliverables

Original gradient derivation, numerical checks, baseline implementation, split manifest, experiment report, and journal review.

### Assessment criteria

Explain identifiability, bias/variance, and leakage. On smooth float64 examples, target gradient relative error below `1e-5`, with an absolute tolerance near zero. Reproduce the reference objective within a declared tolerance and explain any coefficient differences due to conditioning or regularization.

## Month 2 — Deep learning and PyTorch

### Learning objectives

Implement and debug neural-network training, distinguish optimization failure from generalization failure, and establish a reproducible image-classification baseline.

### Mathematical concepts

Reverse-mode differentiation, Jacobian-vector products, cross-entropy, initialization variance, stochastic gradients, momentum/Adam, regularization. Survey PCA/clustering and margin-based classification to place neural methods among alternatives.

### Topics and subtopics

MLPs and CNNs, activations, autograd, data loaders, batching, normalization, dropout, augmentation, transfer learning, learning-rate schedules, checkpoint/resume, train/eval mode, mixed-precision tradeoffs.

### University lectures

Select training and optimization material from [Stanford CS230](https://cs230.stanford.edu/) and visual-network foundations from [Stanford CS231n](https://cs231n.stanford.edu/2025/). Use public notes or archived videos where current videos are restricted.

### Recommended textbooks

[Deep Learning](https://www.deeplearningbook.org/): feedforward networks, regularization, and optimization. Refer to MML for missing derivative/probability foundations.

### Practical exercises

Manually backpropagate through a two-layer network; compare to autograd. Overfit a fixed tiny batch; deliberately introduce a label shuffle or missing `eval()` call and diagnose the symptoms.

### Programming assignment

Train a small CNN and a transfer-learning baseline for the [classifier project](../projects/image-classification/README.md). Implement resumable state, validation-only model selection, per-class metrics, and an ablation of one regularizer.

### Hardware or simulation

Replay fixed camera images under simulated brightness/noise changes. Use CPU training on a small subset if a GPU is unavailable; physical camera capture is optional.

### Projects and weekly sequence

W1: derivatives and tiny-batch debugging. W2: CNN baseline. W3: transfer learning/ablation. W4: frozen evaluation and model card.

### Parallel AI engineering

Measure CPU/GPU throughput with warmup and synchronization. Save optimizer and RNG state; document memory usage and nondeterministic operations. Use the [GPU benchmark protocol](../infrastructure/gpu-computing/benchmarking.md).

### Expected deliverables

Training entry-point specification or implementation, environment manifest, checkpoints outside Git, metrics, error slices, ablation table, model card, and resume comparison.

### Assessment criteria

Target at least 95% training accuracy on an intentionally small clean batch. Evaluate against the majority-class baseline on held-out data and explain failures rather than hiding them. Demonstrate correct split handling and checkpoint restoration; report variation across three seeds for the inexpensive baseline.

## Month 3 — Computer vision pipelines

### Learning objectives

Build image/video pipelines with explicit preprocessing, detection, segmentation, and tracking evaluation. Understand what individual frames cannot reveal about temporal behavior.

### Mathematical concepts

Discrete convolution, gradients, sampling/aliasing, coordinate rescaling, intersection-over-union, precision/recall, bipartite assignment, elementary Kalman prediction and update.

### Topics and subtopics

OpenCV color spaces, filtering, morphology, edges, feature extraction; detector fine-tuning/inference, NMS, segmentation masks, association, occlusion, track lifecycle, video timestamps, sequence leakage.

### University lectures

Select image-processing material from [MIT 6.801](https://ocw.mit.edu/courses/6-801-machine-vision-fall-2020/) and recognition/detection material from [CS231n](https://cs231n.stanford.edu/2025/). MIT OCW supplies notes/assignments; do not assume every topic has a video.

### Recommended textbooks

[Szeliski — Computer Vision](https://szeliski.org/Book/): image processing, recognition, and motion topics; DL for CNN review.

### Practical exercises

Measure resizing effects on bounding boxes; compare edge filters; label a small segmentation subset and compute mean IoU. Track two crossing objects and inspect ID switches manually.

### Programming assignment

Implement the offline baseline for [object detection and tracking](../projects/object-detection-tracking/README.md), plus one small segmentation evaluation. Split by recording/session and document annotation and matching conventions.

### Hardware or simulation

Use a fixed prerecorded sequence or a simulator camera. Optional USB-camera capture should log exposure/resolution and capture timestamps; keep video artifacts outside Git.

### Projects and weekly sequence

W1: classical processing. W2: detection. W3: segmentation and association. W4: temporal evaluation and error review.

### Parallel AI engineering

Define an inference request/output schema and preprocessing contract. Profile decode, preprocess, model, postprocess, and queueing separately using the [vision inference guide](../infrastructure/model-serving/vision-inference.md).

### Expected deliverables

Pipeline diagram, sequence split manifest, detection/segmentation/tracking report, annotated failure clips, and latency table with hardware and sample count.

### Assessment criteria

Check coordinate round trips on known boxes, metric calculations on hand-labeled examples, and empty-frame behavior. Report AP at explicit IoU thresholds, mean IoU, ID switches, and latency percentiles. Compare against a simple fixed detector/association baseline; no hardware-independent FPS target is imposed.

## Month 4 — Spatial intelligence and 3D perception

### Learning objectives

Recover calibrated spatial structure and quantify its uncertainty. Distinguish metric depth from scale-ambiguous monocular reconstruction.

### Mathematical concepts

Homogeneous coordinates, pinhole projection, SO(3)/SE(3), camera extrinsics, epipolar constraints, triangulation, least squares, RANSAC, bundle-adjustment objective, uncertainty propagation.

### Topics and subtopics

Camera calibration/distortion, stereo rectification, correspondence, disparity/depth, monocular depth limitations, structure from motion, RGB-D backprojection, point clouds, ICP and degenerate geometry.

### University lectures

Select camera/geometry material from [Stanford CS231A](https://web.stanford.edu/class/cs231a/) and image-formation material from [MIT 6.801](https://ocw.mit.edu/courses/6-801-machine-vision-fall-2020/).

### Recommended textbooks

[Multiple View Geometry](https://www.robots.ox.ac.uk/~vgg/hzbook/) for projective geometry and [Szeliski](https://szeliski.org/Book/) for practical reconstruction. Use available sample material or library access rather than assuming free full-book access.

### Practical exercises

Derive `Z = fB/d` for rectified stereo and analyze depth sensitivity to disparity error. Compose/invert frame transforms. Simulate near-zero baseline, distant points, and outlier correspondences.

### Programming assignment

Build a small [3D reconstruction](../projects/3d-reconstruction/README.md) baseline: calibrate or use documented synthetic intrinsics, estimate correspondences, triangulate, filter invalid depth, and calculate reprojection residuals.

### Hardware or simulation

Use simulated stereo/RGB-D ground truth. Optional real-camera calibration requires held-out calibration views and a known scale reference; a monocular sequence alone does not establish metric scale.

### Projects and weekly sequence

W1: calibration/frames. W2: epipolar geometry. W3: depth/reconstruction. W4: residual analysis. Use the following buffer week for geometric debugging.

### Parallel AI engineering

Version calibration files, coordinate conventions, image hashes, and preprocessing. Make the same pipeline replayable without a camera.

### Expected deliverables

Calibration record, transform diagram, synthetic geometry checks, reconstruction artifact reference, residual distributions, and scale/uncertainty discussion.

### Assessment criteria

Recover noise-free synthetic projections within declared floating-point tolerance; detect negative depth and near-zero disparity. On held-out noisy views, report reprojection and depth errors separately. Explain why low reprojection error can coexist with poor depth or ambiguous scale.

## Month 5 — Robot mechanics, control, and embedded interfaces

### Learning objectives

Model a manipulator and differential-drive base, implement stable discrete control, and connect sensing/actuation concepts to physical interfaces.

### Mathematical concepts

Rigid-body transformations, forward/inverse kinematics, manipulator Jacobians, singularities, Newton/Euler or Lagrangian dynamics, ODE discretization, PID, saturation and integral windup.

### Topics and subtopics

Joints/actuators, encoders, IMUs, motor drivers, differential-drive odometry, trajectory setpoints; robotics C++ ownership/RAII, references, build systems, numerical types, timing, and bounded loops.

### University lectures

Select modeling and control material from [Northwestern Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/), [Princeton Introduction to Robotics](https://irom-lab.princeton.edu/intro-to-robotics/), and [MIT Underactuated Robotics](https://underactuated.mit.edu/).

### Recommended textbooks

[Modern Robotics — Lynch and Park](https://modernrobotics.org/): kinematics, dynamics, and control by topic. Use MIT's notes selectively for nonlinear-control context.

### Practical exercises

Derive two-link planar arm kinematics and finite-difference its Jacobian. Derive wheel-speed/body-twist relations. Compare PID behavior under saturation, sensor noise, and timestep changes.

### Programming assignment

Build a small simulated arm or wheel-velocity controller in C++ with reproducible build/run instructions and Python plots. Add joint/velocity limits, anti-windup, and stale-input handling. Reuse the model in the [arm project](../projects/robotic-arm/README.md).

### Hardware or simulation

Begin with [ESP32 telemetry](../hardware/esp32/README.md), then a constrained low-energy motor test with a driver. Keep wheels raised and power limited. Full alternative: simulated encoder/PWM interface and motor dynamics.

### Projects and weekly sequence

W1: kinematics. W2: dynamics/PID. W3: C++ controller and sensor protocol. W4: disturbances and limits; record mobile-base and arm models for later reuse.

### Parallel AI engineering

Define telemetry units, sequence numbers, timestamps, watchdog behavior, and logs; separate nondeterministic analysis from the control loop.

### Expected deliverables

Kinematics derivation, C++ build manifest, simulation traces, tuning report, sensor interface record, and optional bench evidence clearly labeled physical.

### Assessment criteria

Check known arm poses and finite-difference Jacobians away from singularities. Report rise time, overshoot, steady-state error, and disturbance recovery for declared scenarios. Pass saturation and stale-command tests in simulation before motor commissioning.

## Month 6 — ROS 2 and robot simulation

### Learning objectives

Integrate a robot as timestamped, frame-consistent components and reproduce behavior from launch configurations and recorded messages.

### Mathematical concepts

Transform composition, quaternion normalization, discretized state updates, sampling and latency, closed-loop timing, covariance interpretation.

### Topics and subtopics

ROS 2 nodes, topics/services/actions, QoS, parameters, lifecycle concepts, tf2, URDF/Xacro, robot_state_publisher, rosbag2, simulated time; Gazebo worlds, sensors, plugins and bridges; introductory ros2_control concepts.

### University lectures

Revisit robot-modeling selections in [Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/). Pair them with the [official ROS 2 Jazzy docs](https://docs.ros.org/en/jazzy/) and [Gazebo integration guide](https://gazebosim.org/docs/harmonic/ros_installation/); ROS documentation content was blocked during browsing, as recorded in resources.

### Recommended textbooks

[Modern Robotics](https://modernrobotics.org/) for mechanics and frame reasoning. Official middleware/simulator documentation supplies software-specific material.

### Practical exercises

Build a transform tree by hand; diagnose a deliberately reversed transform. Compare best-effort/reliable sensor delivery in a controlled test. Check sim-time behavior during pause and replay.

### Programming assignment

Create a minimal differential-drive robot model and launch specification/implementation in Gazebo with ROS 2 sensor and velocity interfaces. Include one small `rclcpp` or `rclpy` diagnostic node and bag replay evaluation.

### Hardware or simulation

Simulation is required. Optionally bridge the Month 5 ESP32 telemetry through a host adapter; keep motor authority disabled until integration tests pass.

### Projects and weekly sequence

Advance the [mobile robot](../projects/autonomous-mobile-robot/README.md). W1: messaging. W2: frames/model. W3: simulator/bridge. W4: replay and fault tests.

### Parallel AI engineering

Document the pinned Ubuntu/Jazzy/Harmonic environment, launch parameters, asset hashes, and container/HPC separation in the [container plan](../infrastructure/containers/README.md).

### Expected deliverables

Robot description, node/topic diagram, launch configuration, frame/clock contract, bag manifest, and replay/fault report.

### Assessment criteria

Reproduce a fixed trajectory from a fresh environment. Explain every transform and clock. Pause, drop a command source, and inject stale timestamps; verify the documented stop/fallback behavior. Middleware configuration alone does not prove a physical real-time guarantee.

## Month 7 — Localization, fusion, visual odometry, and SLAM

### Learning objectives

Estimate robot state with uncertainty, distinguish odometry from globally corrected localization, and diagnose mapping/estimation failure.

### Mathematical concepts

Bayes filtering, Gaussian models, EKF linearization, covariance propagation, innovation residuals, particle filters, observability, least-squares pose graphs and gauge freedom.

### Topics and subtopics

Wheel/IMU fusion, sensor calibration and time alignment, visual odometry, scan matching, landmark/occupancy mapping, loop closure, data association, localization against a fixed map.

### University lectures

Select estimation/autonomy material from [Princeton robotics](https://irom-lab.princeton.edu/intro-to-robotics/) and geometry review from [CS231A](https://web.stanford.edu/class/cs231a/). Supplement using the book and the installed SLAM package's documentation.

### Recommended textbooks

[Probabilistic Robotics](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) for filtering/localization/mapping; [Multiple View Geometry](https://www.robots.ox.ac.uk/~vgg/hzbook/) for visual motion geometry.

### Practical exercises

Derive a planar motion/measurement EKF; inspect innovations under incorrect sensor noise. Show unobservable states for a chosen sensor setup. Demonstrate VO failure on low-texture or pure-rotation sequences.

### Programming assignment

Implement a small planar filter and compare against wheel-only odometry, then integrate an established SLAM baseline in the simulator. Evaluate one simple visual-odometry sequence; keep this a bounded comparison rather than a new SLAM framework.

### Hardware or simulation

Use wheel encoder, IMU, camera or simulated lidar streams with independently logged ground truth. Optional recorded hardware data is evaluated offline first.

### Projects and weekly sequence

Advance the [mobile robot](../projects/autonomous-mobile-robot/README.md). W1: filtering. W2: time/calibration and fusion. W3: SLAM/VO. W4: drift and failure analysis.

### Parallel AI engineering

Create replay regression cases and separate estimator inputs from evaluator-only ground truth. Version maps/calibration; monitor timestamp age and dropped messages.

### Expected deliverables

Filter derivation, estimator comparison, trajectory/map references, residual plots, alignment convention, and replay manifest.

### Assessment criteria

Report absolute/relative trajectory error with units, alignment method, and scene conditions. Explain drift, uncertainty, and loop-closure effects. Check covariance symmetry/positive semidefiniteness numerically; show at least one case where the uncertainty model is inadequate.

## Month 8 — Planning and mobile/aerial autonomous systems

### Learning objectives

Turn estimated state into bounded autonomous motion; evaluate navigation under disturbances and establish an aerial simulation baseline.

### Mathematical concepts

Configuration spaces, graph search, A*, sampling-based planning, trajectory constraints, feedback tracking, collision margins, uncertainty-aware decisions; quadrotor state/attitude basics.

### Topics and subtopics

Global/local planning, occupancy/cost maps, replanning, recovery behavior, Nav2 integration; PX4 SITL, offboard/mission interfaces, coordinate conventions, geofence and link-loss concepts.

### University lectures

Select planning/control material from [Princeton robotics](https://irom-lab.princeton.edu/intro-to-robotics/) and [MIT Underactuated Robotics](https://underactuated.mit.edu/). Use [Nav2 Jazzy](https://docs.nav2.org/jazzy/) and [PX4 v1.17 docs](https://docs.px4.io/v1.17/en/) for implementation guidance.

### Recommended textbooks

[Modern Robotics](https://modernrobotics.org/) for planning/control; [Probabilistic Robotics](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/) for uncertainty and localization review.

### Practical exercises

Implement A* on a small grid, compare with Dijkstra, and demonstrate why an inadmissible heuristic can lose optimality. Calculate obstacle inflation from footprint and positioning error. Translate a documented ENU/NED example explicitly.

### Programming assignment

Integrate a mobile planning/tracking baseline and run a small fixed mission suite. Add a bounded PX4 SITL smoke test: takeoff, waypoint/hold, landing, and simulated loss of command source. Keep ground and aerial environments separately pinned.

### Hardware or simulation

Use Gazebo for mobile navigation and PX4-supported simulation for aerial work. No physical autonomous flight is required. Physical ground trials follow the [commissioning gates](../hardware/README.md).

### Projects and weekly sequence

W1: planning algorithms. W2: mobile navigation. W3: PX4 SITL. W4: fault evaluation and primary capstone choice. Projects: [mobile robot](../projects/autonomous-mobile-robot/README.md), [drone simulation](../projects/autonomous-drone/README.md).

### Parallel AI engineering

Log mission state transitions, planner runtime, command age, and recovery reasons. Pin scenes and seeds. Use the following buffer week to reproduce both simulation baselines.

### Expected deliverables

A* checks, mission configurations, mobile report, aerial SITL logs, failure demonstrations, and capstone scope decision.

### Assessment criteria

Compare A* with Dijkstra on known grids. Report mission success denominator, collisions, path length, tracking error, and timeouts across at least ten inexpensive simulated trials. Verify specified stop/hold/land behavior on command loss in simulation before any physical progression.

## Month 9 — Agentic AI and bounded task planning

### Learning objectives

Build an evaluated language-model application that can retrieve evidence and propose robot tasks through constrained interfaces.

### Mathematical concepts

Token probabilities, attention, embedding similarity, retrieval precision/recall, calibration, finite-state machines, task graphs, budgeted sequential decisions.

### Topics and subtopics

LLM inference/prompting, structured output, tool calling, RAG with citations, agent orchestration, retries/timeouts/idempotency, prompt injection through retrieved content, environment state grounding, deterministic fallback planning.

### University lectures

Select transformer/language-model systems material from [Stanford CS336](https://cs336.stanford.edu/). Revisit planning abstractions from [Princeton robotics](https://irom-lab.princeton.edu/intro-to-robotics/). Tool/RAG implementation is an original assignment; no invented university lecture is attributed to it.

### Recommended textbooks

[Deep Learning](https://www.deeplearningbook.org/) for representation/probabilistic foundations and [Modern Robotics](https://modernrobotics.org/) for geometric planning boundaries. Current tool protocols come from the chosen runtime's official documentation when implementation begins.

### Practical exercises

Hand-label a small retrieval set; separate retrieval failure from generation failure. Model a pick/place request as a state machine with preconditions, postconditions, and rejection states.

### Programming assignment

Build a simulated task planner that calls schema-validated tools such as `observe_scene`, `plan_route`, or `request_pick`. Use a mocked/local model path when API access is unavailable. Compare with a scripted planner; language output cannot bypass the executor's limits.

### Hardware or simulation

Use a mocked world first, then the established robot simulator. Tools expose high-level bounded tasks; motor control remains with the existing controller.

### Projects and weekly sequence

Prepare [vision-guided manipulation](../projects/vision-guided-manipulation/README.md) or a mobile task interface. W1: LLM contracts. W2: retrieval. W3: executor/orchestration. W4: adversarial/failure evaluation.

### Parallel AI engineering

Trace tool arguments/results, model/config versions, retrieval IDs, budgets, latency, and cost where applicable. Follow the [agent systems guide](../infrastructure/model-serving/agent-systems.md).

### Expected deliverables

Tool schemas, state-machine diagram, labeled evaluation set, planner/scripted baseline comparison, retrieval evaluation, and replayable tool traces.

### Assessment criteria

Use at least 20 predeclared tasks including invalid arguments, unavailable objects, stale observations, and injected instructions. Report task success, invalid-call/rejection counts, retrieval quality, and resource use. All executor tests must reject out-of-bounds requests and terminate within a bounded budget.

## Month 10 — Embodied AI and learned policies

### Learning objectives

Compare model-based control, imitation learning, and reinforcement learning on a bounded simulated task. Explain what a VLM understands versus what an action policy must specify.

### Mathematical concepts

MDPs/POMDPs, discounted return, Bellman equations, value/policy functions, policy gradients, behavioral cloning loss, covariate shift, action normalization and temporal horizons.

### Topics and subtopics

Vision-language models, vision-language-action interfaces, robot task grounding, demonstrations, behavior cloning, a small RL baseline, reward design/hacking, held-out initial states, sim-to-real limitations.

### University lectures

Select imitation/RL material from [Berkeley CS185/285](https://rail.eecs.berkeley.edu/deeprlcourse/) and dynamics/control context from [MIT Underactuated Robotics](https://underactuated.mit.edu/). Read [OpenVLA](https://openvla.github.io/) as a research case study, not a required large-model training project.

### Recommended textbooks

[Deep Learning](https://www.deeplearningbook.org/) for learning objectives and [Modern Robotics](https://modernrobotics.org/) for policy/control interfaces; supplement with the university notes for RL-specific derivations.

### Practical exercises

Derive a Bellman backup on a tiny MDP. Compare teacher demonstrations with policy rollouts; identify distribution shift. Specify observation/action shapes, units, rates, horizons, and termination rules for a VLA example.

### Programming assignment

Train a small behavior-cloning policy and an inexpensive RL baseline on the same bounded simulator task, comparing both with a scripted controller. Reuse a simple arm reach or navigation environment; cap compute and keep checkpoints outside Git.

### Hardware or simulation

Train/evaluate entirely in simulation. A VLM/VLA paper/interface study suffices if pretrained models exceed available hardware. Do not connect an unevaluated learned policy to actuators.

### Projects and weekly sequence

Extend the [arm](../projects/robotic-arm/README.md) or [manipulation](../projects/vision-guided-manipulation/README.md) simulator. W1: MDP/rollout setup. W2: demonstrations/BC. W3: small RL comparison. W4: held-out evaluation and VLA critique.

### Parallel AI engineering

Version demonstration provenance, episode splits, seeds, policy artifacts, and compute budget. Separate training reward from external task-success evaluation.

### Expected deliverables

MDP/task specification, demonstration manifest, BC/RL/scripted comparison, held-out rollout report, VLA interface critique, and failure clips.

### Assessment criteria

Report success and return separately across at least three seeds for cheap baselines and fixed held-out initial conditions. Explain any reward/success mismatch. Verify action limits and fallback behavior; unsuccessful learning is acceptable only with a reproducible diagnostic and passing interface tests.

## Month 11 — Capstone integration and edge deployment

### Learning objectives

Integrate perception, state estimation, planning, and control for one primary platform; measure deployment tradeoffs on an actual target or explicitly labeled surrogate.

### Mathematical concepts

End-to-end error propagation, latency budgets, control-delay effects, numerical precision/quantization, sampling, paired output comparison and confidence intervals.

### Topics and subtopics

Sensor-to-action contracts, asynchronous queues, stale-state rejection, ONNX export, TensorRT where supported, CPU/GPU/edge profiling, model serving, observability, fallback operation and rollout/rollback.

### University lectures

Revisit relevant planning/control selections in [Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/) and [MIT Underactuated Robotics](https://underactuated.mit.edu/); choose perception review from [CS231n](https://cs231n.stanford.edu/2025/) based on observed failures.

### Recommended textbooks

Use [Szeliski](https://szeliski.org/Book/) for perception error reasoning and [Modern Robotics](https://modernrobotics.org/) for the selected platform. Read to resolve concrete integration questions.

### Practical exercises

Allocate a latency/error budget from sensor capture to actuator command. Measure output drift before/after export and precision changes. Predict how stale observations affect a moving target.

### Programming assignment

Integrate the chosen [capstone project](../projects/README.md), add a replayable end-to-end scenario, and export one working perception/policy component if supported. Compare original and exported outputs on identical held-out inputs before accelerating.

### Hardware or simulation

Use the simulator as the system baseline. Optional ground/arm hardware proceeds through supervised commissioning. Edge alternative: CPU ONNX inference with a documented deployment budget; a desktop GPU is not reported as an edge-device measurement.

### Projects and weekly sequence

W1: freeze architecture/contracts. W2: integration/replay. W3: export/profile. W4: failures and validation freeze. Preserve the smaller arm/mobile/aerial simulation demonstrations from earlier months.

### Parallel AI engineering

Apply the [edge workflow](../infrastructure/edge-deployment/README.md), [serving contract](../infrastructure/model-serving/README.md), and [observability plan](../infrastructure/observability.md).

### Expected deliverables

Integrated architecture, model/runtime manifest, parity report, latency/memory/power observations where measurable, commissioning record, and frozen Month 12 scenario suite.

### Assessment criteria

Reproduce the reference scenario and report component plus end-to-end latency percentiles under a declared load. Pass predeclared parity tolerances on task metrics and outputs. Demonstrate stale-input/overload fallback. If target hardware is unavailable, identify all unvalidated deployment claims.

## Month 12 — Capstone validation and technical publication

### Learning objectives

Demonstrate a reproducible autonomous system, explain its limits with evidence, and prepare material another engineer can review and extend.

### Mathematical concepts

Sampling uncertainty, paired baseline comparisons, binomial success estimates, error budgets, reliability/failure categories, estimator/controller sensitivity.

### Topics and subtopics

Frozen scenario evaluation, system regression, ablation, robustness to sensor/communication faults, release manifests, runbooks, architecture decisions, media provenance and technical communication.

### University lectures

Review specific conceptual gaps in [Princeton robotics](https://irom-lab.princeton.edu/intro-to-robotics/), [Modern Robotics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/), or [MIT Underactuated Robotics](https://underactuated.mit.edu/). No new full university course is added during validation.

### Recommended textbooks

Use the platform-relevant sections of [Probabilistic Robotics](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/), [Modern Robotics](https://modernrobotics.org/), and [Szeliski](https://szeliski.org/Book/) to support the final design analysis.

### Practical exercises

Audit one successful and one failed mission from raw observations to decisions. Reproduce a result after restoring a clean environment. Perform an ablation that tests a stated architectural assumption.

### Programming assignment

Package the main capstone with launch/run/evaluate commands, frozen configuration, artifact acquisition instructions, and a regression suite. Make one small simulated demonstration available for each secondary platform rather than attempting three new builds.

### Hardware or simulation

Repeat simulated missions with faults and varied seeds. Include physical ground/arm demonstrations only after their gates pass and identify them separately. Drone evidence remains simulation-first; physical flight is outside the core requirement.

### Projects and weekly sequence

W1: frozen suite execution. W2: ablation and failure investigation. W3: clean reproduction and secondary demos. W4: report/video/release review. Final buffer week is reserved for reproduction failures.

### Parallel AI engineering

Finalize deployment/rollback instructions, telemetry interpretation, artifact checksums, environment manifests, and operational limits. Verify the documentation automation against the release candidate.

### Expected deliverables

Capstone report, architecture/decision records, complete evaluation tables with denominators, failure taxonomy, short labeled video, reproducibility runbook, and evidence-linked roadmap/journal updates.

### Assessment criteria

Run at least 20 inexpensive frozen simulated missions for the primary system, reporting success intervals and all failures; do not imply this establishes production reliability. Compare the baseline and chosen ablation on the same scenarios. A clean checkout plus documented external artifacts must reproduce a representative run. State which mathematical, software, physical, and deployment claims remain unvalidated.
