# Spec Delta

## ADDED Requirements

### Requirement: Wiki readiness is owned by the enabled Wiki module
The Wiki module SHALL declare its readiness workflow, and ODK SHALL invoke it only after the Wiki module is successfully enabled. The workflow SHALL perform read-only Wiki presence and integrity checks and return findings to ODK.

#### Scenario: Readiness reaches an enabled Wiki module
- **WHEN** readiness processes a successfully enabled Wiki module
- **THEN** ODK delegates Wiki-specific health checks to the module-owned readiness workflow and communicates its findings to the user

#### Scenario: Wiki is selected but not enabled
- **WHEN** Wiki installation has not completed successfully
- **THEN** readiness does not invoke Wiki health checks or its specialist

#### Scenario: Existing Wiki health check
- **WHEN** the enabled Wiki module's readiness workflow checks an existing Wiki
- **THEN** the check remains read-only and reports canonical OKF format, source provenance, references, index, taxonomy, and consistency

### Requirement: Wiki readiness asks bounded data-operation questions
The Wiki readiness workflow SHALL ask for explicit user choices before seeding, repairing, or reseeding Wiki data. A seed or reseed choice authorizes only the screened scan and proposal preparation, not writes; ODK SHALL obtain separate approval of proposed Wiki changes before writing.

#### Scenario: Wiki is missing
- **WHEN** Wiki readiness finds no initialized Wiki
- **THEN** ODK asks “Would you like to seed a Wiki by scanning this repository and its Git history?” with “Yes” and “No” choices, and begins no scan unless the user chooses “Yes”

#### Scenario: Missing-Wiki scan is declined
- **WHEN** the user answers “No” to the missing-Wiki seed prompt
- **THEN** readiness leaves the Wiki absent and starts no repository or Git-history scan

#### Scenario: Seed proposal is not yet approved
- **WHEN** the user opts in to seed or reseed and the specialist prepares proposed changes
- **THEN** ODK presents the proposed file changes and asks “Do you approve these proposed Wiki changes?” with “Approve” and “Decline” choices, obtaining separate explicit approval before any Wiki write

#### Scenario: Existing Wiki has integrity issues
- **WHEN** Wiki readiness reports integrity issues
- **THEN** ODK asks “How should I handle the Wiki issues?” with “Repair,” “Reseed from repository/history,” and “Leave unchanged” choices, and obtains separate approval for proposed Wiki changes before writing

#### Scenario: User chooses repair
- **WHEN** the user chooses “Repair”
- **THEN** the specialist prepares a repair proposal without a broad repository or Git-history scan, and makes no changes before ODK obtains separate approval

#### Scenario: User chooses reseed
- **WHEN** the user chooses “Reseed from repository/history”
- **THEN** readiness treats that choice as explicit opt-in to the screened scan, prepares a proposal, and makes no changes before separate approval

#### Scenario: User leaves an existing Wiki unchanged
- **WHEN** the user chooses “Leave unchanged”
- **THEN** readiness performs no repair, reseed, scan, or Wiki write

### Requirement: Post-Archive capture opt-in belongs to Wiki readiness
When OpenSpec and an initialized Wiki are available, Wiki readiness SHALL offer the one-time post-Archive capture choice only when `.opendevkit/config.json` has `preferences.postArchiveWikiCapture` set to `not-offered`. It SHALL record the explicit choice as `enabled` or `declined` without changing unrelated configuration.

#### Scenario: Post-Archive capture has not been offered
- **WHEN** OpenSpec and an initialized Wiki are available and the preference is `not-offered`
- **THEN** ODK asks “Enable automatic Wiki capture after OpenSpec Archive?” with “Enable” and “Leave disabled” choices

#### Scenario: User enables post-Archive capture
- **WHEN** the user chooses “Enable”
- **THEN** Readiness records the preference as `enabled` and automatic capture runs only after a successful OpenSpec Archive

#### Scenario: User declines post-Archive capture
- **WHEN** the user chooses “Leave disabled”
- **THEN** Readiness records the preference as `declined` and automatic capture remains disabled

#### Scenario: Post-Archive capture is gated
- **WHEN** OpenSpec is unavailable, the Wiki is not initialized, or the preference is not `not-offered`
- **THEN** readiness does not offer the choice or seed a missing Wiki to enable it
