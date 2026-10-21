from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from .audit import AuditLogger
from .classifier import (
    classify_risk_level,
    classify_task_class,
    classify_topic,
    score_scope_confidence,
    score_task_risk,
)
from .config import resolve_runtime_paths
from .executor import ExecutorAdapter
from .gates import evaluate_gates
from .loader import RuntimeSpecBundle, load_runtime_specs
from .models import (
    ActionRequest,
    AuditRecord,
    ExecutionOutcome,
    GateDecision,
    GateResult,
    PolicyDecision,
    RuntimeDecision,
    TaskClass,
    TaskInput,
)
from .policy import evaluate_action_policy
from .router import route_task


class RuntimeEngine:
    def __init__(
        self,
        *,
        base_dir: str | Path | None = None,
        audit_log_path: str | Path | None = None,
        handlers=None,
    ) -> None:
        self.paths = resolve_runtime_paths(base_dir)
        self.specs: RuntimeSpecBundle = load_runtime_specs(base_dir)
        self.audit = AuditLogger(audit_log_path)
        self.executor = ExecutorAdapter(handlers)

    def evaluate(self, task: TaskInput) -> RuntimeDecision:
        task_class = task.task_class or classify_task_class(task.text)
        topic = task.topic or classify_topic(task.text)
        risk_level = task.risk_level or classify_risk_level(task.text, task_class)
        task_risk_score = int(task.metadata.get("task_risk_score") or score_task_risk(task, task_class, risk_level))
        scope_confidence = float(task.metadata.get("scope_confidence") or score_scope_confidence(task, task_class, risk_level))
        normalized_metadata = dict(task.metadata)
        normalized_metadata.update(
            {
                "task_risk_score": task_risk_score,
                "scope_confidence": scope_confidence,
            }
        )
        normalized_task = replace(
            task,
            task_class=task_class,
            topic=topic,
            risk_level=risk_level,
            metadata=normalized_metadata,
        )

        route = route_task(normalized_task, self.specs)
        gate = evaluate_gates(normalized_task, route, self.specs)
        policy = evaluate_action_policy(normalized_task.requested_action)

        notes: list[str] = []
        if scope_confidence < 0.6 and gate.result is GateResult.PASS:
            gate = GateDecision(
                result=GateResult.ASK_USER,
                failed_gate="GATE-SCOPE",
                reason=f"scope confidence too low ({scope_confidence:.2f}); ask User",
            )
            notes.append("soft score is advisory; low confidence always asks User")

        can_proceed = gate.result is GateResult.PASS and policy.decision in {
            PolicyDecision.ALLOW,
            PolicyDecision.ALLOW_WITH_CONSENT,
        }
        rollback_trigger = gate.result in {GateResult.STOP, GateResult.ESCALATE} or policy.decision is PolicyDecision.BLOCK

        execution = None
        next_action = "stop"
        if can_proceed:
            execution = self.executor.execute(normalized_task.requested_action, policy)
            next_action = "execute" if execution.status == "noop" or execution.status == "executed" else "audit"
        elif gate.result is GateResult.ASK_USER or policy.decision is PolicyDecision.REQUIRE_INSPECTION:
            next_action = "ask_user"
        elif gate.result is GateResult.ESCALATE:
            next_action = "escalate"

        decision = RuntimeDecision(
            task=normalized_task,
            task_class=task_class,
            topic=topic,
            risk_level=risk_level,
            route=route,
            gate=gate,
            policy=policy,
            execution=execution,
            task_risk_score=task_risk_score,
            scope_confidence=scope_confidence,
            files_read=list(self.specs.files_read),
            can_proceed=can_proceed,
            need_user_confirmation=gate.result is GateResult.ASK_USER or policy.decision is PolicyDecision.ALLOW_WITH_CONSENT,
            rollback_trigger=rollback_trigger,
            next_action=next_action,
            notes=notes,
        )

        self.audit.log(
            AuditRecord.now(
                task_text=normalized_task.text,
                task_class=task_class.value,
                topic=topic,
                risk_level=risk_level.value,
                task_risk_score=task_risk_score,
                scope_confidence=scope_confidence,
                route=route.route.value,
                gate_result=gate.result.value,
                policy_decision=policy.decision.value,
                files_read=list(self.specs.files_read),
                reason=gate.reason or route.reason or policy.reason,
                uncertainty="low" if can_proceed else "medium" if gate.result is GateResult.ASK_USER else "high",
                rollback_trigger=rollback_trigger,
                next_action=next_action,
            )
        )

        return decision


def build_runtime_engine(base_dir: str | Path | None = None, audit_log_path: str | Path | None = None, handlers=None) -> RuntimeEngine:
    return RuntimeEngine(base_dir=base_dir, audit_log_path=audit_log_path, handlers=handlers)


def evaluate_runtime_task(task: TaskInput, base_dir: str | Path | None = None) -> RuntimeDecision:
    return build_runtime_engine(base_dir=base_dir).evaluate(task)
