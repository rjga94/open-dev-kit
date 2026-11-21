# Spec Delta

## ADDED Requirements

### Requirement: Optional modules own their installation metadata
Each optional module SHALL provide a machine-readable manifest and installation guidance, and the central catalog SHALL reference each module's manifest instead of duplicating its source and destination mappings.

#### Scenario: Readiness prepares a selected module
- **WHEN** readiness prepares an installation plan for a selected optional module
- **THEN** it uses that module's manifest for source and destination mappings and its guidance for module-specific setup decisions

### Requirement: Readiness asks only selected modules' setup questions
After module selection, readiness SHALL consult only selected modules' installation guidance, ask only questions needed to resolve their setup choices, and include the answers in one consolidated installation plan.

#### Scenario: A selected module needs a setup choice
- **WHEN** a selected module's guidance identifies a required user decision not already answered
- **THEN** the orchestrator asks that targeted question before preparing the plan

#### Scenario: Selected modules need no additional choices
- **WHEN** the selected modules' installation guidance requires no unanswered setup decisions
- **THEN** readiness prepares the plan without an unnecessary module-specific interview

### Requirement: Readiness fetches module assets from one resolved ODK commit
Readiness SHALL use the repository and exact commit recorded during core bootstrap when available. If source provenance is absent, it SHALL resolve the latest commit from the canonical ODK repository and plan to refresh all ODK-managed core files and selected module assets from that same commit; it SHALL NOT mix revisions.

#### Scenario: The recorded source is available
- **WHEN** readiness prepares an optional-module installation plan from the recorded source
- **THEN** every fetched module asset comes from the recorded repository commit

#### Scenario: A legacy installation has no source provenance
- **WHEN** readiness prepares optional-module setup for a core installation without recorded source metadata
- **THEN** it resolves the latest canonical ODK commit and includes the complete ODK-managed core refresh and selected module assets from that same commit in one plan, even when the selection is empty

#### Scenario: The resolved source cannot be retrieved
- **WHEN** readiness cannot retrieve the resolved repository commit or a selected asset from it
- **THEN** it reports the failure and does not install or enable that module

#### Scenario: The legacy refresh plan is declined
- **WHEN** the user declines a plan containing a legacy core refresh and optional-module installation
- **THEN** readiness leaves core and module files unchanged and keeps optional-module setup pending
