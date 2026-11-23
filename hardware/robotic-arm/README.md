# Manipulator integration

Start with a simple [simulated arm](../../projects/robotic-arm/README.md). Its kinematics, limits, and controller become the foundation for [vision-guided manipulation](../../projects/vision-guided-manipulation/README.md).

## Platform record

Document joint types/order, link geometry, joint zero/sign, position/velocity/effort limits, payload, gripper interface, controller rate, and mounting. Distinguish model coordinates from vendor encoders. Preserve the transform from robot base to camera/tool frames and state its direction.

## Commissioning sequence

Verify known poses and numerical Jacobians in simulation, including singular and unreachable goals. Validate trajectory limits, collision constraints, stale commands, and stop response. For physical hardware, review power/isolation and start with bounded low-energy individual-joint motion before coordinated trajectories.

Camera-guided motion additionally requires hand-eye/extrinsic calibration, timestamp age limits, pose uncertainty, and outcome verification. A detected object center is not automatically a feasible collision-free grasp.

## Required evidence

Record the robot model and calibration versions, joint/mounting checks, controller settings, constrained workspace, stop behavior, and simulation versus physical results separately. Use the [hardware gates](../README.md). Large payload, high-speed, or uncommissioned autonomous operation is outside the core setup.

Without an arm, simulated reach and pick/place with known geometry satisfy the learning path. Do not claim force/torque or contact realism unless the chosen simulator/model supports and validates it.
