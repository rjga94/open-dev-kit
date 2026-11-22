# Repository Releases

## ADDED Requirements

### Requirement: Explicit release skill invocation
The repository SHALL provide a manually invoked `/odk-release` skill that executes the maintainer release workflow for the requested commit, or the current commit when no target is specified.

#### Scenario: Maintainer invokes the release skill
- **WHEN** a maintainer invokes `/odk-release` for a commit
- **THEN** the AI identifies the target commit and follows the repository release workflow

#### Scenario: Maintainer invokes the skill without a target
- **WHEN** a maintainer invokes `/odk-release` without specifying a commit
- **THEN** the AI uses the current commit as the requested target

#### Scenario: Automatic invocation is disabled
- **WHEN** a user describes a release without explicitly invoking the skill
- **THEN** the skill is not automatically loaded by VS Code Copilot

## REMOVED Requirements

### Requirement: Natural-language release requests
**Reason**: The maintainer prefers an explicit slash command rather than automatic release routing.
**Migration**: Invoke `/odk-release` to run the repository release workflow.
