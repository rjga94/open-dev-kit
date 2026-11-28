# project-readiness Specification

## Purpose

This capability assesses a project's readiness for effective AI-assisted development, interviews users only about unresolved gaps, and prepares approved updates to project guidance and documentation.

## Requirements

### Requirement: Readiness refactor is available after bootstrap
After bootstrap, the user SHALL be able to invoke `/odk-readiness-check` through the orchestrator, which SHALL delegate readiness assessment to the internal Readiness specialist.

#### Scenario: User starts readiness refactor
- **WHEN** the user invokes `/odk-readiness-check`
- **THEN** the orchestrator delegates project assessment to the core Readiness specialist

### Requirement: Readiness assessment uses current project evidence
The Readiness specialist SHALL inspect relevant project guidance, documentation, configuration, tests, and source code, and MAY inspect Git history as secondary context. It SHALL exclude secrets and credentials from model context.

#### Scenario: Current and historical evidence differ
- **WHEN** Git history conflicts with the current project state
- **THEN** the specialist treats current files as evidence of current implementation and history only as secondary context

#### Scenario: Sensitive material is encountered
- **WHEN** assessment encounters a secret or credential
- **THEN** that material is excluded from model context and generated guidance

### Requirement: Readiness topics are assessed adaptively
The specialist SHALL assess architecture, project-specific AI guidance, engineering standards, and testing scope, and MAY assess additional topics when relevant to the project. It SHALL classify topics as clear/current, partial or ambiguous, missing, stale, or contradictory.

#### Scenario: Topic is clear and current
- **WHEN** existing evidence clearly and consistently defines a topic
- **THEN** the specialist records it as clear/current and does not ask the user to repeat it

#### Scenario: Topic has an unresolved gap
- **WHEN** a topic is partial, ambiguous, missing, stale, or contradictory
- **THEN** the specialist returns the evidence and gap to the orchestrator for targeted clarification

### Requirement: Readiness interview asks only unresolved questions
The orchestrator SHALL ask targeted questions based on the Readiness specialist's findings and SHALL not ask about topics already clear and current.

#### Scenario: Project guidance is absent
- **WHEN** no project-specific AI guidance exists
- **THEN** the orchestrator asks whether the user wants such guidance and what it should cover

#### Scenario: Existing guidance needs clarification
- **WHEN** existing AI guidance is ambiguous, incomplete, or conflicts with current project evidence
- **THEN** the orchestrator asks only questions needed to clarify or resolve the identified gap

### Requirement: Readiness refactor prepares guidance and documentation updates
After the interview, the Readiness specialist SHALL prepare updates to host-readable AI guidance and relevant project documentation using existing project locations and conventions where possible. It SHALL NOT modify implementation code.

#### Scenario: Existing project documentation covers a topic
- **WHEN** relevant architecture, standards, or testing documentation already exists
- **THEN** the specialist updates the appropriate existing document rather than creating a duplicate

#### Scenario: A required document has no established location
- **WHEN** an agreed readiness topic needs documentation and no suitable file or project convention exists
- **THEN** the specialist includes the proposed new file and location in the change preview

### Requirement: Readiness changes require one consolidated approval
Before changing project guidance or documentation, the readiness workflow SHALL present a consolidated summary of proposed file changes and SHALL wait for user approval.

#### Scenario: User approves proposed changes
- **WHEN** the user approves the consolidated change summary
- **THEN** the Readiness specialist applies only the approved changes

#### Scenario: User declines proposed changes
- **WHEN** the user declines the consolidated change summary
- **THEN** no proposed guidance or documentation changes are applied

### Requirement: Readiness offers OpenSpec setup
The Readiness specialist SHALL detect whether a verified official OpenSpec CLI and project skills are available and SHALL ask before installing or initializing them.

#### Scenario: OpenSpec is not set up
- **WHEN** readiness finds the OpenSpec CLI or project skills are missing
- **THEN** the orchestrator offers to set up OpenSpec for the current VS Code Copilot project

#### Scenario: User declines OpenSpec setup
- **WHEN** the user declines the OpenSpec setup offer
- **THEN** readiness continues without installing or initializing OpenSpec

