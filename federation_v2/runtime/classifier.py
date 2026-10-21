from __future__ import annotations

import unicodedata

from .models import ActionType, RiskLevel, TaskClass, TaskInput


QUERY_HINTS = {
    "hoi",
    "what",
    "how",
    "why",
    "explain",
    "giai thich",
    "tom tat",
    "tra cuu",
    "lookup",
    "summarize",
}

ANALYSIS_HINTS = {
    "phan tich",
    "analyze",
    "analyse",
    "ra soat",
    "review",
    "danh gia",
    "so sanh",
    "kiem ke",
    "audit",
    "inspect",
    "assess",
    "check",
    "investigate",
    "examine",
}

MUTATION_HINTS = {
    "sua",
    "tao",
    "xoa",
    "delete",
    "move",
    "rename",
    "write",
    "update",
    "patch",
    "overwrite",
    "modify",
    "change",
    "install",
}

GOVERNANCE_INTENT_HINTS = {
    "activate",
    "approve",
    "enforce",
    "deprecate",
    "archive",
    "set policy",
    "resolve conflict",
    "decide",
}

TOPIC_GOVERNANCE_HINTS = {
    "rule",
    "registry",
    "constitution",
    "authority",
    "protocol",
    "gate",
    "conflict",
    "governance",
}

TOPIC_SCIENCE_HINTS = {
    "scientific",
    "khoa hoc",
    "validation",
    "validate",
    "claim",
    "method",
    "phuong phap",
    "evidence",
    "formula",
    "mo hinh",
    "ket luan",
}

TOPIC_RISK_HINTS = {
    "risk",
    "rui ro",
    "unsafe",
    "danger",
    "security",
    "bao mat",
}

TOPIC_ROUTING_HINTS = {"routing", "route", "router"}
TOPIC_ACTIVATION_HINTS = {"activation", "activate", "partial-active", "scoped"}
TOPIC_RUNTIME_HINTS = {"runtime", "engine", "executor", "policy", "smoke-test", "smoke test"}
TOPIC_MEMO_HINTS = {"memo", "memory", "session"}
TOPIC_TOOL_HINTS = {"tool", "mcp", "action", "install", "run", "notebook"}

TASK_RISK_BASE = {
    TaskClass.QUERY: 5,
    TaskClass.ANALYSIS: 20,
    TaskClass.MUTATION: 70,
    TaskClass.SCIENCE: 75,
    TaskClass.GOVERNANCE: 80,
    TaskClass.RISK: 80,
    TaskClass.UNKNOWN: 40,
}

RISK_LEVEL_BONUS = {
    RiskLevel.LOW: -5,
    RiskLevel.MEDIUM: 5,
    RiskLevel.HIGH: 20,
    RiskLevel.UNKNOWN: 10,
}

ACTION_RISK_BONUS = {
    ActionType.READ: 0,
    ActionType.WRITE: 15,
    ActionType.MOVE: 15,
    ActionType.DELETE: 25,
    ActionType.RUN: 25,
    ActionType.INSTALL: 30,
    ActionType.NETWORK: 25,
    ActionType.NOTEBOOK_EXECUTE: 20,
    ActionType.UNKNOWN: 20,
}


def _normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    return stripped.lower()


def _contains_any(text: str, keywords: set[str]) -> bool:
    normalized_text = _normalize(text)
    return any(_normalize(keyword) in normalized_text for keyword in keywords)


def classify_task_class(text: str) -> TaskClass:
    if _contains_any(text, MUTATION_HINTS):
        return TaskClass.MUTATION
    if _contains_any(text, ANALYSIS_HINTS):
        return TaskClass.ANALYSIS
    if _contains_any(text, QUERY_HINTS):
        return TaskClass.QUERY
    if _contains_any(text, GOVERNANCE_INTENT_HINTS):
        return TaskClass.GOVERNANCE
    if _contains_any(text, TOPIC_SCIENCE_HINTS):
        return TaskClass.SCIENCE
    if _contains_any(text, TOPIC_RISK_HINTS):
        return TaskClass.RISK
    return TaskClass.UNKNOWN


