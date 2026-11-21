# Spec Delta

## MODIFIED Requirements

### Requirement: User selects optional kit modules during bootstrap
The GitHub-hosted install guidance SHALL install the core orchestrator, Readiness specialist, and Implementation specialist without asking about optional modules. After core installation, `/odk-readiness-refactor` SHALL ask which optional modules to enable and SHALL enable only those selected after the user approves the proposed changes. It SHALL NOT seed module data.

#### Scenario: User selects optional modules
- **WHEN** the user selects one or more optional modules during `/odk-readiness-refactor`
- **THEN** only the selected optional modules are enabled in addition to the core kit

#### Scenario: User selects no modules
- **WHEN** the user selects no optional modules during `/odk-readiness-refactor`
- **THEN** no optional modules are enabled and the core orchestrator, Readiness specialist, and Implementation specialist remain installed

#### Scenario: Wiki is selected
- **WHEN** the user selects the Wiki module during `/odk-readiness-refactor`
- **THEN** the approved setup enables its commands without creating or seeding Wiki content

### Requirement: Bootstrap guidance is available before installation
The kit source SHALL include canonical installation guidance in `INSTALL.md` that an AI can retrieve from the supplied GitHub repository and follow when the user requests installation in an ordinary chat prompt. Initial installation SHALL NOT depend on a pre-installed kit skill.

#### Scenario: User starts from a clean project
- **WHEN** the user asks an AI to install the kit from its GitHub repository in a project with no kit skills installed
- **THEN** the AI can retrieve and follow `INSTALL.md` to install core kit content without an installation interview

### Requirement: Bootstrap preserves existing project files
The installation workflow SHALL preserve existing project and Wiki content. Before writing any core kit file, it SHALL check for conflicts; if any core target conflicts with existing content, it SHALL report the conflicting paths and stop without writing any core files.

#### Scenario: No file conflict
- **WHEN** all core kit target paths are absent or already contain the same ODK content
- **THEN** the installer adds missing core files and leaves existing files unchanged

#### Scenario: File conflict
- **WHEN** any core kit target path contains different content
- **THEN** the installer reports the conflicting path or paths and stops before writing any core files

### Requirement: Workspace Allow all requires explicit opt-in
The Readiness workflow SHALL check the workspace's default permissions before offering to set new chat sessions to Allow all, shall offer the setting only when it is not already enabled, and SHALL NOT change user-wide settings. The core installation workflow SHALL NOT offer or change this setting.

#### Scenario: User opts in to workspace Allow all
- **WHEN** the user explicitly accepts the Allow all option during `/odk-readiness-refactor`
- **THEN** the workspace default for new chat sessions is set to Allow all and the user is told it applies to all agents in that workspace

#### Scenario: User declines workspace Allow all
- **WHEN** the user declines the Allow all option during `/odk-readiness-refactor`
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
