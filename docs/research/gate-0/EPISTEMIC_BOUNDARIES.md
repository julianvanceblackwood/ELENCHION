# Research Gate 0: Epistemic Boundaries

## Status

**Research specification: provisional**

Companion specification: [Claim Logic and Inference Boundaries](CLAIM_LOGIC.md)

This document defines the initial semantic boundaries that Research Gate 0 must preserve before implementation is accepted.

It does not claim that ELENCHION currently implements these semantics.

The purpose of this specification is to establish the distinction between reality, observation, recorded representation, evidence, claim, and epistemic state before those concepts are encoded into executable software.

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

A system that fails to preserve these boundaries may convert missing telemetry, degraded collection, incomplete visibility, or faulty evidence into unsupported certainty.

Research Gate 0 exists to determine whether making these distinctions explicit materially improves the defensibility of execution analysis.

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

ELENCHION therefore does not treat telemetry as direct access to reality.

Instead, reality is approached through observation mechanisms that may themselves have capability limits, failure modes, uncertainty, transformation boundaries, and trust dependencies.

This distinction is fundamental:

```text
Reality
≠
Observation of Reality
```

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

```text
sensor defects
incomplete capability
event loss
incorrect attribution
timing errors
configuration errors
duplicate events
corruption
collection interruption
observer effects
```

Therefore:

```text
Observed(E)
≠
True(E)
```

An observation can correctly represent an event.

An observation can also be incomplete, misleading, duplicated, corrupted, misattributed, or produced under conditions that limit its evidential value.

Observation must therefore remain a first-class semantic layer rather than being collapsed directly into a claim.

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

A record may also differ from the original observation because of:

```text
serialization
normalization
parsing
aggregation
filtering
deduplication
timestamp conversion
schema transformation
storage failure
```

ELENCHION must therefore preserve enough provenance to distinguish an original observation from its recorded or transformed representations.

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

What configuration was active?

When was it produced?

Which clock domain was used?

Which environment produced it?

Was it transformed?

Which parser or engine version processed it?

Can the original observation be recovered?

Was information lost during collection or transformation?

Which later claims depend on it?
```

The initial invariant is:

> **No claim without provenance.**

This means that a material claim should eventually be traceable backward through the evidence chain that supports it.

Conceptually:

```text
Claim
↓
Evidence
↓
Record
↓
Observation
↓
Sensor
↓
Capability
↓
Health
↓
Configuration
↓
Environment
```

The exact production representation remains outside the current research boundary.

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

Multiple evidence sources may support the same claim.

Multiple evidence sources may disagree.

A claim may also remain unsupported or insufficiently supported.

ELENCHION must preserve these distinctions instead of normalizing them into a single apparently certain result.

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

The reverse conceptual situation is also possible.

A system may possess evidence that strongly appears to support a proposition even when the proposition is not actually true.

Therefore:

```text
EvidenceSupport(E)
≠
Truth(E)
```

The system must never treat its epistemic state as direct access to reality.

---

## 8. UNKNOWN Is Not Failure

`UNKNOWN` describes an information state.

`FAILURE` describes a system, sensor, collection, transformation, or processing condition.

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

ELENCHION must therefore allow:

```text
UNKNOWN
```

to remain a legitimate final result when available evidence does not justify a stronger state.

The system should eventually be able to explain why the result is unknown.

For example:

```text
UNKNOWN because:

collection failed

or

sensor capability was insufficient

or

coverage was incomplete

or

evidence sources contradicted one another

or

the relevant interval cannot be bounded
```

This converts uncertainty from an implicit weakness into an explicit part of the evidence model.

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

E occurred but a transformation removed or corrupted the record.

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

This is one of the central Research Gate 0 constraints.

The absence of telemetry is itself an observation condition that requires interpretation.

It is not automatically a conclusion about reality.

---

## 10. Conditions for Negative Evidence

Silence may become meaningful negative evidence only when the relevant observation boundary is sufficiently constrained.

Candidate requirements include:

```text
sensor capability is known

collection was active

collection health is known

the relevant interval is known

event-loss bounds are acceptable

observation scope is appropriate

configuration is known

source trust is sufficient

relevant transformation behavior is understood
```

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
Known configuration
+
Bounded event loss
+
Sufficient coverage
+
Acceptable source trust
────────────────────────
Potential negative evidence
```

The exact semantics remain under research.

Research Gate 0 must not assume perfect completeness.

The strength of negative evidence must remain bounded by the actual observation contract.

---

## 11. Independent Semantic Dimensions

Research Gate 0 must preserve at least three distinct dimensions.

### Epistemic State

Describes the relationship between a claim and the evidence available to support or challenge it.

Candidate states:

```text
OBSERVED
DERIVED
INFERRED
HYPOTHESIZED
CONTRADICTED
UNKNOWN
```

These states describe how a claim is epistemically supported.

They do not describe sensor health.

They do not describe collection state.

They do not directly encode truth.

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

These states describe what was or could be observed.

They do not describe whether a claim is true.

