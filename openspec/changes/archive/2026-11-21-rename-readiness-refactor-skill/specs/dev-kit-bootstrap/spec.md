# Spec Delta

## MODIFIED Requirements

### Requirement: User selects optional kit modules during bootstrap
The GitHub-hosted install guidance SHALL install the core orchestrator, Readiness specialist, and Implementation specialist without asking about optional modules. After core installation, `/odk-readiness-check` SHALL ask which optional modules to enable and SHALL enable only those selected after the user approves the proposed changes. It SHALL NOT seed module data.

#### Scenario: User selects optional modules
- **WHEN** the user selects one or more optional modules during `/odk-readiness-check`
- **THEN** only the selected optional modules are enabled in addition to the core kit

#### Scenario: User selects no modules
- **WHEN** the user selects no optional modules during `/odk-readiness-check`
- **THEN** no optional modules are enabled and the core orchestrator, Readiness specialist, and Implementation specialist remain installed

#### Scenario: Wiki is selected
- **WHEN** the user selects the Wiki module during `/odk-readiness-check`
- **THEN** the approved setup enables its commands without creating or seeding Wiki content

### Requirement: Readiness is a core specialist
The kit SHALL include the internal Readiness specialist with the orchestrator in every installation; its availability SHALL NOT depend on optional module selection.

#### Scenario: Installation omits optional modules
- **WHEN** bootstrap completes with no optional modules selected
- **THEN** the user can still invoke the readiness-check workflow through the orchestrator

### Requirement: Workspace Allow all requires explicit opt-in
The Readiness workflow SHALL check the workspace's default permissions before offering to set new chat sessions to Allow all, shall offer the setting only when it is not already enabled, and SHALL NOT change user-wide settings. The core installation workflow SHALL NOT offer or change this setting.

#### Scenario: User opts in to workspace Allow all
- **WHEN** the user explicitly accepts the Allow all option during `/odk-readiness-check`
- **THEN** the workspace default for new chat sessions is set to Allow all and the user is told it applies to all agents in that workspace

#### Scenario: User declines workspace Allow all
- **WHEN** the user declines the Allow all option during `/odk-readiness-check`
- **THEN** the workspace permission setting remains unchanged

#### Scenario: Workspace Allow all is already enabled
- **WHEN** the workspace default for new chat sessions is already Allow all
- **THEN** Readiness does not ask the user to enable it again

#### Scenario: Existing workspace settings are present
- **WHEN** the user opts in and `.vscode/settings.json` already contains settings
- **THEN** only the relevant chat permission setting is changed and unrelated settings are preserved

#### Scenario: VS Code or organization policy blocks Allow all
- **WHEN** workspace trust or organization policy prevents the permission setting from taking effect
- **THEN** the Readiness workflow reports that Allow all could not be enabled and does not attempt to bypass the restriction

### Requirement: The orchestrator delegates domain work
For an enabled module request, the orchestrator SHALL delegate domain-specific work to that module's specialized agent and SHALL pass only the request and context relevant to the task.

#### Scenario: Wiki request is routed
- **WHEN** a user invokes an enabled Wiki command
- **THEN** the orchestrator delegates Wiki work to the internal Wiki agent with scoped, relevant context

#### Scenario: Unrelated conversation context exists
- **WHEN** the conversation contains context unrelated to the delegated task
- **THEN** the orchestrator does not pass that context to the specialized agent by default

#### Scenario: Readiness request is routed
- **WHEN** a user invokes `/odk-readiness-check`
- **THEN** the orchestrator delegates project-readiness assessment to the core Readiness specialist
