from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .config import RuntimePaths, resolve_runtime_paths
from .models import GateResult, RouteKind, TaskClass, RiskLevel


@dataclass(slots=True)
class RuntimeSpecBundle:
    paths: RuntimePaths
    files_read: list[str] = field(default_factory=list)
    activation_scope: dict[tuple[TaskClass, RiskLevel], RouteKind] = field(default_factory=dict)
    route_table: dict[tuple[TaskClass, RiskLevel], RouteKind] = field(default_factory=dict)
    gate_tokens: list[str] = field(default_factory=list)
    action_policy_text: str = ""
    operating_protocol_text: str = ""


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _parse_scope_lines(text: str) -> dict[tuple[TaskClass, RiskLevel], RouteKind]:
    scope: dict[tuple[TaskClass, RiskLevel], RouteKind] = {}
    pattern = re.compile(r"([A-Z]+)\s*\+\s*([A-Z]+)\s*->\s*([A-Z]+)")
    for line in text.splitlines():
        match = pattern.search(line)
        if not match:
            continue
        task_name, risk_name, route_name = match.groups()
        try:
            task_class = TaskClass[task_name]
            risk_level = RiskLevel[risk_name]
            route_kind = RouteKind[route_name]
        except KeyError:
            continue
        scope[(task_class, risk_level)] = route_kind
    return scope


def _parse_routing_lines(text: str) -> dict[tuple[TaskClass, RiskLevel], RouteKind]:
    routing: dict[tuple[TaskClass, RiskLevel], RouteKind] = {}
    pattern = re.compile(r"\|\s*`([A-Z]+)\s*\+\s*([A-Z]+)`\s*\|\s*`([A-Z]+)`")
    for line in text.splitlines():
        match = pattern.search(line)
        if not match:
            continue
        task_name, risk_name, route_name = match.groups()
        try:
            task_class = TaskClass[task_name]
            risk_level = RiskLevel[risk_name]
            route_kind = RouteKind[route_name]
        except KeyError:
            continue
        routing[(task_class, risk_level)] = route_kind
    return routing


def _parse_gate_tokens(text: str) -> list[str]:
    tokens: list[str] = []
    pattern = re.compile(r"`(GATE-[A-Z-]+)`")
    for match in pattern.finditer(text):
        token = match.group(1)
        if token not in tokens:
            tokens.append(token)
    return tokens


def load_runtime_specs(base_dir: str | Path | None = None) -> RuntimeSpecBundle:
    paths = resolve_runtime_paths(base_dir)
    files_read = []

    activation_text = _read_text(paths.activation)
    routing_text = _read_text(paths.routing)
    gate_text = _read_text(paths.gate_protocol)
    action_policy_text = _read_text(paths.action_policy)
    operating_protocol_text = _read_text(paths.operating_protocol)

    files_read.extend(
        [
            str(paths.activation),
            str(paths.routing),
            str(paths.gate_protocol),
            str(paths.action_policy),
            str(paths.operating_protocol),
        ]
    )

    return RuntimeSpecBundle(
        paths=paths,
        files_read=files_read,
        activation_scope=_parse_scope_lines(activation_text),
        route_table=_parse_routing_lines(routing_text),
        gate_tokens=_parse_gate_tokens(gate_text),
        action_policy_text=action_policy_text,
        operating_protocol_text=operating_protocol_text,
    )

