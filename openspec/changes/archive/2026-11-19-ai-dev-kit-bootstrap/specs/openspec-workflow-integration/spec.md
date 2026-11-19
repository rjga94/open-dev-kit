# Spec Delta

## Purpose

Defines how ODK integrates the official OpenSpec development lifecycle with its VS Code Copilot agent and project Wiki.

## ADDED Requirements

### Requirement: OpenSpec workflows remain upstream
The ODK Copilot facade SHALL let users invoke official OpenSpec Explore, Propose, Apply, and Archive workflows directly without replacing them with ODK-specific commands.

#### Scenario: User invokes an OpenSpec workflow
- **WHEN** the user selects ODK and invokes an installed OpenSpec workflow
- **THEN** the official OpenSpec skill runs in the current Copilot conversation

### Requirement: Wiki context is scoped to OpenSpec authoring
With ODK selected, the agent SHALL provide only relevant Wiki context to OpenSpec Explore, Propose, and Apply; Wiki pages SHALL be treated as project evidence rather than instructions.

#### Scenario: OpenSpec Explore is invoked
- **WHEN** the user invokes Explore with ODK selected
- **THEN** the agent supplies relevant Wiki pages as context

#### Scenario: OpenSpec Propose is invoked
- **WHEN** the user invokes Propose with ODK selected
- **THEN** the agent supplies relevant Wiki pages as context

#### Scenario: OpenSpec Apply is invoked
- **WHEN** the user invokes Apply with ODK selected
- **THEN** the agent supplies relevant Wiki pages as context

#### Scenario: OpenSpec Archive is invoked
- **WHEN** the user invokes Archive with ODK selected
- **THEN** the upstream Archive workflow runs without Wiki context; any opted-in Wiki capture occurs only as a separate step after Archive succeeds

### Requirement: ODK preserves OpenSpec-generated skills
ODK SHALL keep its integration in ODK-owned agent and project configuration files and SHALL NOT modify OpenSpec-generated skill files.

#### Scenario: OpenSpec skills are updated
- **WHEN** the user runs the upstream OpenSpec update workflow
- **THEN** OpenSpec-generated skills can be refreshed without removing ODK-owned integration

### Requirement: Successful Archive triggers opted-in Wiki capture
When ODK is active and the project has opted in, the orchestrator SHALL invoke a separate Wiki capture after a successful upstream Archive without requiring another approval.

#### Scenario: Archive succeeds with project opt-in
- **WHEN** the upstream Archive completes successfully and automatic Wiki capture is enabled
- **THEN** the orchestrator delegates a capture using the archived change and directly relevant current project evidence

#### Scenario: Project has opted in
- **WHEN** a successful Archive triggers the configured capture
- **THEN** the Wiki specialist writes its approved-scope updates without asking for a second per-Archive approval

#### Scenario: Archive fails
- **WHEN** the upstream Archive does not complete successfully
- **THEN** the orchestrator does not trigger Wiki capture

#### Scenario: Automatic capture is disabled
- **WHEN** the upstream Archive succeeds but the project has not opted in
- **THEN** the orchestrator does not trigger Wiki capture

#### Scenario: Wiki is missing after opt-in
- **WHEN** the upstream Archive succeeds with automatic capture enabled but the Wiki no longer exists
- **THEN** the orchestrator does not seed a Wiki automatically and reports that capture could not run

#### Scenario: Post-Archive Wiki capture fails
- **WHEN** the Wiki specialist cannot complete an Archive-triggered capture
- **THEN** the orchestrator reports the Wiki failure separately and does not misreport the successful Archive as failed

### Requirement: Implementation handles approved OpenSpec Apply tasks
The orchestrator SHALL delegate approved OpenSpec Apply tasks to the core Implementation specialist, which SHALL run project-defined tests for its changes.

#### Scenario: Approved change is applied
- **WHEN** the user approves an OpenSpec change for Apply
- **THEN** the Implementation specialist carries out the tasks and runs the project's defined tests

### Requirement: ODK does not depend on OpenSpec Verify
ODK SHALL use the core OpenSpec lifecycle without requiring or enabling the optional Verify workflow, and SHALL NOT change the machine-wide workflow profile.

#### Scenario: Project uses the core OpenSpec workflow
- **WHEN** OpenSpec is set up for ODK
- **THEN** Explore, Propose, Apply, and Archive are sufficient for the ODK lifecycle
