# Experiment records

An experiment answers a bounded engineering question with reproducible evidence. This directory contains the protocol and template; no experiments have been run at initialization.

Copy [TEMPLATE.md](TEMPLATE.md) to a dated topic file when starting work, for example `YYYY-MM-DD-stereo-baseline.md`. Keep configurations/scripts with their owning course or project; link them here by commit/path. Use an immutable run ID for external artifacts.

State the hypothesis, baseline, independent variable, controlled conditions, and acceptance rule before running. Record unsuccessful trials and changes to the protocol. Avoid changing several variables at once unless the question explicitly requires it.

Commit small original text configuration, summaries, and analysis. Store images/video, datasets, weights, bag/flight logs, point clouds, and large profiling traces outside Git with hashes and acquisition instructions. Public artifact locations must not expose credentials or private recordings.

Close an experiment with a measured result, limitations, and a decision. Link it from the [learning journal](../docs/learning-journal.md) and the relevant project. A planned table without observations is not experimental evidence.
