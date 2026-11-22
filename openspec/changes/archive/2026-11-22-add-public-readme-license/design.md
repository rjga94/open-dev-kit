# Design

## Context

See proposal.md for the motivation and public-release scope. The repository
currently has INSTALL.md and CONTRIBUTING.md but no root README or license.
The existing install guide already defines the supported bootstrap behavior,
so the README should orient users to it rather than duplicate or reinterpret
the procedure.

## Goals / Non-Goals

**Goals:**
- Give public users an immediate understanding of ODK and how to install or
  use it.
- Direct readers to the canonical installation and contribution documents.
- Add a standard MIT license with Ricardo Abreu identified as copyright holder.

**Non-Goals:**
- Document optional modules in exhaustive detail; link to repository-owned
  module guidance instead.
- Change installation behavior or contributor standards.
- Add badges, analytics, generated assets, or external service integrations.

## Decisions

1. **Use README.md as a concise, usage-first entry point.**

   Structure it with ODK identity, a short feature overview, installation,
   available modules, development/contribution links, and license. This keeps
   the README discoverable and avoids contradicting the detailed
   implementation rules in INSTALL.md and CONTRIBUTING.md.

   Alternative: a long README that repeats every install preflight rule.
   Rejected because it would duplicate canonical guidance and increase drift.

2. **Use the standard MIT license text in LICENSE.**

   Include the copyright line `Copyright (c) 2026 Ricardo Abreu`. The year
   follows the repository's current public-release year.

   Alternative: license the repository through package metadata or a
   CONTRIBUTING.md notice. Rejected because a root LICENSE is the conventional
   public repository marker and is easy for tooling and users to discover.

## Risks / Trade-offs

- README claims could become stale as modules or hosts are added.
  Mitigation: phrase supported entry points conservatively and link to the
  canonical manifest and install guide.
- Incorrect public-facing branding or ownership details could persist.
  Mitigation: keep the copy bounded to confirmed repository identity and
  Ricardo Abreu as the MIT copyright holder.
