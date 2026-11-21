# Spec Delta

## MODIFIED Requirements

### Requirement: Readiness refactor is available after bootstrap
After bootstrap, the user SHALL be able to invoke `/odk-readiness-check` through the orchestrator, which SHALL delegate readiness assessment to the internal Readiness specialist.

#### Scenario: User starts readiness refactor
- **WHEN** the user invokes `/odk-readiness-check`
- **THEN** the orchestrator delegates project assessment to the core Readiness specialist

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
