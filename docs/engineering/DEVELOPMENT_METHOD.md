# ELENCHION Development Method

## Purpose

ELENCHION is developed through a **foundations-first, evidence-driven engineering method**.

The objective is not to maximize implementation speed, commit volume, or architectural complexity. The objective is to build technical understanding and system capability together so that every important design choice can be explained, tested, challenged, and traced to evidence.

The method therefore treats learning, research, implementation, verification, and public engineering artifacts as parts of one continuous system.

> **Understanding precedes implementation. Evidence precedes confidence.**

---

## 1. The Development Model

ELENCHION advances through three parallel tracks.

### Knowledge Track

Build the foundations required to understand the problem correctly.

This may include:

- mathematics;
- logic;
- computer science;
- computer architecture;
- operating systems;
- networking;
- programming-language semantics;
- security engineering;
- digital forensics;
- experimental design;
- statistics and measurement;
- systems performance;
- reproducibility.

### Engineering Track

Turn validated understanding into executable system behavior.

This may include:

- specifications;
- data models;
- algorithms;
- prototypes;
- tests;
- benchmarks;
- tooling;
- architecture decisions;
- security controls;
- reproducible experiments.

### Evidence Track

Produce artifacts that allow another person to inspect what was learned, built, measured, and concluded.

Examples include:

- research notes promoted into formal specifications;
- experiment protocols;
- benchmark definitions;
- test results;
- architecture decisions;
- threat models;
- signed commits;
- reviewed pull requests;
- reproducible outputs;
- documented limitations.

The three tracks are intentionally connected:

```text
Foundations
    ↓
Understanding
    ↓
Model
    ↓
Experiment
    ↓
Implementation
    ↓
Verification
    ↓
Engineering Evidence
    ↓
Public Artifact
```

A public artifact is not created merely to increase repository activity. It must preserve real engineering value.

---

## 2. Stage 0: Define the Problem

Implementation does not begin with a framework, language, database, service boundary, or architecture diagram.

It begins with a problem.

Before substantive work, define:

- what is unknown, incorrect, missing, or unverified;
- why the problem matters;
- what evidence suggests the problem exists;
- what is in scope;
- what is outside scope;
- which assumptions are being made;
- how success could be measured;
- what result would falsify the current hypothesis.

A problem that cannot be explained clearly is not ready for implementation.

---

## 3. Stage 1: Build the Prerequisite Map

Before writing code, identify the knowledge required to reason about the problem without hiding behind abstractions.

For example, a sensor-capability model may require understanding:

```text
observation
measurement
sets
subsets
relations
functions
predicates
state
state spaces
sampling
event loss
clock behavior
trust
integrity
failure models
```

A dependency is studied because the project requires it, not because a generic curriculum says it should be studied.

The rule is:

> **Do not skip a prerequisite that materially affects correctness. Do not add a prerequisite that exists only for appearance.**

---

## 4. Stage 2: Foundations Before Abstractions

A concept is developed from its primitive form before its software representation is introduced.

If the implementation eventually uses an enum, graph, probability, queue, hash, state machine, parser, lock, thread, process, socket, memory mapping, cryptographic digest, or database transaction, the underlying concept is studied first.

Examples:

```text
Enum
← finite set
← membership
← symbolic state
← state space

Graph
← set
← relation
← vertex
← edge
← reachability

Concurrency primitive
← process/thread model
← shared state
← ordering
← race condition
← synchronization

Evidence digest
← bytes
← deterministic function
← collision concept
← cryptographic hash properties
```

The purpose is not academic ceremony. The purpose is to prevent software syntax from disguising misunderstood semantics.

---

## 5. Stage 3: Establish the Mental Model

Before code, the system behavior should be explainable without code.

The development session should be able to answer:

- What entities exist?
- Which states can they occupy?
- Which states are independent?
- Which transitions are legal?
- What evidence causes a transition?
- What remains unknown?
- What assumptions are hidden?
- Which failure modes are possible?

Diagrams, tables, truth tables, set notation, state tables, small examples, and paper exercises may be used where they improve reasoning.

A clean mental model is not proof that the design is correct, but an unclear mental model is evidence that implementation is premature.

---

## 6. Stage 4: Microexperiment Before System Complexity

The smallest experiment capable of challenging the hypothesis is preferred over premature architecture.

A microexperiment should isolate one idea.

For Research Gate 0, for example:

```text
Sensor A
complete observation for scope

Sensor B
capable but intentionally loses observations

Sensor C
incapable of observing one event class
```

