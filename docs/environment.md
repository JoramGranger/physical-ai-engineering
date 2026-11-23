# Development environment

## Documentation baseline

Repository checks need only Python 3.12+ and Git. No ML framework, GPU, ROS installation, account, or paid service is required to review the initial repository.

```bash
python3 --version
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -v
```

Run these commands from the repository root. CI uses Python 3.12. There is deliberately no universal requirements file: training, ROS, firmware, and edge runtimes have different dependency and hardware constraints.

## Workload environments

| Workload | Starting choice | Record before running |
| --- | --- | --- |
| Numerical work | Isolated Python environment, NumPy when needed | Python/library versions and numerical precision |
| Training | PyTorch installation selected for the actual CPU/GPU | GPU model, driver, runtime, package lock, seeds |
| Robotics | Ubuntu 24.04, ROS 2 Jazzy, Gazebo Harmonic | OS image, package versions, simulator world/seed |
| Embedded work | ESP-IDF for the actual ESP32 board | Board/SoC revision, SDK, wiring and firmware hash |
| Aerial simulation | PX4 versioned release and supported simulator | Firmware commit, airframe, simulator and bridge versions |
| Edge inference | Target-compatible ONNX runtime / TensorRT | Device OS/SDK, opset, precision, calibration, power mode |

The robotics baseline is an intentional compatible combination, supported by the [official Jazzy announcement](https://www.openrobotics.org/blog/2024/5/ros-jazzy-jalisco-released) and [Gazebo compatibility guide](https://gazebosim.org/docs/harmonic/ros_installation/). It is not a claim to use every newest release. Follow the selected release's official installation instructions from the [resource register](resources.md).

Keep PX4 simulation separate from the ground-robot environment unless their simulator and middleware versions have been demonstrated compatible. A documentation link does not establish an integrated software environment.

## Reproducible run contract

Each executable project should gain its own dependency lock/manifest and documented entry point when implementation starts. Record the commit, dirty-tree status, exact command, input hashes, configuration, seed, hardware, elapsed time, and artifact locations. Use the [experiment template](../experiments/TEMPLATE.md).

Start on CPU with a small deterministic example. Move to a GPU after correctness checks. On HPC, separate job scheduling, data staging, and container execution; do not assume cluster driver/container combinations match your workstation.

Do not commit private `.env` files, weights, datasets, bag files, or credentials. Use a documented external artifact location and checksums. Store small original text configurations and summaries in Git. Hardware-free alternatives are included in each month of the [curriculum](curriculum.md).
