# Spec Delta

## ADDED Requirements

### Requirement: Readiness clarification questions use bounded choices
The orchestrator SHALL ask each unresolved readiness decision as one focused question with concise, closed answer choices grounded in the specialist's evidence. It SHALL not require a free-form explanation or ask about a topic already established by evidence or prior user input.

#### Scenario: Project-specific gap needs clarification
- **WHEN** Readiness reports an unresolved project-specific gap
- **THEN** the orchestrator asks one focused question and provides a small set of evidence-based choices that directly resolve that gap

#### Scenario: A topic is already clear or answered
- **WHEN** evidence or prior user input resolves a readiness topic
- **THEN** the orchestrator does not ask a duplicate question about it

#### Scenario: A selected module requires a setup decision
- **WHEN** selected-module guidance identifies an unanswered decision that affects setup
- **THEN** the orchestrator presents only that decision with the concise choices defined by the selected module's authoritative install guide

### Requirement: Built-in readiness prompts use canonical wording and answer formats
The readiness workflow SHALL define exact text and bounded answer formats for built-in setup prompts, and SHALL present each prompt only when its existing applicability conditions are met.

#### Scenario: Optional module setup is pending
- **WHEN** optional-module setup is pending or the user explicitly requests a module change
- **THEN** the orchestrator presents modules from the authoritative catalog one at a time, asking “Would you like to enable the `<module>` module?” with “Yes” and “No” choices; answering “No” for every module is a valid empty selection

#### Scenario: User selects a module
- **WHEN** the user answers “Yes” for an optional module
- **THEN** before asking about the next module or preparing the setup plan, the orchestrator consults only that selected module’s manifest and install guide and asks any unanswered setup questions from the guide; if none remain, it proceeds without an extra interview

#### Scenario: User selects no modules
- **WHEN** the user answers “No” for every available optional module
- **THEN** readiness treats the selection as empty and does not load module manifests or guides as setup inputs

#### Scenario: Workspace Allow All is not enabled
- **WHEN** workspace approvals are absent or are not set to `allowAll`
- **THEN** the orchestrator asks “Enable Allow All approvals for this workspace?” with “Enable” and “Leave unchanged” choices

#### Scenario: OpenSpec project setup is needed
- **WHEN** readiness finds the official CLI or project-scoped OpenSpec skills are missing
- **THEN** the orchestrator asks “Would you like me to prepare a project-scoped OpenSpec setup plan for this workspace?” with “Yes” and “No” choices

### Requirement: Readiness dispatches to enabled module workflows
For each enabled module, the orchestrator SHALL invoke its declared module-owned readiness workflow and communicate its findings. Newly selected modules SHALL be checked only after successful enablement; unselected or incompletely installed modules SHALL NOT be checked.

#### Scenario: Enabled module declares readiness
- **WHEN** readiness runs for an enabled module that declares a readiness workflow
- **THEN** the orchestrator invokes that module's readiness workflow and communicates its findings

#### Scenario: Module was not enabled
- **WHEN** a module was declined, skipped, or incompletely installed
- **THEN** the orchestrator does not invoke that module's readiness workflow

#### Scenario: Enabled module has no readiness workflow
- **WHEN** an enabled module does not declare a readiness workflow
- **THEN** readiness skips module-specific checks without loading unselected module guidance

### Requirement: Readiness approvals remain separate, explicit decisions
The readiness workflow SHALL present plan, conflict-replacement, and documentation approvals separately from clarification answers, using a clear action choice for each approval.

#### Scenario: A setup plan is ready
- **WHEN** readiness presents the complete setup plan
- **THEN** the orchestrator asks “Do you approve this exact setup plan?” with “Approve” and “Decline” choices

#### Scenario: A destination conflicts with proposed content
- **WHEN** a planned destination contains conflicting content
- **THEN** the orchestrator asks “Replace the existing file at `<path>` with the proposed content?” with “Replace” and “Keep existing” choices

#### Scenario: Documentation changes are ready for review
- **WHEN** readiness presents the consolidated documentation preview
- **THEN** the orchestrator asks “Do you approve the proposed documentation changes?” with “Approve all,” “Approve selected files,” and “Decline” choices

## REMOVED Requirements

### Requirement: Readiness delegates Wiki integrity checks
The readiness workflow SHALL delegate Wiki presence and integrity checks to the Wiki specialist; the check SHALL be read-only.

#### Scenario: Wiki is missing
- **WHEN** readiness assessment finds no project Wiki
- **THEN** the orchestrator asks whether the user wants to seed one

#### Scenario: Wiki exists
- **WHEN** readiness assessment finds an existing Wiki
- **THEN** the Wiki specialist reports integrity findings for the orchestrator without changing Wiki content

**Reason**: Wiki health checks belong to the Wiki module rather than the core readiness workflow.
**Migration**: The core readiness workflow dispatches to the Wiki-owned readiness workflow after Wiki is enabled.

### Requirement: Wiki repair or seeding requires user choice
When readiness finds Wiki integrity issues, it SHALL present repair and reseeding options and SHALL make no Wiki changes until the user chooses an option and approves the proposed changes. Seeding SHALL also require explicit opt-in before scanning the repository and Git history.

#### Scenario: User chooses repair
- **WHEN** the user selects repair after reviewing the integrity findings
- **THEN** the Wiki specialist prepares a repair plan and waits for approval before changing the Wiki

#### Scenario: User chooses reseeding
- **WHEN** the user explicitly opts in to reseeding after reviewing the integrity findings
- **THEN** the Wiki specialist performs the seed operation under the Wiki seeding requirements

#### Scenario: User declines Wiki action
- **WHEN** the user declines repair or reseeding
- **THEN** the readiness workflow leaves the Wiki unchanged

**Reason**: Wiki data-operation choices and approvals are owned by the Wiki module.
**Migration**: The Wiki-owned readiness workflow presents these choices and delegates approved work under the existing Wiki seeding and repair requirements.

### Requirement: Readiness offers opted-in Archive Wiki capture
When OpenSpec is configured and the Wiki is initialized, Readiness SHALL offer a one-time project-level choice to update the Wiki automatically after successful OpenSpec Archive runs. The feature SHALL remain disabled unless the user opts in.

#### Scenario: Both OpenSpec and Wiki are ready
- **WHEN** readiness finds configured OpenSpec and an initialized Wiki
- **THEN** the orchestrator asks whether to enable automatic Wiki capture after successful Archive runs

#### Scenario: User opts in to Archive Wiki capture
- **WHEN** the user accepts the one-time opt-in
- **THEN** Readiness stores the project preference under `.opendevkit/`

#### Scenario: User declines Archive Wiki capture
- **WHEN** the user declines the one-time opt-in
- **THEN** automatic Wiki capture after Archive remains disabled

#### Scenario: Wiki is missing or not initialized
- **WHEN** OpenSpec is configured but the Wiki is not initialized
- **THEN** Readiness does not enable Archive Wiki capture and handles Wiki seeding through the existing opt-in flow

**Reason**: The post-Archive capture opt-in is a Wiki-specific readiness choice.
**Migration**: The Wiki-owned readiness workflow handles the opt-in while preserving the existing preference and capture behavior.
