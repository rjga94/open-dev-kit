---
type: architecture
title: OpenSpec integration
description: ODK adds project-owned orchestration around the official OpenSpec Explore, Propose, Apply, and Archive workflows.
sources:
  - resource: "project:.opendevkit/workflows/openspec-context.md"
  - resource: "project:.opendevkit/agents/implementation.md"
  - resource: "project:openspec/specs/openspec-workflow-integration/spec.md"
  - resource: "project:openspec/config.yaml"
---

# OpenSpec integration

ODK uses the official OpenSpec Explore, Propose, Apply, and Archive workflows.
It supplies relevant Wiki evidence to Explore, Propose, and Apply; Archive
runs without Wiki context. Approved Apply tasks are delegated to the core
Implementation specialist, which runs project-defined tests.

ODK-owned guidance is kept under `.opendevkit/` and in the project-owned
`openspec/config.yaml`, rather than modifying OpenSpec-generated skills. The
optional Verify workflow and machine-wide OpenSpec profile are not required
or changed by this integration.