The question is not whether a large platform can be constructed.

The question is whether the model can distinguish materially different evidence conditions without manufacturing certainty.

Microexperiments should be:

- deterministic where practical;
- benign;
- reproducible;
- isolated;
- measurable;
- easy to falsify;
- small enough to understand completely.

---

## 7. Stage 5: Specify Before Generalizing

Once the experiment exposes the required semantics, represent them explicitly.

Candidate specification artifacts may define:

- state spaces;
- evidence identities;
- sensor contracts;
- temporal bounds;
- provenance requirements;
- trust dependencies;
- invariants;
- failure conditions;
- serialization requirements;
- validation rules.

Specifications remain provisional when the evidence remains provisional.

A specification is allowed to change when experiments reveal a flaw.

---

## 8. Stage 6: VS Code Implementation

Project code is written in **VS Code**.

The terminal is used for activities such as:

- Git operations;
- tests;
- builds;
- package management;
- environment management;
- static analysis;
- debugging commands;
- profiling;
- inspection of generated artifacts.

Code is not treated as text to paste blindly.

Each meaningful line must be understood in terms of:

- syntax;
- type behavior;
- runtime behavior;
- memory implications where relevant;
- control flow;
- error behavior;
- security implications;
- performance implications where relevant;
- relationship to project invariants.

Repeated concepts may be explained again. Familiarity is not assumed to equal understanding.

---

## 9. Stage 7: Test the Invariant, Not the Demo

Tests should target the semantic property the system claims to preserve.

A test suite should ask questions such as:

- Can missing evidence be confused with negative evidence?
- Can an unobservable event class appear as a confident absence?
- Can degraded collection silently support a strong claim?
- Can contradiction be discarded?
- Can source trust and claim confidence collapse into one field?
- Can a parser failure lose provenance?
- Can temporal uncertainty be converted into false total ordering?

A passing happy-path demonstration is not sufficient evidence.

Relevant techniques may include:

- unit tests;
- integration tests;
- negative tests;
- property-based tests;
- fault injection;
- fuzzing;
- differential testing;
- benchmark tests;
- reproducibility checks.

The technique should follow the failure mode being tested.

---

## 10. Stage 8: Debug From Evidence

Debugging is treated as hypothesis testing.

The loop is:

```text
Observed failure
      ↓
Bound the problem
      ↓
Form hypothesis
      ↓
Design discriminating test
      ↓
Collect evidence
      ↓
Reject or retain hypothesis
      ↓
Reduce uncertainty
      ↓
Fix
      ↓
Regression test
```

Errors should not be patched by changing code until the symptom disappears.

The goal is to identify why the system behaved as it did and preserve a test that prevents recurrence when practical.

---

## 11. Stage 9: Measure Before Performance Claims

Performance language requires measurement.

Claims such as:

```text
fast
low-overhead
scalable
real-time
efficient
```

must eventually identify the measured dimension and method.

Possible dimensions include:

- throughput;
- latency;
- CPU cost;
- memory cost;
- storage amplification;
- event loss;
- query latency;
- reconstruction latency;
- experiment duration.

Optimization begins after the relevant bottleneck is identified.

---

## 12. Stage 10: Cross-Examine the Change

Before merge, challenge the implementation as if the author were wrong.

Relevant questions include:

- Is the model semantically correct?
- Is the claim stronger than the evidence?
- What happens under malformed input?
- What happens under partial failure?
- Can evidence be lost?
- Can evidence be poisoned?
- Can uncertainty disappear accidentally?
- Can a trust boundary be bypassed?
- Can resource exhaustion become a security problem?
- Can the behavior be reproduced?
- Is there a simpler design with equal evidence?

Review is expected to create friction when the evidence is weak.

---

## 13. Stage 11: Git and GitHub Lifecycle

Substantive engineering work should normally follow:

```text
Problem
   ↓
Issue when the problem merits a durable record
   ↓
Research / Design
   ↓
Dedicated Branch
   ↓
Implementation
   ↓
Tests / Experiments
   ↓
Diff Review
   ↓
Signed Commit
   ↓
Pull Request
   ↓
Cross-Examination Review
   ↓
Automated Checks where available
   ↓
Merge
```

Issues are intentionally proportional.

They are appropriate for substantial research questions, architecture changes, important features, security problems, benchmarks, significant defects, and high-risk refactors.

They are not required for every documentation edit, typo, metadata change, or routine repository maintenance.

Commit count is not a performance metric.

---

## 14. Stage 12: Convert Learning Into Engineering Evidence

