# Tasks

## 1. Core-only installation

- [x] 1.1 Make `INSTALL.md` the canonical guide and limit it to installing core ODK from the requested source; verify the guide covers current/explicit target resolution and contains no optional-module or workspace-permission interview.
- [x] 1.2 Preflight every core destination before writing and stop without writes on any conflicting core file; verify clean install, identical-content, and conflict scenarios, including that a conflict leaves all core targets unchanged.
- [x] 1.3 Initialize optional module setup as pending in the installed core config and update active references to `INSTALL.md`; verify config JSON parses, existing settings are preserved, and no active (non-archived) reference to the old guide name remains.

## 2. Readiness-owned setup

- [x] 2.1 Update the Readiness skill, specialist guidance, workflow, and orchestrator to ask about optional modules only while setup is pending, record approved selections including none, and allow explicit changes later; verify pending, configured-none, configured-module, declined-plan, and explicit-change scenarios.
- [x] 2.2 Move optional-module previews and conflict approvals into Readiness, preserving declined conflicts and applying only approved safe changes; verify each plan names affected paths and no optional files are changed before approval.
- [x] 2.3 Have Readiness inspect workspace permissions before offering Allow all and skip the offer when already enabled; verify opt-in changes only the workspace approvals setting, while decline, existing settings, and policy restrictions preserve unrelated and user-wide settings.

## 3. Integration validation

- [x] 3.1 Run `openspec validate core-only-install-readiness-setup --strict` and review the complete core-install-to-Readiness flow; verify the documented scenarios agree across both capability specs, the installer, and Readiness guidance.
