# LLM tools, RAG, and agent orchestration

The Month 9 assignment builds a bounded task planner, using your service architecture experience for schemas, state, traces, and failure handling. A framework is optional; a small explicit state machine is a valid starting point.

## Tool design

Expose high-level operations such as observation, route planning, and a checked manipulation request. Specify request ID, argument schema, units/frame, freshness, preconditions, timeout, permitted workspace, and result/failure schema. Validate at the executor independently of model output. Motion limits and command expiry remain enforced below the task layer.

Retries must be bounded and idempotent for task requests. Record accepted/rejected arguments and structured failure reasons. Treat retrieved text, camera text, and tool output as data; they cannot redefine tool authority or executor limits.

## RAG evaluation

Start with a small versioned corpus of original robot/environment documentation. Label retrieval questions and relevant evidence IDs. Evaluate retrieval precision/recall separately from answer correctness and final task success. Require citations to retrieved evidence and preserve corpus/chunk/embedding versions.

## Orchestration evaluation

Compare against a scripted planner using the same predeclared tasks. Include impossible goals, unavailable objects, stale scenes, malformed tool calls, retrieval injection, and timeout cases. A mocked/local model path allows evaluation without a paid API.

Trace model/prompt/config version, input/observation IDs, retrieved evidence, tool arguments/results, state transitions, token/step/time budgets, and cost where applicable. Report rejection counts and failures as well as success. Terminate after bounded attempts and hand control to the deterministic fallback.

Use [CS336](https://cs336.stanford.edu/) for selected language-model foundations; provider/framework API details must be taken from the actual chosen runtime's current official documentation during implementation.