def classify_risk_level(text: str, task_class: TaskClass | None = None) -> RiskLevel:
    if task_class is None:
        task_class = classify_task_class(text)

    if task_class in {TaskClass.MUTATION, TaskClass.SCIENCE, TaskClass.GOVERNANCE, TaskClass.RISK}:
        return RiskLevel.HIGH
    if _contains_any(text, {"high", "risky", "nguy hiem", "nguy hiem"}):
        return RiskLevel.HIGH
    if task_class is TaskClass.ANALYSIS:
        return RiskLevel.MEDIUM
    if task_class is TaskClass.QUERY:
        return RiskLevel.LOW
    return RiskLevel.UNKNOWN


def classify_topic(text: str) -> str:
    normalized = _normalize(text)
    if _contains_any(normalized, TOPIC_ROUTING_HINTS):
        return "ROUTING"
    if _contains_any(normalized, TOPIC_ACTIVATION_HINTS):
        return "ACTIVATION"
    if _contains_any(normalized, TOPIC_GOVERNANCE_HINTS):
        return "GOVERNANCE"
    if _contains_any(normalized, TOPIC_SCIENCE_HINTS):
        return "SCIENCE"
    if _contains_any(normalized, TOPIC_RISK_HINTS):
        return "RISK"
    if _contains_any(normalized, TOPIC_RUNTIME_HINTS):
        return "RUNTIME"
    if _contains_any(normalized, TOPIC_MEMO_HINTS):
        return "MEMO"
    if _contains_any(normalized, TOPIC_TOOL_HINTS):
        return "TOOL_SAFETY"
    return "GENERAL"


def score_task_risk(task: TaskInput, task_class: TaskClass | None = None, risk_level: RiskLevel | None = None) -> int:
    if task_class is None:
        task_class = classify_task_class(task.text)
    if risk_level is None:
        risk_level = classify_risk_level(task.text, task_class)

    score = TASK_RISK_BASE[task_class] + RISK_LEVEL_BONUS[risk_level]

    if task.mutation_requested:
        score += 20
    if task.scientific_claim:
        score += 15
    if task.conflict_detected:
        score += 25

    action = task.requested_action
    if action is not None:
        score += ACTION_RISK_BONUS[action.action_type]
        if action.consented:
            score -= 5

    if task.evidence_files and task.scientific_claim:
        score -= 10
    if task.source_files and task_class in {TaskClass.QUERY, TaskClass.ANALYSIS}:
        score -= 5
    if task.user_confirmed:
        score -= 5

    return max(0, min(100, score))


def score_scope_confidence(task: TaskInput, task_class: TaskClass | None = None, risk_level: RiskLevel | None = None) -> float:
    if task_class is None:
        task_class = classify_task_class(task.text)
    if risk_level is None:
        risk_level = classify_risk_level(task.text, task_class)

    if task_class is TaskClass.UNKNOWN:
        confidence = 0.2
    elif task_class in {TaskClass.QUERY, TaskClass.ANALYSIS}:
        confidence = 0.9 if risk_level in {RiskLevel.LOW, RiskLevel.MEDIUM} else 0.75
    else:
        confidence = 0.55

    if task.topic and task.topic != "GENERAL":
        confidence += 0.03
    if task.conflict_detected:
        confidence -= 0.2
    if task.mutation_requested:
        confidence -= 0.1
    if task.scientific_claim:
        confidence -= 0.1
    if task.requested_action is not None and task.requested_action.action_type is not ActionType.READ:
        confidence -= 0.1
    if task.user_confirmed:
        confidence += 0.05
    if task.source_files:
        confidence += 0.02
    if task.evidence_files:
        confidence += 0.02

    return round(max(0.0, min(1.0, confidence)), 2)
