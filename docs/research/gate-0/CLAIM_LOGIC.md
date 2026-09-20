# Research Gate 0: Claim Logic and Inference Boundaries

## Status

Companion specification: [Epistemic Boundaries](EPISTEMIC_BOUNDARIES.md)

**Research specification: provisional**

This document defines the initial logical boundaries governing propositions, observations, evidence, inference, contradiction, and defensible claims within Research Gate 0.

It does not define production inference behavior.

It does not claim that ELENCHION currently implements these semantics.

The purpose of this specification is to establish which logical transformations are currently admissible, which remain unsupported, and which forms of reasoning must be explicitly rejected.

---

## 1. Purpose

ELENCHION must distinguish between:

```text
what is true

what was observed

what was recorded

what evidence supports

what an inference rule permits

what the system may defensibly claim
```

These concepts are related.

They are not interchangeable.

The initial reasoning boundary is:

> **A valid inference cannot repair unsupported premises, and missing observation cannot silently become negation.**

Research Gate 0 therefore treats logical validity and evidence defensibility as independent requirements.

---

## 2. Proposition

A proposition is a declarative statement capable of carrying a truth value.

Example:

```text
P := "Process 42 wrote File F."
```

In classical propositional logic:

```text
Truth(P) ∈ {TRUE, FALSE}
```

The truth value concerns the underlying state of the world.

ELENCHION's knowledge about that truth is a separate dimension.

Therefore:

```text
Truth(P)
≠
EpistemicState(P)
```

A proposition may be true while the strongest defensible epistemic result available to ELENCHION remains:

```text
UNKNOWN
```

This separation is fundamental.

The system must never treat its internal knowledge state as direct access to reality.

---

## 3. Negation

For proposition:

```text
P := "Event E occurred."
```

its logical negation is:

```text
¬P := "Event E did not occur."
```

This is different from defining:

```text
O := "Event E was observed."
```

and therefore:

```text
¬O := "Event E was not observed."
```

The following transformation is not generally valid:

```text
¬Observed(E)
────────────
¬E
```

Therefore:

```text
¬Observed(E) ⇏ ¬E
```

is a core Research Gate 0 invariant.

The absence of an observation describes the observation system.

It does not, by itself, describe the underlying world.

---

## 4. Observation Propositions and World Propositions

ELENCHION must represent propositions about reality separately from propositions about observation.

Define:

```text
E := "File write occurred."

O := "Sensor S observed the file write."
```

These propositions may occupy different truth configurations.

### Case 1

```text
E = TRUE
O = TRUE
```

The event occurred and the sensor observed it.

### Case 2

```text
E = TRUE
O = FALSE
```

The event occurred but was not observed.

Possible causes include:

```text
sensor incapability
collection failure
event loss
coverage gap
temporal mismatch
pipeline failure
```

### Case 3

```text
E = FALSE
O = FALSE
```

The event did not occur and no observation was produced.

### Case 4

```text
E = FALSE
O = TRUE
```

The event did not occur, but the observation system reported that it did.

Possible causes include:

```text
false positive
incorrect attribution
corruption
parser defect
sensor defect
duplicate or stale data
```

The observation layer must therefore remain semantically distinct from the world state.

---

## 5. Conjunction

For propositions `P` and `Q`:

```text
P ∧ Q
```

is true only when both propositions are true.

Truth table:

```text
P | Q | P ∧ Q
--|---|------
T | T | T
T | F | F
F | T | F
F | F | F
```

Conjunction becomes important when an inference requires multiple independent preconditions.

For example, meaningful negative evidence may eventually require conditions such as:

```text
C := sensor has relevant capability

H := sensor health is acceptable

A := collection was active

I := observation interval is correctly bounded
```

A candidate prerequisite may therefore resemble:

```text
C ∧ H ∧ A ∧ I
```

This does not yet define sufficient conditions for negative evidence.

It only expresses that multiple independent requirements may need to hold simultaneously.

---

## 6. Disjunction

