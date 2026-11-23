# GPU computing and training

Start with a correct CPU/small-model reference, then move to GPU profiling. Your HPC experience supports scheduler/container/data staging; the learning work is to measure model behavior and performance without mixing confounding variables.

- [Training workflow](training.md): data contracts, diagnostics, checkpoint state, run manifests.
- [Benchmarking protocol](benchmarking.md): warmup, synchronization, sample design, distributed tradeoffs.

Record device/driver/runtime and package versions together. A GPU being visible does not establish framework compatibility, numerical parity, or a useful end-to-end speedup. Match [PyTorch documentation](https://docs.pytorch.org/tutorials/) to the installed version.
