# Readiness: OpenSpec setup

This workflow detects and offers project-scoped OpenSpec setup. Never initialize or update a project with an unverified executable. Readiness reports findings to ODK; only ODK asks the user for approval.

## Detect the active CLI

1. Resolve every `openspec` executable, not only the first one on `PATH`. On Windows use `Get-Command -All openspec` and `where.exe openspec`; use the equivalent all-path lookup on other platforms.
2. For each resolved executable, record its absolute path and inspect only safe identity information such as `--version`, `--help`, package metadata, package-manager provenance, and installation source. Do not initialize a project while investigating provenance.
3. Verify that the executable is an official Fission-AI/OpenSpec distribution. Official references are the [Fission-AI/OpenSpec repository](https://github.com/Fission-AI/OpenSpec), its [official installation guide](https://openspec.dev/docs/installation), and the [`@fission-ai/openspec` npm package](https://www.npmjs.com/package/@fission-ai/openspec).
   - For npm, confirm the resolved package is the official package and was installed from the official registry release, not a local `file:` dependency, fork, workspace, or unknown source.
   - For the Windows standalone install, confirm its installed path and version against the official installer/release. If provenance cannot be established from available local evidence, treat it as unverified.
   - A package name or a `repository` field alone is not proof: inspect the resolved path and actual install provenance. A checkout with a fork origin is not an official release.
4. Verify the official CLI is compatible by checking its own `init --help` output for project scope and the `github-copilot` tool. The supported setup must allow project-scoped skills and must not require changing the machine-wide profile.
5. If more than one executable exists, identify any earlier PATH entry that shadows the verified official CLI. Do not silently change PATH or invoke an unverified shadow.

Return every relevant path, version, provenance evidence, supported setup flags, and shadowing/conflict findings to ODK. Do not report a CLI as verified when any required evidence is missing or contradictory.

## Offer installation or upgrade

- If a compatible official CLI is verified, tell ODK its path, version, and provenance. It may be reused only for a project setup the user explicitly approves.
- If the CLI is missing, incompatible, shadowed, or unverified, report the resolved path/version and why it cannot be used. Offer an official Windows install/update route, such as the standalone installer at `https://openspec.dev/cli/install.ps1` or the official `@fission-ai/openspec` npm package.
- Wait for explicit user approval before downloading, running an installer, installing/updating the package, or changing the active CLI. Do not replace an unverified executable or alter PATH silently.
- After an approved installation or update, resolve all `openspec` paths again and repeat version, provenance, scope, and shadow checks. Do not proceed unless the executable that will be invoked is now verified and compatible.
- If verification still fails, report the blocker and stop. Never fall back to the unverified executable.

## Inspect and initialize the project

Before any project setup, inspect existing OpenSpec configuration and installed skill files. If OpenSpec is already configured, integrate with it rather than overwriting or reinitializing its configuration. Preserve existing project context, specs, changes, skills, and unrelated files.

Present the exact proposed project changes and obtain explicit user approval before initialization. If there are legacy OpenSpec files or other conflicts that the CLI may remove or overwrite, enumerate them and stop for approval of that cleanup; do not use `--force`.

When approved, use only the verified executable by its resolved absolute path and select the GitHub Copilot tool with project scope, for example:

```text
openspec init --scope project --tools github-copilot --profile core
```

First confirm that the verified executable's `init --help` supports all specified options. The `core` profile is a per-invocation choice for the project setup; do not run `openspec config profile` or change the machine-wide workflow profile. Do not require or enable the optional Verify workflow.

Do not pass `--force`. If an existing project configuration or legacy file means the CLI may change content beyond the approved plan, stop and ask instead of relying on the CLI to preserve it. Do not run `openspec init` with a different executable after a verification or initialization error.

After successful project setup and approval of the integration, add the ODK-owned OpenSpec context from `.opendevkit/workflows/openspec-context.md` to the project's `openspec/config.yaml` `context` field. Preserve existing context verbatim and append the ODK guidance; if the merge would replace conflicting project instructions, show the proposed merged context and obtain approval first. Do not place Wiki page contents in the config.

## Verify and report

After an approved setup, verify the CLI path/version/provenance again and inspect the resulting project diff. Confirm that GitHub Copilot skills are project-scoped, existing OpenSpec configuration and project content were preserved, the machine-wide profile was not changed, and no Verify workflow was added by ODK.

Return to ODK the CLI evidence, user approval, exact files added or changed, verification outcomes, and any failures. Report setup as incomplete if any required check fails.
