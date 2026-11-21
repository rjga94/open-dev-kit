# Spec Delta

## ADDED Requirements

### Requirement: Readiness interviews for optional ODK setup
After core installation, `/odk-readiness-refactor` SHALL check whether optional module setup is complete and ask for a selection only when it is incomplete or the user requests a change. It SHALL record an approved selection, including selecting no modules, so completed choices are not repeatedly requested. Setup SHALL remain pending if a selected module cannot be fully installed.

#### Scenario: Optional modules are available
- **WHEN** the user invokes `/odk-readiness-refactor` after core installation and optional module setup is incomplete
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