They do not directly describe whether a source is trustworthy.

### Source Trust State

Describes whether a source can support conclusions within a stated scope.

Candidate states:

```text
TRUSTED_FOR_SCOPE
DEGRADED
UNTRUSTED
UNKNOWN
```

Source trust is scope dependent.

A source may be trustworthy for one observation class while being incapable of observing another.

These dimensions must not be collapsed into one generic:

```text
status
```

field.

---

## 12. Orthogonality Requirement

The candidate dimensions are intentionally independent.

For example:

```text
Epistemic State:
OBSERVED

Observation State:
AVAILABLE

Source Trust State:
DEGRADED
```

may be a meaningful combination.

Likewise:

```text
Epistemic State:
UNKNOWN

Observation State:
UNOBSERVABLE

Source Trust State:
TRUSTED_FOR_SCOPE
```

may also be meaningful.

A sensor may be trustworthy while being incapable of observing the phenomenon in question.

A claim may be directly observed while its supporting source is degraded.

A phenomenon may remain unknown because relevant evidence was never collected.

The model must therefore avoid treating these dimensions as interchangeable severity levels.

---

## 13. Initial Invariants

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

`UNKNOWN` must remain a valid final result.

### Invariant 6

Every claim must expose the evidence sources on which it depends.

### Invariant 7

Evidence source degradation must be capable of weakening dependent claims.

### Invariant 8

Observation state must not silently determine epistemic state without an explicit reasoning step.

### Invariant 9

Source trust must remain scoped to the capability and context in which the source is used.

### Invariant 10

A missing record must not be treated as proof that no observation occurred.

---

## 14. Controlled Research Scenario

The first microexperiment will compare three controlled sensor profiles.

```text
Sensor A

capable
healthy
complete for experiment scope
```

```text
Sensor B

capable
degraded
selected observations intentionally lost
```

```text
Sensor C

incapable of observing one event class
```

The experiment must demonstrate that identical-looking missing telemetry can represent materially different epistemic conditions.

For example:

```text
Sensor A:
no event observed
```

may potentially carry different evidential meaning from:

```text
Sensor B:
no event recorded because selected observations were lost
```

and:

```text
Sensor C:
no event observed because the event class is unobservable
```

A correct model must preserve these distinctions.

---

## 15. Falsification Direction

The current model should be revised if:

```text
the state dimensions cannot be kept semantically distinct

the model requires ad-hoc exceptions for every missing-observation case

provenance does not materially affect claim evaluation

sensor capability does not change the interpretation of silence

degraded collection cannot propagate into dependent reasoning

contradictory evidence cannot be preserved without destroying model consistency

the model produces certainty where the controlled experiment requires UNKNOWN

the proposed dimensions add complexity without improving defensibility
```

Failure to satisfy these conditions is evidence against the current model.

Research Gate 0 must allow the thesis to fail.

The architecture must not be expanded merely to conceal a weak or unnecessary abstraction.

---

## 16. Relationship to Claim Logic

This specification defines the epistemic and observational boundaries of Research Gate 0.

It establishes the distinction between:

```text
reality
observation
record
evidence
claim
epistemic state
```

The companion specification, [Claim Logic and Inference Boundaries](CLAIM_LOGIC.md), defines how propositions and inference rules may operate across those boundaries.

The two specifications therefore address different questions:

```text
EPISTEMIC_BOUNDARIES.md

What information state are we actually in?

What was observable?

What was collected?

What evidence exists?

What remains unknown?
```

and:

```text
CLAIM_LOGIC.md

What propositions are being asserted?

Which inference rule connects them?

Is the inference valid?

Are the premises defensible?
```

Neither specification is sufficient alone.

Together they define the initial semantic baseline that executable Research Gate 0 work must preserve.

Conceptually:

```text
Epistemic Boundary
        +
Logical Boundary
        ↓
Defensible Claim Boundary
```

---

## 17. Current Boundary

This document defines semantics only.

It does not yet define:

```text
Python classes

serialization formats

database schemas

graph schemas

APIs

production architecture

confidence scores

probabilistic models

Bayesian inference

temporal logic

causal logic

production rule engines

malware execution infrastructure
```

Those decisions remain downstream of research evidence.

No implementation technology should be selected merely because it is available.

Implementation should follow validated semantic requirements.

---

## 18. Implementation Gate

Executable implementation should begin only when the prerequisite concepts required by the model have been studied and the intended semantics can be explained without relying on source code.

Before implementation, the current sequence is:

```text
Problem
↓
Prerequisite Map
↓
Foundations
↓
Semantic Model
↓
Logical Model
↓
Controlled Microexperiment
↓
Specification
↓
Implementation
↓
Verification
```

This ordering exists to prevent programming constructs from hiding unresolved semantic questions.

The implementation must conform to the research model.

The research model must not be retroactively rewritten merely to justify convenient implementation.

---

## Final Principle

> **Observation is not truth. A record is not automatically evidence. Evidence is not automatically knowledge. A claim is only as defensible as the provenance and observation boundaries that support it.**
