from __future__ import annotations

from .classifier import classify_risk_level, classify_task_class
from .loader import RuntimeSpecBundle
from .models import RouteDecision, RouteKind, RiskLevel, TaskClass, TaskInput


def route_task(task: TaskInput, specs: RuntimeSpecBundle) -> RouteDecision:
    task_class = task.task_class or classify_task_class(task.text)
    risk_level = task.risk_level or classify_risk_level(task.text, task_class)

    if task_class in {TaskClass.MUTATION, TaskClass.SCIENCE, TaskClass.GOVERNANCE, TaskClass.RISK}:
        return RouteDecision(
            route=RouteKind.FULL,
            scope_match=False,
            reason=f"{task_class.value} always uses FULL gate",
            escalate=True,
        )

    scope_route = specs.activation_scope.get((task_class, risk_level))
    if scope_route is not None:
        return RouteDecision(
            route=scope_route,
            scope_match=True,
            reason=f"matched Phase 8 scope for {task_class.value} + {risk_level.value}",
            escalate=False,
        )

    if task_class is TaskClass.UNKNOWN:
        return RouteDecision(
            route=RouteKind.STOP,
            scope_match=False,
            reason="task class is unknown; ask User",
            escalate=True,
        )

    if risk_level == RiskLevel.HIGH:
        return RouteDecision(
            route=RouteKind.FULL,
            scope_match=False,
            reason="high-risk task must use FULL gate",
            escalate=True,
        )

    return RouteDecision(
        route=RouteKind.FULL,
        scope_match=False,
        reason="task is outside Phase 8 partial activation scope",
        escalate=False,
    )