For propositions `P` and `Q`:

```text
P ∨ Q
```

is true when at least one proposition is true.

Truth table:

```text
P | Q | P ∨ Q
--|---|------
T | T | T
T | F | T
F | T | T
F | F | F
```

This is inclusive OR.

ELENCHION must preserve competing explanations when available evidence does not discriminate between them.

Example:

```text
A missing record may indicate:

event did not occur
∨
sensor could not observe the event
∨
collection was disabled
∨
event was lost
∨
transport failed
∨
persistence failed
∨
coverage is unknown
```

The existence of multiple explanations must not be collapsed into one preferred explanation without evidence.

---

## 7. Implication

An implication has the form:

```text
P → Q
```

and states:

```text
if P is true, Q must also be true
```

Truth table:

```text
P | Q | P → Q
--|---|------
T | T | T
T | F | F
F | T | T
F | F | T
```

In classical propositional logic:

```text
P → Q
```

is logically equivalent to:

```text
¬P ∨ Q
```

An implication constrains the relationship between propositions.

It does not establish that its antecedent actually occurred.

---

## 8. Converse Must Not Be Assumed

From:

```text
P → Q
```

ELENCHION must not automatically infer:

```text
Q → P
```

These are different propositions.

Example:

```text
P := "Behavior B produced network connection N."

Q := "Network connection N exists."
```

Even if:

```text
P → Q
```

is established, observing `Q` does not establish `P`.

Alternative causes may produce the same consequence.

Therefore:

```text
consequence observed
```

does not automatically mean:

```text
proposed cause established
```

This distinction is particularly important in behavioral detection and execution reconstruction.

---

## 9. Contrapositive

For classical implication:

```text
P → Q
```

the contrapositive is:

```text
¬Q → ¬P
```

and the two are logically equivalent.

However, evidence systems introduce an important boundary.

ELENCHION must establish actual support for:

```text
¬Q
```

before applying the contrapositive.

The following is not automatically sufficient:

```text
¬Observed(Q)
```

because:

```text
¬Observed(Q)
≠
¬Q
```

This means that classical logical equivalence does not eliminate the need to establish defensible premises.

---

## 10. Modus Ponens

A valid inference form is:

```text
P
P → Q
──────
Q
```

This is Modus Ponens.

The inference structure is valid.

However, validity concerns logical form.

It does not independently establish the truth of the premises.

ELENCHION must therefore maintain the distinction between:

```text
inference validity
```

and:

```text
premise defensibility
```

A valid rule applied to an unsupported premise may still produce an indefensible claim.

---

## 11. Modus Tollens

Another valid classical inference form is:

```text
P → Q
¬Q
──────
¬P
```

This is Modus Tollens.

In an evidence-bounded system, the second premise must genuinely support:

```text
¬Q
```

rather than merely:

```text
¬Observed(Q)
```

Otherwise the inference is not justified.

This becomes particularly important under incomplete telemetry.

---

## 12. Invalid Pattern: Affirming the Consequent

The following form is invalid:

```text
P → Q
Q
──────
P
```

This is the fallacy of affirming the consequent.

The presence of `Q` does not establish that `P` was its cause.

Alternative explanations may exist.

For execution analysis:

```text
behavior P may produce artifact Q
artifact Q exists
```

does not establish:

```text
behavior P occurred
```

unless additional evidence eliminates or sufficiently bounds competing explanations.

---

## 13. Invalid Pattern: Denying the Antecedent

The following form is also invalid:

```text
P → Q
¬P
──────
¬Q
```

`Q` may still arise through another cause.

An even more serious error occurs when:

```text
¬P
```

was itself incorrectly produced from:

```text
¬Observed(P)
```

The resulting failure chain becomes:

```text
missing observation
↓
unsupported negation
↓
invalid inference
↓
overstated claim
```

Research Gate 0 must preserve enough provenance to expose such reasoning chains.

---

## 14. Validity

Validity concerns the structure of an argument.

An argument is valid when:

> If all premises are true, the conclusion must also be true.

Validity therefore answers:

```text
Does the conclusion logically follow from the premises?
```

It does not answer:

```text
Are the premises actually true?
```

These questions must remain separate.

---

## 15. Soundness

A deductive argument is sound when:

```text
inference is valid
+
premises are true
```

Therefore:

```text
Soundness
=
Validity
+
True premises
```

A valid argument may still fail to describe reality when one or more premises are false.

This distinction directly motivates ELENCHION's separation between reasoning integrity and evidence defensibility.

---

## 16. Evidence Support Does Not Equal Truth

Evidence may support a proposition without guaranteeing its truth.

Example:

```text
Evidence A
SUPPORTS
P
```

does not permit ELENCHION to collapse the distinction into:

```text
P is guaranteed TRUE
```

Evidence may be affected by:

```text
sensor defects
incorrect attribution
event duplication
corruption
parser defects
clock errors
collection gaps
source degradation
incomplete context
transformation defects
```

Therefore:

```text
EvidenceSupport(P)
≠
Truth(P)
```

The relationship between evidence and proposition must remain explicit.

---

## 17. Premise Defensibility

In ELENCHION, a premise used by an inference should itself be traceable to evidence.

Conceptually:

```text
Claim Q
↑
Inference
↑
Premise P
↑
Evidence
↑
Observation
↑
Sensor
```

A reasoning chain is therefore only as defensible as the premises on which it depends.

The system should eventually be capable of answering:

```text
Which premises produced Claim Q?

Which evidence supports each premise?

Which sensor produced that evidence?

What observation assumptions were required?

Which premise becomes invalid if a source loses trust?
```

This creates a bridge between formal logic and provenance.

---

## 18. Contradictory Evidence

Contradictory evidence occurs when independent evidence relationships support incompatible propositions.

Example:

```text
Evidence A supports P.

Evidence B supports ¬P.
```

This does not require ELENCHION to assert:

```text
P ∧ ¬P
```

as a true description of reality.

Instead, the system should preserve:

```text
support for P

support for ¬P

source identities

source trust

observation conditions

provenance

temporal context
```

until the conflict can be resolved, bounded, or left explicitly unresolved.

Contradictory evidence is therefore evidence about the state of knowledge.

---

## 19. Logical Contradiction

In classical propositional logic:

```text
P ∧ ¬P
```

is a contradiction.

It evaluates false for every classical truth assignment.

Research Gate 0 must distinguish this formal logical concept from:

```text
Evidence A supports P
```

and:

```text
Evidence B supports ¬P
```

which represent conflicting support rather than direct proof that reality simultaneously satisfies both propositions.

The reasoning model must not destroy conflicting evidence merely to restore visual consistency.

---

## 20. Tautology

A tautology is true under every possible truth assignment.

Example:

```text
P ∨ ¬P
```

Truth table:

```text
P | ¬P | P ∨ ¬P
--|----|-------
T | F  | T
F | T  | T
```

Within classical logic this represents the Law of Excluded Middle.

ELENCHION must nevertheless avoid confusing:

```text
P ∨ ¬P
```

with:

```text
the system knows whether P or ¬P holds
```

The world may satisfy one side while the system remains epistemically unable to identify which.

---

## 21. Negative Evidence Requires an Observation Contract

The absence of observation may acquire evidential significance only when the observation boundary is sufficiently constrained.

Candidate conditions include:

```text
CanObserve(E)

CollectionActive

HealthKnown

IntervalCovered

LossBoundKnown

ConfigurationKnown

SourceTrustAcceptable
```

Conceptually:

```text
¬Observed(E)
+
defined observation contract
+
known collection conditions
────────────────────────────
bounded negative evidence
```

The result remains bounded by the strength of the observation contract.

Research Gate 0 must not assume perfect completeness merely because no event appears in telemetry.

---

## 22. Reasoning Integrity

Reasoning integrity asks:

```text
Did the conclusion follow from the premises using an accepted inference rule?
```

