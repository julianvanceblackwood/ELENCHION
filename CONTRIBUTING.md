# Contributing to ELENCHION

Thank you for considering a contribution to ELENCHION.

ELENCHION is being developed as research and engineering infrastructure for evidence-bounded execution intelligence. Contributions should strengthen the project's ability to produce conclusions that can be inspected, measured, reproduced, and challenged.

## Before Contributing

Read:

* `README.md`
* `docs/engineering/ENGINEERING_PRINCIPLES.md`
* `SECURITY.md`

A contribution should have a clear relationship to the project's research or engineering mission.

Complexity, novelty, automation, or additional code are not sufficient reasons by themselves.

## When to Open an Issue

Issues are reserved for work that benefits from an explicit problem record.

Examples include substantial features, research questions, architecture decisions, security problems, reproducibility problems, benchmarks, important defects, behavioral changes, and significant refactors.

An issue is generally not required for small documentation corrections, repository housekeeping, metadata changes, narrowly scoped editorial improvements, or similarly low-risk maintenance.

Avoid creating process artifacts solely to increase repository activity.

## Branches

Use one primary purpose per branch.

Examples:

```text
research/negative-evidence-semantics
feat/evidence-object
fix/clock-normalization
security/parser-isolation
docs/architecture-model
chore/repository-governance-baseline
```

Branch names should communicate intent without becoming miniature descriptions.

## Commits

A commit should represent one coherent engineering change.

Commits should be:

* reviewable;
* narrowly scoped;
* understandable in isolation;
* reversible where practical;
* cryptographically signed when produced by project maintainers;
* accompanied by meaningful commit messages.

Do not split one logical change into many artificial commits for activity.

Do not combine unrelated work into one commit.

Prefer messages that explain the purpose of the change.

Examples:

```text
research: define negative-evidence experiment
feat: introduce canonical evidence identity
fix: preserve unknown clock ordering
security: isolate parser resource limits
docs: document evidence-bounded claim model
```

## Pull Requests

Pull requests are review units, not administrative ceremony.

A substantial pull request should explain:

* the problem or purpose;
* why the change exists;
* what changed;
* what intentionally did not change;
* validation performed;
* security implications;
* performance implications where relevant;
* portability implications where relevant;
* known limitations;
* reviewer focus.

Small pull requests may be proportionally shorter.

## Review Standard

Review should challenge the change across relevant dimensions:

* correctness;
* security;
* evidence integrity;
* provenance;
* error handling;
* data loss;
* concurrency;
* memory behavior;
* performance;
* portability;
* dependency risk;
* testing;
* documentation;
* reproducibility.

Automated checks support review. They do not replace it.

## Research Contributions

Research-oriented contributions should distinguish among:

* literature evidence;
* experimental evidence;
* implementation evidence;
* interpretation;
* hypothesis;
* unknowns.

Where practical, document:

```text
Problem
↓
Evidence
↓
Hypothesis
↓
Experiment
↓
Measurement
↓
Result
↓
Interpretation
↓
Limitations
```

A failed hypothesis is an acceptable result.

Unsupported certainty is not.

## Code Contributions

Implementation should not begin by assuming an architecture, language, framework, database, graph model, inference model, or deployment pattern merely because it appears sophisticated.

Implementation choices should follow requirements.

When code is introduced, contributions should eventually include appropriate validation such as tests, negative cases, failure handling, performance measurement, or reproducibility evidence according to the risk of the change.

## Documentation

Documentation is part of the engineering system.

Documentation must not describe planned functionality as implemented functionality.

Use explicit language such as:

* proposed;
* provisional;
* under research;
* planned;
* experimentally observed;
* not yet implemented;

when those qualifiers are required.

## Tool-Assisted Work

Tool-assisted contributions are permitted.

Generated output is not evidence by default.

The contributor remains responsible for correctness, licensing, security, provenance, validation, and every claim introduced into the repository.

Do not merge generated code or prose solely because it appears technically sophisticated.

## Security

Never include secrets, credentials, private keys, sensitive evidence, restricted datasets, or unsafe hostile samples in a contribution.

Security vulnerabilities should follow `SECURITY.md`, not public issue disclosure when the report contains sensitive exploit information.

## Safety Boundary

Contributions must remain within ELENCHION's defensive mission.

The project does not accept deployable malware, credential theft, ransomware, offensive persistence infrastructure, real-world command-and-control systems, payload-delivery infrastructure, or real-target attack automation.

## Definition of Done

A change is not complete merely because it compiles, renders, or passes CI.

Depending on scope, completion may require:

```text
Problem understood
↓
Change implemented
↓
Failure cases considered
↓
Validation completed
↓
Diff reviewed
↓
Claims checked against evidence
↓
Documentation updated
↓
Signed commit
↓
Pull-request review
```

The amount of process should remain proportional to the risk and significance of the change.

## Final Principle

> Build only what survives evidence, measurement, falsification, and adversarial review.
