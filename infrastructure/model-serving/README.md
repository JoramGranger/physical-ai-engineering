# Model serving and robot-facing inference

Start with a correct offline callable and a fixed input/output contract. Wrap it in FastAPI or an equivalent service only when remote/asynchronous inference is useful. Existing backend experience should support explicit timeout, version, and error behavior.

## Service contract

Define schema version, request ID, model/preprocessing version, input shape/encoding, capture timestamp/clock, frame ID where applicable, and maximum valid age. Return typed outputs with units/coordinates, inference timestamps, validity, and structured errors. Distinguish liveness from readiness and device/model health.

Bound queues and request size; define overload/rejection behavior. Avoid allowing retries to duplicate robot tasks. Separate inference from motion authority: a response cannot issue actuator commands without passing the robot executor/controller contract.

## Deployment sequence

Verify offline parity, then single-request serving, then bounded concurrency and realistic input rate. Measure decoding, queueing, model, and serialization separately. Test invalid inputs, timeout, restart, unavailable model/device, stale observations, and artifact-version mismatch.

Promote immutable model/config bundles with hashes, a small regression fixture, and a rollback path. Load a candidate, pass readiness/parity checks, then switch traffic or task routing through a bounded transition. Preserve the last known working bundle and observable fallback behavior.

Use the [vision inference guide](vision-inference.md), [agent systems guide](agent-systems.md), and [observability plan](../observability.md). The initial repository defines contracts; no deployed endpoint is claimed.
