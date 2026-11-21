# Spec Delta

## ADDED Requirements

### Requirement: Core bootstrap records its exact kit source
Core bootstrap MUST retain the source repository and exact ODK commit used to install the core kit so later optional-module setup can use the same version.

#### Scenario: Bootstrap uses a movable reference
- **WHEN** core bootstrap retrieves ODK from a branch, tag, or other movable reference
- **THEN** it records the resolved repository and immutable commit identifier used for the installed core kit

#### Scenario: Later module setup needs source files
- **WHEN** a selected optional module's functional files are not included with core ODK
- **THEN** readiness can identify the exact ODK repository and commit from the installed project's metadata

### Requirement: Core bootstrap retains module setup metadata without enabling modules
Core bootstrap SHALL install the optional-module catalog, each module's lightweight install manifest and setup guidance, and SHALL NOT install optional-module functional assets or data.

#### Scenario: Core installation completes without optional modules
- **WHEN** core bootstrap completes
- **THEN** the project has the metadata needed to discover and plan optional-module setup, while optional-module agents, skills, workflows, and runtime data remain uninstalled
