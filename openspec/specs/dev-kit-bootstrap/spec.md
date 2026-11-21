# dev-kit-bootstrap Specification

## Purpose

This capability lets a user bootstrap selected AI development kit modules into an existing or new project through a guided, VS Code-compatible workflow.

## Requirements

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

### Requirement: Readiness is a core specialist
The kit SHALL include the internal Readiness specialist with the orchestrator in every installation; its availability SHALL NOT depend on optional module selection.

#### Scenario: Installation omits optional modules
- **WHEN** bootstrap completes with no optional modules selected
- **THEN** the user can still invoke the readiness-refactor workflow through the orchestrator

### Requirement: Implementation is a core specialist
The kit SHALL include an internal Implementation specialist in every installation to carry out approved software-change tasks.

#### Scenario: OpenSpec Apply requires implementation
- **WHEN** an approved OpenSpec change is applied
- **THEN** the orchestrator delegates implementation tasks to the core Implementation specialist

### Requirement: Bootstrap retrieves kit content from GitHub
The bootstrap workflow SHALL use a GitHub repository reference supplied by the user as the source for kit content and SHALL report a retrieval failure without claiming installation succeeded.

#### Scenario: Kit source is available
- **WHEN** the user supplies an accessible GitHub repository reference
- **THEN** the bootstrap installs the selected kit content from that source

#### Scenario: Kit source cannot be retrieved
- **WHEN** the supplied repository reference cannot be accessed
- **THEN** the bootstrap reports the failure and does not report a successful installation

### Requirement: Kit data has a project-local home
The bootstrap workflow SHALL place canonical kit configuration and module-owned project data under `.opendevkit/` in the target project.

#### Scenario: Selected module is installed
- **WHEN** the bootstrap installs a module into a project
- **THEN** its canonical configuration and project data are stored under `.opendevkit/`

### Requirement: Bootstrap guidance is available before installation
The kit source SHALL include canonical installation guidance in `INSTALL.md` that an AI can retrieve from the supplied GitHub repository and follow when the user requests installation in an ordinary chat prompt. Initial installation SHALL NOT depend on a pre-installed kit skill.

#### Scenario: User starts from a clean project
- **WHEN** the user asks an AI to install the kit from its GitHub repository in a project with no kit skills installed
- **THEN** the AI can retrieve and follow `INSTALL.md` to install core kit content without an installation interview

### Requirement: Kit commands use the odk prefix
Every user-invokable VS Code skill provided by the kit SHALL have a command name beginning with `odk-`.

#### Scenario: Kit skill is installed
- **WHEN** a module skill is installed in VS Code
- **THEN** its slash-command name begins with `/odk-`

#### Scenario: Bootstrap is complete
- **WHEN** the initial installation finishes
- **THEN** the kit does not require or install a persistent `/odk-install` command

### Requirement: Bootstrap preserves existing project files
The installation workflow SHALL preserve existing project and Wiki content. Before writing any core kit file, it SHALL check for conflicts; if any core target conflicts with existing content, it SHALL report the conflicting paths and stop without writing any core files.

#### Scenario: No file conflict
- **WHEN** all core kit target paths are absent or already contain the same ODK content
- **THEN** the installer adds missing core files and leaves existing files unchanged

#### Scenario: File conflict
- **WHEN** any core kit target path contains different content
- **THEN** the installer reports the conflicting path or paths and stops before writing any core files

### Requirement: Kit agents use the selected Copilot model
The ODK orchestrator and installed specialist agents SHALL use the model selected through the normal VS Code Copilot interface, without requiring a separate kit model or provider setting.

#### Scenario: User selects a Copilot model
- **WHEN** the user selects a model in the VS Code Copilot interface and invokes ODK
- **THEN** the orchestrator and its internal specialist agents use that selected model

#### Scenario: Kit has no separate model configuration
- **WHEN** the kit is installed or its agents are invoked
- **THEN** the user does not need to configure a kit-specific model or provider

### Requirement: The orchestrator is the sole user-facing agent
The kit SHALL expose the orchestrator as its only user-facing agent. User-invokable module commands SHALL enter through the orchestrator; specialized agents SHALL remain internal.

#### Scenario: User invokes a module command
- **WHEN** a user invokes an installed `/odk-*` module command
- **THEN** the request enters through the orchestrator rather than directly invoking a specialized agent

#### Scenario: VS Code discovers kit agents
- **WHEN** VS Code discovers the installed kit agents
- **THEN** only the orchestrator is exposed as a user-selectable agent

### Requirement: VS Code exposes an ODK Copilot facade
The bootstrap SHALL install a user-selectable VS Code Copilot agent facade for the orchestrator and hidden Copilot-native adapters for internal specialists. The facade and adapters SHALL use canonical instructions from `.opendevkit/` and SHALL NOT expose specialists as user-facing agents. The bootstrap SHALL explain that users select ODK from the Agent picker and SHALL NOT claim installation makes ODK the default chat agent.

#### Scenario: User selects ODK in VS Code
- **WHEN** the installed ODK custom agent appears in the VS Code agent picker
- **THEN** it represents the orchestrator and can access the canonical ODK instructions

#### Scenario: Internal specialist adapters are installed
- **WHEN** Readiness, Wiki, or Implementation adapters are installed for Copilot
- **THEN** they are available for orchestrator delegation and are not directly user-invocable

#### Scenario: Bootstrap completes
- **WHEN** ODK installation completes
- **THEN** the user is told to select ODK from the Agent picker, and the installation does not claim to change VS Code's default agent

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

### Requirement: Specialized agents communicate through the orchestrator
Specialized agents SHALL return results and clarification requests to the orchestrator and SHALL NOT communicate directly with users or other specialized agents.

