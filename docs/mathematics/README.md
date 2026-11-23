# Mathematics for physical intelligence

Use mathematics to predict behavior, implement a model, and test assumptions. Read selectively from [Mathematics for Machine Learning](https://mml-book.github.io/); keep original derivations here and numerical work alongside the relevant assignment.

| Stage | Essential ideas | Engineering check |
| --- | --- | --- |
| M1–2 | Vector spaces, least squares, SVD, derivatives, probability, optimization | Gradient check; ill-conditioned design matrix; calibrated classifier |
| M3–4 | Convolution, homogeneous coordinates, projective geometry, robust estimation | Image/filter boundary effects; reprojection residual; degenerate triangulation |
| M5–6 | SO(3), SE(3), Jacobians, differential equations, discrete control | Transform inverse/composition; finite-difference Jacobian; timestep sensitivity |
| M7–8 | Bayes filters, covariance, graph optimization, planning | Innovation residuals; unobservable states; independent trajectory evaluation |
| M9–10 | Attention, retrieval similarity, MDPs, Bellman equations, policy gradients | Tool decision calibration; reward/return distinction; held-out rollout tests |
| M11–12 | Error propagation, numerical precision, statistics, system identification | Sensor-to-action error budget; paired deployment parity; repeated mission trials |

## Working conventions

Use SI units unless explicitly converted. Distances are meters, angles radians, and timestamps state their clock. Define every frame and transform before multiplying matrices. Use `T_A_B` to map coordinates from frame B into frame A: `p_A = T_A_B p_B`. Composition is `T_A_C = T_A_B T_B_C`.

For column-vector pinhole geometry, `s [u,v,1]^T = K [R|t] [X,Y,Z,1]^T`, with `[R|t]` mapping world points into the camera frame. Check positive camera depth and distinguish camera pose from the world-to-camera extrinsic transform.

For gradient checking, compare analytic gradients to central differences at several step sizes. For scalar `f`, approximate component i as `(f(x + h e_i) - f(x - h e_i)) / (2h)`. Avoid nondifferentiable points and report absolute and relative errors; cancellation makes very small h unreliable.

## Derivation acceptance

Each note should state the question, assumptions, symbols/shapes, derivation, limiting case, numerical verification, and failure case. An equation copied from a source without these checks is reading evidence, not mastery.

First note: derive the gradient of mean squared error for `X` of shape `(n,d)` and weights `(d,)`, compare normal-equation and iterative solutions, and explain why a linear solve or QR/SVD is preferable to explicitly forming a matrix inverse.
