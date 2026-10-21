from __future__ import annotations

from .loader import RuntimeSpecBundle
from .models import GateDecision, GateResult, RouteDecision, RouteKind, TaskClass, TaskInput


def evaluate_gates(task: TaskInput, route: RouteDecision, specs: RuntimeSpecBundle) -> GateDecision:
    if route.route is RouteKind.STOP:
        return GateDecision(result=GateResult.ASK_USER, failed_gate="GATE-SCOPE", reason=route.reason)

    if task.conflict_detected:
        return GateDecision(
            result=GateResult.ESCALATE,
            failed_gate="GATE-INSPECTION",
            reason="conflict detected",
        )

    if task.task_class is TaskClass.UNKNOWN and route.route is not RouteKind.FULL:
        return GateDecision(
            result=GateResult.ASK_USER,
            failed_gate="GATE-SCOPE",
            reason="task class is unknown",
        )

    if route.scope_match and task.mutation_requested:
        return GateDecision(
            result=GateResult.STOP,
            failed_gate="GATE-USER-CONFIRMATION",
            reason="mutation requested inside partial activation scope",
        )

    if task.requested_action is not None and task.requested_action.action_type.value != "read" and not task.user_confirmed:
        return GateDecision(
            result=GateResult.ASK_USER,
            failed_gate="GATE-USER-CONFIRMATION",
            reason="non-read action needs explicit User confirmation",
        )

    if task.scientific_claim and not task.evidence_files:
        return GateDecision(
            result=GateResult.ASK_USER,
            failed_gate="GATE-EVIDENCE",
            reason="scientific claim needs evidence files or explicit User review",
        )

    if route.route is RouteKind.FULL and not task.user_confirmed and task.mutation_requested:
        return GateDecision(
            result=GateResult.ASK_USER,
            failed_gate="GATE-USER-CONFIRMATION",
            reason="FULL gate task needs explicit User confirmation",
        )

    if not specs.files_read:
        return GateDecision(
            result=GateResult.STOP,
            failed_gate="GATE-READ",
            reason="runtime specs could not be loaded",
        )

    return GateDecision(result=GateResult.PASS, reason="all required gates passed")

