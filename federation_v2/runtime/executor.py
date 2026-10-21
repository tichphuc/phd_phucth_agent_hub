from __future__ import annotations

from typing import Mapping

from .models import ActionHandler, ActionRequest, ExecutionOutcome, PolicyOutcome, PolicyDecision


class ExecutorAdapter:
    def __init__(self, handlers: Mapping[str, ActionHandler] | None = None) -> None:
        self._handlers = dict(handlers or {})

    def execute(self, action: ActionRequest | None, policy: PolicyOutcome) -> ExecutionOutcome:
        if action is None:
            return ExecutionOutcome(status="noop", message="no action requested")

        if policy.decision not in {PolicyDecision.ALLOW, PolicyDecision.ALLOW_WITH_CONSENT}:
            return ExecutionOutcome(status="blocked", message=policy.reason)

        handler = self._handlers.get(action.action_type.value)
        if handler is None:
            return ExecutionOutcome(status="noop", message="no handler configured", details={"action": action.action_type.value})

        return handler(action)