Possible failures include:

```text
invalid implication reversal

affirming the consequent

denying the antecedent

unsupported negation

hidden assumptions

discarded alternatives

untracked contradiction
```

Reasoning integrity concerns the transformation from premises to conclusions.

---

## 23. Evidence and Premise Defensibility

Premise defensibility asks:

```text
Are the premises sufficiently supported by traceable evidence?
```

Relevant dimensions may eventually include:

```text
provenance

source trust

sensor capability

collection health

coverage

integrity

transformation history

temporal uncertainty

contradictory evidence
```

This dimension is independent of reasoning validity.

---

## 24. Defensible Claim Boundary

A strong ELENCHION claim should require both:

```text
Reasoning Integrity
```

and:

```text
Evidence-Bounded Premises
```

Conceptually:

```text
Defensible Claim
        ↑
        │
 ┌──────┴──────┐
 │             │
Reasoning    Premises
Integrity    Defensible
 │             │
 └──────┬──────┘
        │
      Evidence
        │
    Provenance
```

Neither side is sufficient alone.

---

## 25. Initial Logical Invariants

Research Gate 0 should preserve the following invariants.

### Invariant L1

```text
¬Observed(E) ⇏ ¬E
```

unless additional observation assumptions justify bounded negative evidence.

### Invariant L2

```text
P → Q
```

must not silently become:

```text
Q → P
```

### Invariant L3

Observation propositions must remain distinct from propositions about underlying events.

### Invariant L4

Modus Ponens and other accepted inference rules must remain distinguishable from evidence support.

### Invariant L5

Affirming the consequent must not be treated as valid reasoning.

### Invariant L6

Denying the antecedent must not be treated as valid reasoning.

### Invariant L7

Contradictory evidence must be preserved rather than silently discarded.

### Invariant L8

Inference validity and premise defensibility must remain independent dimensions.

### Invariant L9

A valid inference must not automatically strengthen the epistemic status of unsupported premises.

### Invariant L10

The provenance path from a derived claim back to its supporting premises and evidence must remain inspectable.

---

## 26. Controlled Research Example

Define:

```text
E := event occurred

O := sensor observed event

C := sensor can observe event class

H := sensor health acceptable

A := collection active

I := relevant interval covered
```

Suppose only:

```text
¬O
```

is known.

Research Gate 0 must not conclude:

```text
¬E
```

from this fact alone.

If later evidence establishes:

```text
C ∧ H ∧ A ∧ I
```

together with sufficiently bounded event loss, configuration state, and source trust, then:

```text
¬O
```

may acquire negative evidential value.

The strength of the resulting claim must remain bounded by the actual observation contract.

---

## 27. Failure Example

Consider the reasoning chain:

```text
No event was recorded.

Therefore the event was not observed.

Therefore the event did not occur.

Therefore behavior B did not happen.
```

Each transition requires independent justification.

The chain may fail because:

```text
record absence
does not establish
observation absence
```

and:

```text
observation absence
does not establish
event absence
```

and:

```text
event absence
may not establish
behavior absence
```

Research Gate 0 should eventually make each unsupported transition computationally visible.

---

## 28. Current Boundary

This specification does not yet define:

```text
probability theory

Bayesian inference

likelihood ratios

confidence scores

three-valued logic

many-valued logic

paraconsistent logic

temporal logic

modal logic

causal logic

automated theorem proving

production rule engines
```

These subjects may become relevant later.

They must not be introduced merely for sophistication.

They should enter the system only when a concrete research problem requires them.

---

## 29. Research Direction

The immediate objective is not to build a universal reasoning engine.

The immediate objective is narrower:

> Determine whether explicit separation between world propositions, observation propositions, evidence support, premise defensibility, and inference validity produces more defensible execution analysis.

Research Gate 0 must test that claim using controlled cases rather than architectural assumption.

---

## Final Principle

> **A conclusion is not defensible merely because its reasoning is valid. Its premises must also survive cross examination by their evidence.**
