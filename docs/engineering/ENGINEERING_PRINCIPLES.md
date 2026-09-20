# ELENCHION Engineering Principles

## 1. Purpose

ELENCHION is developed as research and engineering infrastructure for evidence-bounded execution intelligence.

The repository must preserve a traceable relationship between problems, evidence, decisions, implementation, validation, and claims.

Repository activity is not an end in itself.

A commit, pull request, architecture component, benchmark, security control, or research artifact is valuable only when its purpose can be explained and its claims can be defended.

---

## 2. Core Engineering Invariant

> **No claim without provenance.**

A significant technical claim should be traceable to the evidence that supports it.

Where applicable, that evidence should identify:

* its source;
* collection conditions;
* relevant environment;
* transformations;
* versions;
* assumptions;
* known limitations;
* contradictory evidence;
* uncertainty;
* validation method.

A result that cannot be adequately supported must remain explicitly uncertain.

---

## 3. Evidence Before Assertion

ELENCHION distinguishes between:

### Research Evidence

Evidence obtained from literature, standards, experiments, benchmarks, documented observations, or independently verifiable external sources.

### Implementation Evidence

Evidence produced by the repository itself, including:

* tests;
* benchmark results;
* static analysis;
* runtime observations;
* reproducible experiments;
* signed artifacts;
* CI results;
* security assessments.

### Claims

Interpretations or conclusions supported by research evidence, implementation evidence, or both.

Claims must not silently become stronger than their supporting evidence.

---

## 4. UNKNOWN Is a Valid Result

ELENCHION does not manufacture certainty to make reports, interfaces, or documentation appear complete.

Valid outcomes may include:

* unknown;
* unresolved;
* insufficient evidence;
* contradictory evidence;
* collection failure;
* unsupported hypothesis;
* unobservable under current conditions.

An explicit UNKNOWN is preferable to an unsupported conclusion.

---

## 5. Problem-First Engineering

Features do not begin with implementation.

Substantial work should begin with a documented problem.

A useful problem statement should explain:

* what is wrong or missing;
* what evidence indicates the problem exists;
* why the problem matters;
* what is in scope;
* what is not in scope;
* how success can be measured;
* how the proposed solution could fail.

Complexity alone does not justify implementation.

---

## 6. Engineering Traceability

Substantive work should approach the following lifecycle:

```text
Problem
   ↓
Issue
   ↓
Research / Design
   ↓
Branch
   ↓
Implementation
   ↓
Tests / Validation
   ↓
Diff Review
   ↓
Signed Commit
   ↓
Pull Request
   ↓
Review
   ↓
Automated Checks
   ↓
Merge
   ↓
Release / Artifact when applicable
```

Exceptions should remain exceptional and explainable.

The signed repository genesis commit is one such intentional exception because no prior branch or repository history existed.

---

## 7. Commit Discipline

A commit should represent one coherent engineering change.

Good commits are:

* understandable in isolation;
* narrowly scoped;
* reviewable;
* reversible where practical;
* signed;
* accompanied by meaningful messages.

Commit count is not a quality metric.

Artificially splitting one logical change into many commits is discouraged.

Combining unrelated changes into one commit is also discouraged.

Commit messages should describe why the repository changed, not merely which files changed.

---

## 8. Branch Discipline

A branch should have one primary purpose.

Branch names should communicate that purpose.

Examples:

```text
docs/issue-2-engineering-principles
research/issue-12-negative-evidence
feat/issue-27-evidence-object
fix/issue-44-clock-normalization
security/issue-61-parser-isolation
```

Branches should not become long-lived containers for unrelated changes.

---

## 9. Pull Requests Are Engineering Arguments

A substantial pull request should explain:

* the problem;
* why the change exists;
* relevant architecture or research context;
* what changed;
* what intentionally did not change;
* evidence and validation;
* security impact;
* performance impact where relevant;
* portability impact where relevant;
* known limitations;
* failure and rollback considerations;
* areas requiring reviewer attention.

A green CI state does not substitute for review.

---

## 10. Review Is Cross-Examination

Review is not ceremonial approval.

Relevant review dimensions include:

* correctness;
* security;
* evidence integrity;
* provenance preservation;
* data loss;
* error handling;
* concurrency;
* memory behavior;
* performance;
* portability;
* dependency risk;
* tests;
* documentation;
* reproducibility.

