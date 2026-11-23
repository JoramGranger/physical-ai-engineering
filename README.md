# Physical AI Engineering

A 12-month, engineering-focused path from mathematical foundations to intelligent physical systems: perception, state estimation, planning, control, and learned decision-making.

Designed for an experienced Python/backend engineer comfortable with Linux, GPUs, HPC, and containers. The work concentrates on mathematics, AI algorithms, computer vision, robotics, hardware integration, and reproducible evaluation.

**Status:** repository initialized with curriculum, project specifications, engineering guides, and documentation automation. Learning milestones and project implementations are planned; no experimental results are claimed.

## Start here

1. Read the [roadmap](ROADMAP.md) for milestones and the 15–18 hour weekly commitment.
2. Follow the [monthly curriculum](docs/curriculum.md), beginning with the Month 1 diagnostic.
3. Use the [verified resource catalog](docs/resources.md) to select readings and lectures.
4. Set up the [development environment](docs/environment.md) and begin the [learning journal](docs/learning-journal.md).
5. Complete each month's assessment before increasing system complexity.

## Learning path

| Months | Focus | Evidence produced |
| --- | --- | --- |
| 1–2 | Mathematics, machine learning, deep learning | Derivations, numerical checks, reproducible classifier |
| 3–4 | Computer vision, camera geometry, 3D perception | Detection/tracking evaluation, calibrated reconstruction |
| 5–6 | Kinematics, dynamics, control, C++, ROS 2, Gazebo | Tested robot model, simulated closed-loop control |
| 7–8 | Localization, SLAM, planning, mobile and aerial autonomy | Navigation benchmark, PX4 simulation logs |
| 9–10 | Agentic AI, multimodal models, reinforcement and imitation learning | Evaluated tool planner and simulated policy |
| 11–12 | Edge deployment and integrated Physical AI capstone | Reproducible system, failure analysis, demonstration |

Training, inference, GPU benchmarking, serving, observability, and deployment run in parallel throughout the year. See the [engineering track](infrastructure/README.md).

## Repository map

```text
physical-ai-engineering/
├── README.md / ROADMAP.md / CONTRIBUTING.md / LICENSE
├── docs/              # Curriculum, journal, resources, mathematical reference
├── courses/           # Eleven bounded study modules and original assignments
├── projects/          # Seven engineering project specifications
├── hardware/          # ESP32, sensors, mobile robots, arms, aerial interfaces
├── infrastructure/    # Training, inference, HPC, serving, containers, edge
├── experiments/       # Run protocol and evidence template
├── assets/            # Media provenance and publication guidance
├── scripts/           # Dependency-free documentation validation
├── tests/             # Validator regression tests
└── .github/           # Issue/PR templates and CI
```

[Courses](courses/README.md) contain study plans and exercises. [Projects](projects/README.md) combine those skills into systems. [Experiments](experiments/README.md) record measured evidence. Hardware and infrastructure documents describe integration and operating constraints.

## Working agreement

Use simulation before autonomous motion. Introduce physical hardware through supervised sensor acquisition and constrained motor tests. See the [hardware progression](hardware/README.md) for commissioning gates.

Record dataset provenance, frame conventions, units, software versions, seeds, and test conditions. Distinguish proposed targets from observations. Keep datasets, weights, credentials, and large recordings outside Git.

Validate a contribution with Python 3.12 or later:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding work. Original repository content is under the [MIT license](LICENSE); external books, lectures, datasets, and models retain their own licenses.
