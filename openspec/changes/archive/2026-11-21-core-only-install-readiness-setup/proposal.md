# Proposal

## Why

The install guide currently combines core kit installation with choices about optional modules, workspace settings, and file conflicts. Splitting installation from those setup decisions makes the initial install smaller and gives the already-installed Readiness workflow one place to handle follow-up choices.

## What Changes

- Make `INSTALL.md` the canonical guide and limit it to installing ODK core functionality.
- Move the current installation interview and optional setup choices to `/odk-readiness-refactor`.
- Make core installation non-interactive: use the explicitly targeted current project, and preflight core files so any conflicting file causes the installer to report the path and stop before writing.
- Keep optional modules and workspace permission changes out of the initial core install; handle them through Readiness with explicit approval where changes are proposed.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `dev-kit-bootstrap`: Separate non-interactive core installation from optional setup and define conflict behavior.
- `project-readiness`: Own the post-install interview and approved optional ODK setup choices.

## Impact

The canonical install guide, ODK orchestrator guidance, Readiness skill and workflow, and the `dev-kit-bootstrap` and `project-readiness` specifications will change. Core installation will no longer install optional modules or change workspace permissions.
