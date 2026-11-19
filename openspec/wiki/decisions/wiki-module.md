---
type: decision
title: Wiki module is optional
description: Bootstrap installs Wiki capabilities only when selected and does not seed Wiki data during installation.
sources:
  - resource: "project:BOOTSTRAP.md"
  - resource: "project:.opendevkit/agents/manifest.json"
  - resource: "project:.opendevkit/workflows/wiki-module.md"
  - resource: "project:openspec/specs/project-wiki/spec.md"
  - resource: "project:.opendevkit/config.json"
---

# Wiki module is optional

The ODK Wiki module is optional. Bootstrap installs its specialist and
`/odk-wiki-*` commands only when selected; installation does not create or
seed Wiki content. Capture requires an initialized Wiki, while repository and
Git-history seeding is a distinct, explicitly invoked operation with
pre-context screening requirements.

For this repository, `enabledModules` is currently empty and
`postArchiveWikiCapture` is `not-offered`. These are current local settings,
not a change to the kit's optional-module behavior.
