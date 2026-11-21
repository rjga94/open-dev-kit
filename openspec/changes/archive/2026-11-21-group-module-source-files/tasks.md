# Tasks

## 1. Group Wiki Module Sources

- [x] 1.1 Move the Wiki specialist instructions and profile template, Wiki skill sources, and Wiki-specific workflows under `.opendevkit/modules/wiki/`; verify the expected source files are present and their internal references resolve.
- [x] 1.2 Update the central manifest and all live installation, readiness, orchestrator, and module guidance references to the new source paths; verify the manifest parses, every declared source exists, and all `installAs` destinations remain unchanged.
- [x] 1.3 Search live kit sources for stale references to the old Wiki source locations and update them; verify the target project's `.opendevkit/wiki/` data path and shared core source paths are unchanged.

## 2. Validate the Source-Only Refactor

- [x] 2.1 Run `openspec validate group-module-source-files` and available repository-defined checks; verify the moved-source references are complete and installed behavior, commands, and destinations remain unchanged.
