# ELENCHION Roadmap

> **The roadmap is a research hypothesis, not a promise of architecture.**

ELENCHION evolves only when evidence justifies the next layer of complexity.

The project deliberately separates research validation from production engineering. A phase is not complete because files, services, diagrams, or dashboards exist. Progress requires explicit exit evidence.

---

## Phase Zero — Research and Thesis Validation

**Current phase**

### Objective

Determine whether claim-level provenance, observation capability, sensor health, contradiction preservation, temporal uncertainty, and trust dependencies can measurably improve execution-analysis defensibility.

### Research Areas

* evidence-bounded claim semantics;
* epistemic-state semantics;
* observation and collection states;
* sensor capability contracts;
* sensor-health representation;
* negative-evidence semantics;
* contradictory evidence;
* partial temporal ordering;
* uncertainty propagation;
* trust-degradation analysis;
* controlled multi-run comparison;
* reproducibility;
* analyst verification.

### Required Experimental Baseline

Initial experiments should use benign deterministic workloads rather than hostile samples.

The first controlled environment should be capable of simulating conditions such as:

```text
Sensor A
complete observation

Sensor B
event loss

Sensor C
incapable of observing one event class
```

The system must distinguish:

```text
OBSERVED

UNKNOWN

NOT COLLECTED

COLLECTION FAILED

UNOBSERVABLE

CONTRADICTED
```

without silently collapsing them into a single verdict.

### Exit Evidence

Phase Zero is complete only when the project has:

* a versioned epistemic model;
* a versioned provenance model;
* a sensor-contract specification;
* a temporal uncertainty model;
* negative-evidence semantics;
* controlled microexperiments;
* falsifiable benchmark definitions;
* measured baseline behavior;
* documented failure cases;
* documented thesis limitations.

---

## Phase One — Evidence Kernel Prototype

### Objective

Build the smallest executable system capable of representing and evaluating evidence-bounded claims.

### Candidate Scope

* canonical evidence identity;
* raw-to-canonical transformation metadata;
* evidence-bounded claim representation;
* supporting and contradicting evidence;
* sensor dependencies;
* source trust;
* temporal bounds;
* invalidation dependencies;
* claim lifecycle;
* deterministic query primitives;
* trust-degradation traversal.

### Non-Goal

Phase One is not a production malware-analysis platform.

The prototype exists to test the research model.

### Exit Evidence

* deterministic benign test corpus;
* reproducible claim reconstruction;
* explicit UNKNOWN behavior;
* contradiction preservation;
* provenance completeness measurement;
* trust-degradation tests;
* negative-evidence tests;
* failure-mode documentation.

---

## Phase Two — Multi-Source and Multi-Run Reconstruction

### Objective

Test whether the model survives disagreement across sensors, environments, runtimes, and executions.

### Candidate Research

* cross-run evidence identity;
* behavior intersection and union;
* behavior delta;
* environment-dependent behavior;
* sensor-dependent behavior;
* memory-derived evidence;
* runtime-semantic evidence;
* cross-source contradiction;
* partial temporal ordering;
* evidence graph projections;
* first-class query.

### Core Question

> Does additional telemetry increase defensible knowledge, or merely increase event volume?

### Exit Evidence

* reproducible cross-run experiments;
* measured contradiction behavior;
* measured uncertainty propagation;
* environment-fidelity studies;
* observer-effect studies;
* query validation;
* bounded graph-growth strategy.

---

## Phase Three — Containment, Integrity, and Assurance

### Objective

Harden the research architecture against hostile evidence and hostile execution.

### Candidate Scope

* analyst-plane / execution-plane separation;
* disposable execution workers;
* credential-free workers;
* parser isolation;
* resource exhaustion controls;
* evidence custody;
* immutable raw evidence;
* artifact integrity;
* signed transformations;
* workload identity;
* offline operation;
* trust distribution;
* supply-chain provenance;
* reproducibility capsules.

### Core Question

> Can the system continue making defensible claims when parts of the collection or analysis pipeline may themselves be compromised?

### Exit Evidence

Security properties must be validated rather than merely documented.

---

## Phase Four — Integrated Execution Intelligence

### Objective

Integrate validated primitives into a coherent analyst-facing execution-intelligence platform.

Possible capabilities may include:

```text
Case Management
Controlled Execution
Evidence Collection
Canonicalization
Temporal Reconstruction
Runtime Reconstruction
Memory Evidence
Evidence-Bounded Claims
Contradiction Analysis
Trust Degradation
Cross-Run Comparison
Query
Analyst Review
Reproducibility
Custody / Assurance
```

Capabilities enter this phase only if previous research justifies them.

---

## Phase Five — Public Research and Evaluation

### Objective

Make ELENCHION externally testable.

Potential deliverables include:

* reproducible benchmark suites;
* published experiment methodology;
* reference datasets where legally and safely distributable;
* architecture decision records;
* threat models;
* performance measurements;
* assurance evidence;
* release artifacts;
* interoperability documentation;
* independent replication guidance.

The goal is not merely adoption.

The goal is independent scrutiny.

---

## Cross-Cutting Gates

Every phase is subject to the same questions:

```text
Can the claim be traced?

Can the result be reproduced?

Can the hypothesis be falsified?

Can a sensor fail silently?

Can a source become untrusted?

Can evidence contradict another source?

Can time ordering be uncertain?

Can hostile input poison interpretation?

Can uncertainty be preserved?

Can an analyst inspect the reasoning?

Does the added complexity produce measurable value?
```

If the answer is unknown, the project records the unknown.

---

## Roadmap Rule

ELENCHION does not advance because a calendar says it should.

It advances when the evidence supports the next engineering decision.
