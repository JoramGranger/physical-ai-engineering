# Assignment: Modeled robot and bounded controller

**Status:** specification. Implementation and measured results are future work.

## Task

Deliver the Month 5 C++ simulation controller and mathematical model. Choose arm position or wheel velocity as the main controlled variable and keep the other model as a small exercise.

## Verification

- Verify kinematics/Jacobians numerically and controller behavior on known trajectories.
- Test joint/velocity limits, stale-command timeout, saturation, and declared disturbance cases before bench work.

## Submission

Provide the derivation/design, runnable command or clearly scoped implementation plan, configuration/version manifest, evaluation evidence, and one failure analysis. Link external artifacts by hash/location rather than committing large files. Use the [experiment record](../../../experiments/TEMPLATE.md).

The corresponding [monthly assessment](../../../docs/curriculum.md) defines required deliverables and gates. Keep proposed thresholds separate from measured results. Hardware trials require the [commissioning progression](../../../hardware/README.md); a simulation-only submission must say so explicitly.