Not every lesson becomes a repository artifact.

A concept enters the repository when it produces project-relevant evidence.

Examples:

| Foundation | Possible ELENCHION Artifact |
|---|---|
| Set theory | evidence/state specification |
| Logic | claim-evaluation semantics |
| Probability | uncertainty experiment |
| Graph theory | provenance dependency model |
| Data structures | measured implementation comparison |
| Operating systems | execution-observation experiment |
| Memory | memory-evidence experiment |
| Networking | network-evidence model |
| Cryptography | evidence-integrity design and tests |
| Testing theory | invariant and failure-mode suite |
| Security engineering | threat model or abuse-case analysis |
| Experimental design | reproducible experiment protocol |

The repository should demonstrate applied understanding rather than document every study session.

---

## 15. Stage 13: Portfolio Evidence

The public repository is treated as engineering evidence.

Portfolio strength is not estimated by commit volume.

A stronger signal is produced by the combination of:

```text
important problem
×
technical depth
×
measurable evidence
×
reproducibility
×
security discipline
×
review quality
×
clear communication
```

High-value portfolio artifacts may include:

- a falsifiable research thesis;
- a reproducible experiment;
- a benchmark;
- a threat model;
- a meaningful architecture decision;
- a tested subsystem;
- failure analysis;
- measured performance work;
- signed development history;
- rigorous pull-request review;
- explicit limitations.

Activity theater is explicitly rejected.

---

## 16. Stage 14: Retrieval, Transfer, and Independent Reconstruction

Understanding is periodically tested without relying on the implementation in front of the developer.

Three forms of verification are used.

### Recall

Explain the concept without copying the existing explanation.

### Transfer

Apply the concept to a different problem or failure mode.

### Reconstruction

Rebuild a small model or experiment from first principles.

If a concept cannot survive transfer, implementation familiarity may be hiding incomplete understanding.

---

## 17. Stage 15: Gate Decision

Every major development slice ends with a gate decision.

Possible outcomes include:

### Advance

Evidence supports the next layer of implementation.

### Revise

The model is useful but assumptions, semantics, or implementation require change.

### Repeat

The experiment is inconclusive or insufficiently controlled.

### Reject

The hypothesis did not survive testing.

### Unknown

Available evidence is insufficient to justify a stronger decision.

A failed experiment is not a failed project.

Hiding a failed experiment behind additional complexity is a failure of the method.

---

## 18. Safety Boundary

The development method remains inside ELENCHION's defensive mission.

Research and experiments may examine malicious behavior conceptually or through safe evidence, but public implementation work must not become a path for deployable malware, credential theft, ransomware, offensive persistence, propagation, real-world command-and-control, payload delivery, real-target attack automation, or offensive evasion optimization.

Benign deterministic experiments are preferred until a stronger research requirement justifies a different controlled environment.

---

## 19. Example: Research Gate 0

The current gate illustrates the method.

```text
Question
Can claim-level evidence state distinguish different reasons for missing telemetry?

↓

Prerequisites
logic
sets
state spaces
observation
measurement
sensor capability
failure models
trust

↓

Mental Model
Epistemic State × Observation State × Source Trust State

↓

Microexperiment
complete sensor
lossy sensor
incapable sensor

↓

Specification
explicit state dimensions
sensor contract
provenance dependency

↓

Implementation
minimal deterministic research harness

↓

Verification
negative evidence tests
UNKNOWN outcome
contradiction preservation
trust degradation

↓

Gate
advance, revise, repeat, reject, or remain unknown
```

The purpose of the gate is not to prove that ELENCHION is already a platform.

It is to determine whether the first core thesis survives controlled execution.

---

## 20. Definition of Done

A meaningful development slice is complete only when its required level of evidence exists.

Depending on scope, that may mean:

```text
Problem understood
↓
Prerequisites understood
↓
Model explainable
↓
Experiment reproducible
↓
Implementation reviewable
↓
Failure modes tested
↓
Claims measured
↓
Limitations documented
↓
Diff reviewed
↓
Commit signed
↓
Pull request cross-examined
↓
Artifact merged
```

Not every change requires every stage at maximum depth. Process must remain proportional to risk and significance.

The non-negotiable principle is that important conclusions must remain explainable from first principles and defensible from evidence.

---

## Final Principle

ELENCHION does not separate learning from engineering, or engineering from evidence.

The project advances by converting understanding into models, models into experiments, experiments into implementation, and implementation into evidence that can survive review.

> **Build only what can be understood, tested, measured, and defended.**
