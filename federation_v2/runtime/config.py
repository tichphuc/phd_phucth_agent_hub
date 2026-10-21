from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class RuntimePaths:
    root: Path
    activation: Path
    routing: Path
    gate_protocol: Path
    action_policy: Path
    operating_protocol: Path


def resolve_runtime_paths(base_dir: str | Path | None = None) -> RuntimePaths:
    runtime_dir = Path(base_dir) if base_dir is not None else Path(__file__).resolve().parent
    root = runtime_dir.parent
    return RuntimePaths(
        root=root,
        activation=root / "activation" / "PARTIAL_ACTIVATION.md",
        routing=root / "core" / "TASK_ROUTING.md",
        gate_protocol=root / "core" / "GATE_PROTOCOL.md",
        action_policy=root / "schemas" / "ACTION_POLICY_SCHEMA.md",
        operating_protocol=root / "OPERATING_PROTOCOL.md",
    )

