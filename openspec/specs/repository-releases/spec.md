# repository-releases Specification

## Purpose

Enable ODK maintainers to request consistent, traceable GitHub releases through AI chat.

## Requirements

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

### Requirement: Alpha version policy
While the maintainer has not explicitly changed the alpha policy, releases SHALL use `0.y.z` versions, start at `0.1.0` when no previous version exists, and increment the minor component and reset the patch component for each subsequent release.

#### Scenario: First alpha release
- **WHEN** no previous version exists and the first release is requested
- **THEN** the AI selects `v0.1.0`

#### Scenario: Subsequent alpha release
- **WHEN** the previous version is `v0.2.0` and a new release is requested
- **THEN** the AI selects `v0.3.0`

### Requirement: Release change analysis
The AI SHALL analyze all commits and relevant changes between the previous release and the target commit, identify user-visible changes and breaking changes, and use that analysis to prepare release notes.

#### Scenario: Changes include an incompatible modification
- **WHEN** the release range includes a breaking change
- **THEN** the release notes identify the breaking change and its impact

#### Scenario: First release has no previous version
- **WHEN** the first release is requested
- **THEN** the AI analyzes the available history through the target commit and prepares initial release notes

### Requirement: GitHub alpha releases
The AI SHALL publish alpha releases as GitHub pre-releases with a tag pointing to the requested commit.

#### Scenario: Alpha release is published
- **WHEN** the release is successfully published
- **THEN** the GitHub release is marked as a pre-release and references the selected version tag and target commit

### Requirement: Reliable publication
The AI SHALL verify the release baseline, target commit, chosen version, and publication result; it SHALL report errors and stop rather than overwrite an existing version or claim success when publication cannot be verified.

#### Scenario: Version already exists
- **WHEN** the chosen version tag or release already exists and does not represent the intended publication
- **THEN** the AI reports the conflict and does not overwrite it

#### Scenario: Baseline cannot be established
- **WHEN** the AI cannot establish a trustworthy previous release or complete change range
- **THEN** it reports the uncertainty and does not publish an unverified release

#### Scenario: Publication fails
- **WHEN** tagging or GitHub release creation fails
- **THEN** the AI reports the failure and any partially completed steps without claiming success

### Requirement: Repository-only guidance
Release guidance SHALL be maintained for this repository and SHALL NOT be installed into ODK consumer projects.

#### Scenario: ODK is installed in another project
- **WHEN** a user installs the ODK core kit
- **THEN** the repository's maintainer release guidance is not installed as kit functionality
