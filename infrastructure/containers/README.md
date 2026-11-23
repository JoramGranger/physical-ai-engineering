# Docker and Apptainer environments

Use containers to capture workload dependencies while recording the host/device boundary. Training, ROS simulation, PX4 SITL, and serving should be separate environments until their compatibility has been demonstrated.

## Docker workflow

Choose a workload-compatible base and pin its digest. Record OS, Python/system packages, dependency lock, build arguments, and source commit. Keep data/artifacts mounted externally and credentials out of image layers. Run unprivileged where practical and request only the devices needed for the actual workload.

Separate build-time dependencies from runtime configuration. A robotics container additionally needs an explicit policy for display/rendering, middleware networking, simulated clock, sensors, and device access. Do not assume a generic GPU training image also supplies a working ROS/Gazebo environment.

## Apptainer on HPC

Use the cluster-supported [Apptainer workflow](https://apptainer.org/docs/user/main/) and record the image/SIF hash, bind mounts, GPU passthrough options, writable paths, scheduler environment, and host driver. An OCI source image can inform the environment, but conversion and host-runtime behavior must be tested on the target cluster.

Test a small CPU run, then GPU visibility and a numerical operation, then the representative model job. Scheduler resource requests and data staging remain outside the container. Record both image and host environment; an image hash alone cannot reproduce hardware/runtime behavior.

## First implementation deliverables

Add a workload-specific Dockerfile or Apptainer definition only after selecting its dependency versions and a smoke test. Require clean build, reference output check, artifact write/read, and restart/resume evidence. No untested container definition is supplied at initialization.

See [Docker documentation](https://docs.docker.com/) and the [environment baseline](../../docs/environment.md). Exclude datasets, weights, secrets, and large build contexts explicitly when adding container files.
