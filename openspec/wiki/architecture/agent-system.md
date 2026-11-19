---
type: architecture
title: ODK agent system
description: The user-facing ODK facade coordinates core and optional specialist agents in VS Code Copilot.
sources:
  - resource: "project:.opendevkit/agents/manifest.json"
  - resource: "project:.opendevkit/agents/orchestrator.md"
  - resource: "project:.github/agents/odk.agent.md"
  - resource: "project:.opendevkit/config.json"
---

# ODK agent system

ODK is the only user-facing agent. It delegates readiness work to the core
Readiness specialist and approved software changes to the core Implementation
specialist. Wiki is an optional specialist enabled only when the project
selects that module. Specialist results and clarification needs return to ODK,
which owns user communication.

The manifest sets model selection to `inherit`; agents use the model selected
through the normal VS Code Copilot interface rather than a kit-specific model.
For this repository, `.opendevkit/config.json` currently has
`enabledModules: []`, so the optional Wiki module is not enabled here.
