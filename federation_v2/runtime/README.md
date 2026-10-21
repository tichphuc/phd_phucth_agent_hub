# Runtime

Runtime layer for Meow v2.

This folder contains the minimal code that enforces the Markdown specs in `agent_hub/federation_v2/`.

## Responsibilities

* load the phase 8 scope and routing specs
* classify tasks
* route tasks to `FAST`, `GUIDED`, or `FULL`
* evaluate gates in fail-closed mode
* evaluate action policy
* hand off to an executor adapter
* record audit data
* compute lightweight soft scores for task risk and scope confidence

## Soft scoring

Runtime uses two advisory scores:

* `task_risk_score` in `0..100`
* `scope_confidence` in `0.0..1.0`

These scores are not absolute. They only help the runtime explain why a task routes one way or another.

If the runtime is unsure, or `scope_confidence` is low, it must ask the User instead of guessing.

## Source of truth

* `activation/PARTIAL_ACTIVATION.md`
* `core/TASK_ROUTING.md`
* `core/GATE_PROTOCOL.md`
* `schemas/ACTION_POLICY_SCHEMA.md`
* `OPERATING_PROTOCOL.md`

Runtime code does not replace those files. It enforces them.