### Requirement: Readiness verifies official OpenSpec CLI identity
Before using the CLI for setup, Readiness SHALL identify the executable resolved on the machine, check its version and installation provenance, and verify it is an official Fission-AI/OpenSpec distribution that supports project-scoped GitHub Copilot setup.

#### Scenario: Compatible official CLI is installed
- **WHEN** the resolved CLI is verified as an official supported OpenSpec version
- **THEN** Readiness reports its path and version and reuses it

#### Scenario: CLI is unverified or from another project
- **WHEN** the resolved `openspec` command cannot be verified as an official distribution
- **THEN** Readiness reports the path and version and does not invoke or replace it

#### Scenario: Official CLI is incompatible
- **WHEN** the CLI is official but lacks the required project setup support
- **THEN** Readiness offers an official update and waits for approval before changing the installation

### Requirement: OpenSpec setup preserves user scope and profile
After user approval, Readiness SHALL use a verified official CLI to configure project-scoped GitHub Copilot OpenSpec skills without changing the machine-wide workflow profile or replacing existing project OpenSpec configuration.

#### Scenario: User approves project setup
- **WHEN** the user approves OpenSpec setup for the project
- **THEN** Readiness installs the project-scoped Copilot skills while preserving existing project configuration and the current machine-wide profile

#### Scenario: OpenSpec already exists
- **WHEN** the project already has OpenSpec configuration or skills
- **THEN** Readiness inspects and integrates with the existing setup rather than reinitializing or replacing it

#### Scenario: Official CLI is missing
- **WHEN** the user approves OpenSpec setup and no official CLI is installed
- **THEN** Readiness installs the CLI using official Fission-AI/OpenSpec instructions before initializing project skills

#### Scenario: Another CLI conflicts with official setup
- **WHEN** an unverified or incompatible `openspec` command is active on PATH
- **THEN** Readiness asks before installing or updating the official CLI and does not initialize project skills with the unverified command

### Requirement: Readiness interviews for optional ODK setup
After core installation, `/odk-readiness-check` SHALL check whether optional module setup is complete and ask for a selection only when it is incomplete or the user requests a change. It SHALL record an approved selection, including selecting no modules, so completed choices are not repeatedly requested. Setup SHALL remain pending if a selected module cannot be fully installed.

#### Scenario: Optional modules are available
- **WHEN** the user invokes `/odk-readiness-check` after core installation and optional module setup is incomplete
- **THEN** the orchestrator asks which optional modules to enable and explains that selecting none is valid

#### Scenario: Existing module configuration is present
- **WHEN** optional module setup is complete and the user has not requested a change
- **THEN** the orchestrator preserves the current selections and does not ask again

#### Scenario: Setup targets another workspace
- **WHEN** the user requests optional ODK setup for a workspace other than the active project
- **THEN** the orchestrator confirms the target workspace before preparing changes

#### Scenario: User selects no optional modules
- **WHEN** the user selects no optional modules and approves the setup
- **THEN** Readiness records the choice as complete and leaves optional modules disabled

### Requirement: Readiness prepares and approves optional ODK changes
Before changing optional ODK module files or configuration, Readiness SHALL prepare a plan of the proposed paths and changes, and ODK SHALL obtain explicit approval. Readiness SHALL preserve existing content and ask before replacing a conflicting optional-module file. It SHALL enable only modules whose approved setup completed.

#### Scenario: User approves optional setup
- **WHEN** the user approves the proposed optional ODK setup
- **THEN** Readiness applies only the approved module and configuration changes

#### Scenario: Optional module file conflicts
- **WHEN** an optional module target path contains different existing content
- **THEN** ODK identifies the path and asks before replacing it

#### Scenario: User declines a conflicting-file replacement
- **WHEN** the user declines replacement of a conflicting optional-module file
- **THEN** Readiness leaves all files for that module unchanged, does not enable that module, and keeps setup pending while it may proceed with other approved modules that remain safe

#### Scenario: User declines the proposed setup
- **WHEN** the user declines the optional ODK setup plan
- **THEN** Readiness leaves optional module files and configuration unchanged

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