#### Scenario: Specialist completes work
- **WHEN** a specialized agent completes its assigned task
- **THEN** it returns its result to the orchestrator for user-facing communication

#### Scenario: Specialist needs clarification
- **WHEN** a specialized agent cannot safely proceed without user input
- **THEN** it returns the clarification need to the orchestrator

### Requirement: The orchestrator delegates domain work
For an enabled module request, the orchestrator SHALL delegate domain-specific work to that module's specialized agent and SHALL pass only the request and context relevant to the task.

#### Scenario: Wiki request is routed
- **WHEN** a user invokes an enabled Wiki command
- **THEN** the orchestrator delegates Wiki work to the internal Wiki agent with scoped, relevant context

#### Scenario: Unrelated conversation context exists
- **WHEN** the conversation contains context unrelated to the delegated task
- **THEN** the orchestrator does not pass that context to the specialized agent by default

#### Scenario: Readiness request is routed
- **WHEN** a user invokes `/odk-readiness-refactor`
- **THEN** the orchestrator delegates project-readiness assessment to the core Readiness specialist

### Requirement: The orchestrator fans out meaningful independent work
When a request contains multiple meaningful, independent workstreams for different enabled specialists, the orchestrator SHALL delegate those workstreams concurrently. It SHALL keep trivial and single-domain requests focused rather than spawning unnecessary agents.

#### Scenario: Request has independent specialist workstreams
- **WHEN** a request contains multiple meaningful tasks that can be handled independently by different enabled specialists
- **THEN** the orchestrator starts all relevant specialist work concurrently, subject to runtime limits

#### Scenario: Request is simple or single-domain
- **WHEN** a request does not benefit from multiple specialist workstreams
- **THEN** the orchestrator does not fan out to multiple specialists

### Requirement: The orchestrator limits duplicate specialist instances
The orchestrator SHALL have at most one active instance per specialist relationship while allowing different relevant specialist relationships to run concurrently.

#### Scenario: Multiple tasks target the same specialist
- **WHEN** concurrent work would require more than one active instance of the same specialist relationship
- **THEN** the orchestrator queues or reassigns the additional work rather than creating a duplicate active instance

### Requirement: Parallel work has independent dependencies and write scopes
The orchestrator SHALL run tasks concurrently only when they have no unresolved dependencies and their write scopes do not overlap.

#### Scenario: Tasks have a dependency
- **WHEN** one delegated task depends on another task's result
- **THEN** the orchestrator runs the prerequisite first and delegates the dependent task afterward

#### Scenario: Tasks may modify the same resource
- **WHEN** delegated tasks have overlapping write scopes
- **THEN** the orchestrator serializes the conflicting work

### Requirement: The orchestrator adapts to specialist feedback
The orchestrator SHALL use positive or negative specialist results to revise remaining assignments, ordering, and continuation within the user's original request. It SHALL ask before expanding that scope.

#### Scenario: Specialist feedback changes the task plan
- **WHEN** a specialist result shows that remaining assignments should change
- **THEN** the orchestrator redirects, stops, or reorders pending work as needed within the original request

#### Scenario: Feedback implies broader work
- **WHEN** specialist feedback implies work outside the user's original request
- **THEN** the orchestrator asks the user before expanding that scope

### Requirement: The orchestrator joins required specialist work
The orchestrator SHALL wait until every required specialist task has completed or failed before presenting a final consolidated response, and SHALL disclose partial results and failures.

#### Scenario: All required specialist tasks finish
- **WHEN** every required parallel task has completed or failed
- **THEN** the orchestrator consolidates the results and identifies any incomplete or failed work

#### Scenario: A specialist fails while other work remains
- **WHEN** one specialist task fails while other independent tasks are still running
- **THEN** the orchestrator uses that failure as feedback to steer remaining work and reports the resulting partial outcome

### Requirement: Specialized agents own their domains
An available specialized agent SHALL perform work within its domain; the orchestrator SHALL NOT perform that domain work except through the approved unavailability fallback.

#### Scenario: Specialist is available
- **WHEN** a request requires work in an enabled specialist's domain
- **THEN** the specialist performs the domain work and the orchestrator coordinates and communicates the result

### Requirement: Orchestrator fallback requires disclosure and approval
If a specialized agent is missing, disabled, or cannot be loaded, the orchestrator SHALL disclose the unavailability and obtain user approval before performing that agent's domain work.

#### Scenario: User approves fallback
- **WHEN** the orchestrator has disclosed that the specialist is unavailable and the user approves fallback
- **THEN** the orchestrator may perform the requested domain work

#### Scenario: User declines fallback
- **WHEN** the user declines fallback
- **THEN** the orchestrator does not perform the specialized work

#### Scenario: Loaded specialist fails during execution
- **WHEN** an available specialist starts but encounters an execution failure
- **THEN** the orchestrator reports the failure and does not silently retry the domain work itself

### Requirement: Orchestrator responses are concise by default
The orchestrator SHALL keep user-facing responses brief and high-level by default, adding detail only when needed for accuracy, an action or decision, uncertainty or failure, or when requested. This rule SHALL NOT constrain internal specialist communication.

#### Scenario: User asks a straightforward question
- **WHEN** the orchestrator can answer without extensive explanation
- **THEN** it gives the direct answer without unnecessary background or repetition

#### Scenario: Details are needed
- **WHEN** additional detail is necessary to explain an action, decision, uncertainty, or failure
- **THEN** the orchestrator includes the relevant detail while keeping the response focused

#### Scenario: Specialist returns internal context
- **WHEN** a specialist reports findings, evidence, changes, or blockers to the orchestrator
- **THEN** the user-facing brevity rule does not remove information needed for orchestration

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
