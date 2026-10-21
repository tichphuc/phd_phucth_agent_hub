from __future__ import annotations

from .models import ActionRequest, ActionType, PolicyDecision, PolicyOutcome, RiskLevel


def evaluate_action_policy(action: ActionRequest | None) -> PolicyOutcome:
    if action is None:
        return PolicyOutcome(decision=PolicyDecision.ALLOW, reason="no action requested")

    if action.action_type is ActionType.READ:
        return PolicyOutcome(decision=PolicyDecision.ALLOW, reason="read action is low risk")

    if action.action_type in {ActionType.WRITE, ActionType.MOVE}:
        if action.consented:
            return PolicyOutcome(
                decision=PolicyDecision.ALLOW_WITH_CONSENT,
                reason="write/move allowed only with explicit consent",
                needs_inspection=False,
            )
        return PolicyOutcome(
            decision=PolicyDecision.REQUIRE_INSPECTION,
            reason="write/move needs consent and review",
            needs_inspection=True,
        )

    if action.action_type in {ActionType.DELETE, ActionType.RUN, ActionType.INSTALL, ActionType.NETWORK, ActionType.NOTEBOOK_EXECUTE}:
        if action.consented and action.risk_level in {RiskLevel.LOW, RiskLevel.MEDIUM}:
            return PolicyOutcome(
                decision=PolicyDecision.REQUIRE_INSPECTION,
                reason="high-impact action requires inspection even with consent",
                needs_inspection=True,
            )
        return PolicyOutcome(
            decision=PolicyDecision.BLOCK,
            reason="high-impact action blocked until explicit consent and inspection",
            needs_inspection=True,
        )

    return PolicyOutcome(
        decision=PolicyDecision.BLOCK,
        reason="unknown action type",
        needs_inspection=False,
    )