Reviewers should challenge assumptions when evidence is insufficient.

---

## 11. Security Requirements

The public repository must not contain:

* private keys;
* access tokens;
* passwords;
* credentials;
* recovery codes;
* confidential evidence;
* restricted datasets;
* hostile samples;
* secrets embedded in configuration;
* unauthorized proprietary material.

Public repository content must be treated as disclosed information.

Security controls should be justified by the threat they reduce.

Security theater is not assurance.

---

## 12. Evidence Integrity

Original evidence and derived artifacts must remain distinguishable.

Transformations should preserve traceability where practical.

A derived result must not silently replace its source evidence.

Where evidence integrity is material, the project should consider:

* content identity;
* cryptographic digests;
* signed artifacts;
* immutable source preservation;
* transformation versioning;
* audit history.

Specific mechanisms must follow documented requirements rather than fashion.

---

## 13. Error Handling

Errors are part of system behavior.

Code should not silently discard failures that affect:

* evidence collection;
* provenance;
* reconstruction;
* security boundaries;
* persistence;
* temporal interpretation;
* analyst conclusions.

When an operation fails, the system should preserve enough context to determine:

* what failed;
* where it failed;
* what was affected;
* whether retry is safe;
* which conclusions are weakened.

---

## 14. Performance Claims Require Measurement

Performance adjectives are not evidence.

Terms such as:

* fast;
* scalable;
* low-overhead;
* efficient;
* real-time;

must not be used as technical claims without relevant measurement.

Important performance dimensions may include:

* ingestion throughput;
* event-loss rate;
* CPU overhead;
* memory overhead;
* storage amplification;
* reconstruction latency;
* query latency;
* experiment latency.

Measurement methodology should be reproducible.

---

## 15. Portability Claims Require Evidence

ELENCHION must not claim cross-platform behavior merely because code compiles on more than one platform.

Relevant differences may include:

* operating-system semantics;
* architecture;
* binary formats;
* privilege models;
* clocks;
* filesystem semantics;
* runtime behavior;
* sensor capability;
* event meaning.

Cross-platform abstractions must preserve important semantic differences.

---

## 16. Testing Principles

Tests exist to challenge assumptions.

Relevant testing strategies may include:

* unit tests;
* integration tests;
* property-based tests;
* regression tests;
* negative tests;
* fault injection;
* fuzzing;
* differential tests;
* performance benchmarks;
* reproducibility checks.

Test quantity alone is not assurance.

Tests should target meaningful failure modes.

---

## 17. Research and Architecture

Architecture is provisional when evidence is provisional.

An architecture diagram does not prove that an architecture is correct.

Major architecture decisions should document:

* the problem;
* requirements;
* alternatives;
* evidence;
* tradeoffs;
* assumptions;
* failure modes;
* security consequences;
* operational consequences;
* conditions that would invalidate the decision.

Research results are allowed to change the architecture.

---

## 18. Automated Assistance

Generated output is not evidence by default.

Generated hypotheses, summaries, transformations, or recommendations must not silently become factual findings.

Where automated tooling contributes to a conclusion, the system should preserve enough information to identify:

* that automated assistance was involved;
* the relevant model or system version where practical;
* the evidence referenced;
* the transformation performed;
* the human or machine validation applied.

Core evidence semantics must remain useful without automated assistance.

---

## 19. Public Engineering Standard

The repository is not a learning diary.

Internal learning may be extensive, but public artifacts should serve the engineering and research mission.

Repository additions should answer at least one of these questions:

* Does this solve a documented problem?
* Does this preserve important evidence?
* Does this improve reproducibility?
* Does this make a claim more verifiable?
* Does this reduce a documented risk?
* Does this enable a measurable experiment?
* Does this improve analyst verification?
* Does this strengthen engineering assurance?

If none apply, the artifact may not belong in the repository.

---

## 20. Final Standard

Before accepting a significant change, ask:

* Is the problem documented?
* Is the evidence sufficient?
* Is the claim stronger than the evidence?
* Can the result be reproduced?
* Can hostile input break the assumption?
* Can evidence be lost or poisoned?
* Can failure occur silently?
* Can uncertainty be hidden?
* Can an analyst verify the conclusion?
* Can an assessor verify the security claim?
* Does this complexity have measurable value?

ELENCHION should not optimize for appearing sophisticated.

It should optimize for conclusions and systems that survive hostile scrutiny.
