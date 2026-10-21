class RuntimeErrorBase(Exception):
    """Base runtime error."""


class ScopeViolationError(RuntimeErrorBase):
    """Raised when a task falls outside the partial activation scope."""


class GateFailureError(RuntimeErrorBase):
    """Raised when a gate fails closed."""


class PolicyDeniedError(RuntimeErrorBase):
    """Raised when action policy denies execution."""


class MissingSourceError(RuntimeErrorBase):
    """Raised when a required canonical source is missing."""


class RollbackTriggeredError(RuntimeErrorBase):
    """Raised when runtime decides to roll back to read-only mode."""

