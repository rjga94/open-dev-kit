# Proposal

## Why

The maintainer prefers an explicit slash command for ODK releases rather than
an always-applied instruction and a procedure in contributor documentation.

## What Changes

- Add a manually invoked, repository-local `/odk-release` skill containing the
  existing release procedure and safeguards.
- Remove the release procedure from `CONTRIBUTING.md` and the corresponding
  automatic release instruction from `.github/copilot-instructions.md`.
- Retain the current alpha version policy, release analysis, GitHub
  pre-release behavior, and failure handling.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `repository-releases`: Replace natural-language automatic routing with an
  explicitly invoked repository-local release skill.

## Impact

- Repository-local Copilot skill and contributor guidance.
- ODK installations into other projects remain unchanged.
- No release is published as part of this change.
