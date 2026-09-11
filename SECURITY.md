# Security Policy

## Purpose

ELENCHION is defensive security research and engineering infrastructure.

Security reports are treated as engineering evidence. Reports should contain enough information to reproduce, bound, and evaluate the affected behavior without unnecessarily increasing public exposure.

## Reporting a Vulnerability

Do not disclose suspected vulnerabilities, credentials, secrets, private keys, sensitive evidence, or exploit details in a public GitHub issue.

When GitHub private vulnerability reporting is available for this repository, use that channel.

If private reporting is unavailable, contact the repository owner through the contact information published on the maintainer's GitHub profile.

A useful report should include, where available:

* affected component or document;
* affected commit, tag, or version;
* observed behavior;
* expected behavior;
* reproduction conditions;
* security impact;
* relevant logs or evidence;
* environment information;
* assumptions and uncertainty;
* suggested remediation, if known.

Do not include real third-party credentials, confidential datasets, malicious payloads, or unauthorized proprietary material.

## Scope

Security-relevant areas may eventually include:

* evidence integrity;
* provenance integrity;
* parser isolation;
* artifact handling;
* execution-worker containment;
* workload identity;
* authorization boundaries;
* secret isolation;
* plugin trust;
* sensor integrity;
* storage integrity;
* supply-chain provenance;
* update verification;
* auditability;
* resource exhaustion;
* unsafe deserialization or parsing;
* cross-tenant or cross-case isolation.

A security report does not need to fit an existing category to be valid.

## Defensive Research Boundary

ELENCHION does not accept contributions whose primary purpose is to provide:

* deployable malware;
* credential theft;
* ransomware;
* self-propagation;
* offensive persistence;
* real-world command-and-control infrastructure;
* payload-delivery infrastructure;
* real-target attack automation;
* offensive sandbox-evasion optimization.

Research into malicious behavior, anti-analysis techniques, parser abuse, and execution evasion is acceptable only when it serves defensive observability, containment, measurement, validation, or detection.

## Evidence Standard

A security conclusion should distinguish between:

* directly observed behavior;
* deterministic derivation;
* inference;
* hypothesis;
* contradiction;
* unknown or unverified state.

Where uncertainty exists, preserve it.

A plausible explanation is not automatically a verified vulnerability.

## Sensitive Material

Never commit or attach:

* private SSH keys;
* API tokens;
* passwords;
* authentication cookies;
* recovery codes;
* production credentials;
* private certificates;
* confidential forensic evidence;
* restricted datasets;
* hostile samples that create unnecessary distribution risk.

If sensitive information is accidentally committed, treat the credential or artifact as compromised even if the Git history is later rewritten.

## Supported Versions

ELENCHION is currently in **Phase Zero: Research and Thesis Validation**.

There is no production release line or supported-version matrix yet.

Security support policy will become versioned when the project begins publishing supported releases.

## Disclosure

The project favors coordinated remediation before public technical disclosure when premature disclosure would create avoidable risk.

Public advisories should separate verified facts from assumptions and should identify affected versions or commits whenever possible.

## Security Principle

> Security claims require evidence.

A control is not considered effective merely because it exists in documentation or configuration.

Where practical, security properties should eventually be supported by tests, policy evidence, architecture boundaries, reproducible validation, or independent assessment.
