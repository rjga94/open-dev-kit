# Proposal

## Why

ODK has no documented release workflow for an AI assistant to follow from a
simple chat request. Repository maintainers need consistent alpha versioning
and release notes based on the changes since the previous release.

## What Changes

- Add repository-local guidance for creating a Git tag and GitHub release from
  a requested commit.
- Review changes since the prior version and describe their impact, including
  breaking changes, in release notes.
- During alpha, start at `v0.1.0` if no version exists, increment the minor
  version for each subsequent release, and mark GitHub releases as pre-releases.
- Keep the major version at zero until the maintainer explicitly changes the
  policy.

## Capabilities

### New Capabilities

- `repository-releases`: Maintainer-directed version selection and publication
  of GitHub releases for ODK.

### Modified Capabilities

None.

## Impact

- Repository-local AI and contributor guidance, not files installed into ODK
  consumer projects.
- Git tags and GitHub Releases when a maintainer requests a release.
- No package publication or automatic release automation.
