# Research Gate 0 Epistemic Boundaries

## Status

**Research specification provisional**

This document defines the initial semantic boundaries that Research Gate 0 must preserve before implementation is accepted.

It does not claim that ELENCHION currently implements these semantics.

---

## 1. Purpose

Execution-analysis systems observe only part of reality.

ELENCHION therefore separates:

```text
Reality
↓
Observation
↓
Record
↓
Evidence
↓
Claim
↓
Epistemic State
```

These layers must not silently collapse into one another.

The central rule is:

> **What happened, what was observed, what was recorded, and what can be defensibly claimed are different questions.**

---

## 2. Reality

Reality represents the underlying event or state that actually occurred.

Example proposition:

```text
Process P wrote File F.
```

Whether this proposition is true is independent of whether ELENCHION observed it.

Conceptually:

```text
Reality(P) ∈ {TRUE, FALSE}
```

This truth value is not assumed to be directly accessible.

---

## 3. Observation

An observation is information produced by an observation mechanism about a phenomenon.

Example:

```text
Sensor S17 reports a file-write operation
associated with Process P and File F.
```

An observation is not identical to truth.

Possible failure modes include:

* sensor defects;
* incomplete capability;
* event loss;
* incorrect attribution;
* timing errors;
* configuration errors;
* duplicate events;
* corruption.

Therefore:

```text
Observed(E)
≠
True(E)
```

---

## 4. Record

A record is a persisted or transmitted representation of an observation.

The conceptual path may contain multiple failure boundaries:

```text
Reality
↓
Sensor
↓
Observation
↓
Buffer
↓
Transport
↓
Parser
↓
Storage
↓
Record
```

An observation may occur without surviving into the final stored dataset.

Therefore:

```text
Observation exists
```

does not imply:

```text
Record exists
```

and:

```text
Record absent
```

does not imply:

```text
Observation absent
```

---

## 5. Evidence

Evidence is information or an artifact used to support, weaken, or contradict a claim.

Evidence is not represented as an isolated value.

Useful evidence must preserve enough provenance to answer questions such as:

```text
Who produced it?
Which sensor produced it?
What was the sensor capable of observing?
What was its health state?
When was it produced?
Which clock was used?
Which environment produced it?
Was it transformed?
Which parser or engine version processed it?
Can the original observation be recovered?
```

The initial invariant is:

> **No claim without provenance.**

---

## 6. Claim

A claim is a proposition asserted about an execution.

Example:

```text
Process P wrote File F.
```

Evidence may support a claim:

```text
Evidence
↓
SUPPORTS
↓
Claim
```

Evidence may also contradict a claim:

```text
Evidence
↓
CONTRADICTS
↓
Claim
```

A claim is therefore not identical to its supporting evidence.

---

## 7. Truth and Epistemic State Are Different Dimensions

Truth concerns the underlying world.

Epistemic state concerns what the available evidence justifies.

Example:

```text
Reality:
Process P wrote File F.

Truth:
TRUE

Available evidence:
insufficient

Epistemic result:
UNKNOWN
```

This state is valid.

Therefore:

```text
Truth(E) = TRUE
```

may coexist with:

```text
EpistemicState(E) = UNKNOWN
```

The system must not treat its epistemic state as direct access to reality.

---

## 8. UNKNOWN Is Not Failure

`UNKNOWN` describes an information state.

`FAILURE` describes a system or collection condition.

Example:

```text
Sensor collection:
FAILED

Resulting knowledge:
UNKNOWN
```

Therefore:

```text
FAILURE
≠
UNKNOWN
```

although failure may cause an unknown epistemic result.

A justified `UNKNOWN` is preferable to unsupported certainty.

---

## 9. Absence of Observation Is Not Automatically Evidence of Absence

The following statements are not equivalent:

```text
Event E was not observed.
```

and:

```text
Event E did not occur.
```

Missing telemetry may mean:

```text
E did not occur.

or

E occurred but the sensor could not observe it.

or

E occurred but collection was disabled.

or

E occurred but the event was lost.

or

E occurred outside the observed interval.

or

E occurred but persistence failed.

or

coverage is unknown.
```

Therefore:

```text
NOT_OBSERVED(E)
```

must not automatically become:

```text
NOT_OCCURRED(E)
```

---

## 10. Conditions for Negative Evidence

Silence may become meaningful negative evidence only when the relevant observation boundary is sufficiently constrained.

Candidate requirements include:

* the sensor is capable of observing the phenomenon;
* collection was active;
* collection health is known;
* the relevant interval is known;
* event-loss bounds are acceptable;
* the observation scope is appropriate;
* source trust is sufficient.

Conceptually:

```text
No observation
+
Known capability
+
Known collection health
+
Defined time interval
+
Sufficient coverage
────────────────────────
Potential negative evidence
```

The exact semantics remain under research.

---

## 11. Independent Semantic Dimensions

Research Gate 0 must preserve at least three distinct dimensions.

### Epistemic State

Describes the support relationship between evidence and claim.

Candidate states:

```text
OBSERVED
DERIVED
INFERRED
HYPOTHESIZED
CONTRADICTED
UNKNOWN
```

### Observation State

Describes collection and visibility.

Candidate states:

```text
AVAILABLE
NOT_COLLECTED
PARTIALLY_COLLECTED
COLLECTION_FAILED
UNOBSERVABLE
UNKNOWN_COVERAGE
```

### Source Trust State

Describes whether a source can support conclusions within a scope.

Candidate states:

```text
TRUSTED_FOR_SCOPE
DEGRADED
UNTRUSTED
UNKNOWN
```

These dimensions must not be collapsed into one generic `status` field.

---

## 12. Initial Invariants

Research Gate 0 should test the following invariants.

### Invariant 1

Missing telemetry from an incapable sensor must not become evidence that the event did not occur.

### Invariant 2

Collection failure must remain distinguishable from event absence.

### Invariant 3

Direct observation must remain distinguishable from inference.

### Invariant 4

Contradictory evidence must be preserved.

### Invariant 5

`UNKNOWN` must be a valid final result.

### Invariant 6

Every claim must expose the evidence sources on which it depends.

### Invariant 7

Evidence source degradation must be capable of weakening dependent claims.

---

## 13. Controlled Research Scenario

The first microexperiment will compare three sensor profiles.

```text
Sensor A
capable
healthy
complete for experiment scope

Sensor B
capable
degraded
selected observations intentionally lost

Sensor C
incapable of observing one event class
```

The experiment must demonstrate that identical-looking missing telemetry can represent different epistemic conditions.

---

## 14. Falsification Direction

The current model should be revised if:

* the state dimensions cannot be kept semantically distinct;
* the model requires ad-hoc exceptions for every missing-observation case;
* provenance does not materially affect claim evaluation;
* sensor capability does not change the interpretation of silence;
* degraded collection cannot be propagated into dependent reasoning;
* the model produces certainty where the controlled experiment requires `UNKNOWN`.

Failure to satisfy these conditions is evidence against the current model.

---

## 15. Current Boundary

This document defines semantics only.

It does not yet define:

* Python classes;
* serialization formats;
* database schemas;
* graph schemas;
* APIs;
* production architecture;
* confidence scores;
* probabilistic models;
* malware execution infrastructure.

Those decisions remain downstream of the research evidence.

---

## Final Principle

> **Observation is not truth. A record is not automatically evidence. Evidence is not automatically knowledge. A claim is only as defensible as the provenance and observation boundaries that support it.**
