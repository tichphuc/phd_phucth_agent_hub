from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Callable


class TaskClass(str, Enum):
    QUERY = "QUERY"
    ANALYSIS = "ANALYSIS"
    MUTATION = "MUTATION"
    SCIENCE = "SCIENCE"
    GOVERNANCE = "GOVERNANCE"
    RISK = "RISK"
    UNKNOWN = "UNKNOWN"


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    UNKNOWN = "UNKNOWN"


class RouteKind(str, Enum):
    FAST = "FAST"
    GUIDED = "GUIDED"
    FULL = "FULL"
    STOP = "STOP"


class GateResult(str, Enum):
    PASS = "PASS"
    STOP = "STOP"
    ESCALATE = "ESCALATE"
    ASK_USER = "ASK_USER"


class PolicyDecision(str, Enum):
    ALLOW = "ALLOW"
    ALLOW_WITH_CONSENT = "ALLOW_WITH_CONSENT"
    BLOCK = "BLOCK"
    REQUIRE_INSPECTION = "REQUIRE_INSPECTION"
    DEFER = "DEFER"


class ActionType(str, Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    MOVE = "move"
    RUN = "run"
    INSTALL = "install"
    NETWORK = "network"
    NOTEBOOK_EXECUTE = "notebook-execute"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class ActionRequest:
    action_type: ActionType
    target: str = ""
    description: str = ""
    risk_level: RiskLevel = RiskLevel.UNKNOWN
    consented: bool = False
    requires_inspection: bool = False


@dataclass(slots=True)
class TaskInput:
    text: str
    task_class: TaskClass | None = None
    topic: str | None = None
    risk_level: RiskLevel | None = None
    permission_state: str = "read-only"
    user_confirmed: bool = False
    conflict_detected: bool = False
    scientific_claim: bool = False
    mutation_requested: bool = False
    evidence_files: list[str] = field(default_factory=list)
    source_files: list[str] = field(default_factory=list)
    requested_action: ActionRequest | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RouteDecision:
    route: RouteKind
    scope_match: bool
    reason: str
    escalate: bool = False


@dataclass(slots=True)
class GateDecision:
    result: GateResult
    failed_gate: str | None = None
    reason: str = ""
    required_sources: list[str] = field(default_factory=list)


@dataclass(slots=True)
class PolicyOutcome:
    decision: PolicyDecision
    reason: str = ""
    needs_inspection: bool = False


@dataclass(slots=True)
class ExecutionOutcome:
    status: str
    message: str = ""
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AuditRecord:
    timestamp: str
    task_text: str
    task_class: str
    topic: str
    risk_level: str
    route: str
    gate_result: str
    policy_decision: str
    task_risk_score: int = 0
    scope_confidence: float = 0.0
    files_read: list[str] = field(default_factory=list)
    reason: str = ""
    uncertainty: str = ""
    rollback_trigger: bool = False
    next_action: str = ""

    @classmethod
    def now(cls, **kwargs: Any) -> "AuditRecord":
        return cls(timestamp=datetime.now(timezone.utc).isoformat(), **kwargs)


@dataclass(slots=True)
class RuntimeDecision:
    task: TaskInput
    task_class: TaskClass
    topic: str
    risk_level: RiskLevel
    route: RouteDecision
    gate: GateDecision
    policy: PolicyOutcome | None = None
    execution: ExecutionOutcome | None = None
    task_risk_score: int = 0
    scope_confidence: float = 0.0
    files_read: list[str] = field(default_factory=list)
    can_proceed: bool = False
    need_user_confirmation: bool = False
    rollback_trigger: bool = False
    next_action: str = ""
    notes: list[str] = field(default_factory=list)


ActionHandler = Callable[[ActionRequest], ExecutionOutcome]
