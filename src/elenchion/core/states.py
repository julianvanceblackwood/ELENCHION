"""Semantic state dimensions used by ELENCHION."""

from enum import Enum, unique


@unique
class EpistemicState(Enum):
    """Describes how strongly a claim is supported."""

    OBSERVED = "OBSERVED"
    DERIVED = "DERIVED"
    INFERRED = "INFERRED"
    HYPOTHESIZED = "HYPOTHESIZED"
    CONTRADICTED = "CONTRADICTED"
    UNKNOWN = "UNKNOWN"


@unique
class ObservationState(Enum):
    """Describes the collection state for an observation domain."""

    AVAILABLE = "AVAILABLE"
    NOT_COLLECTED = "NOT_COLLECTED"
    PARTIALLY_COLLECTED = "PARTIALLY_COLLECTED"
    COLLECTION_FAILED = "COLLECTION_FAILED"
    UNOBSERVABLE = "UNOBSERVABLE"
    UNKNOWN_COVERAGE = "UNKNOWN_COVERAGE"


@unique
class SourceTrustState(Enum):
    """Describes whether a source can support claims within a scope."""

    TRUSTED_FOR_SCOPE = "TRUSTED_FOR_SCOPE"
    DEGRADED = "DEGRADED"
    UNTRUSTED = "UNTRUSTED"
    UNKNOWN = "UNKNOWN"