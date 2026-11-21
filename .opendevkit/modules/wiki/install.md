# Wiki module installation

## Prerequisites

- The core ODK kit is installed and the user selected the Wiki module.
- This release supplies a GitHub Copilot adapter only. Do not claim or infer
  support for other hosts.
- Installation planning and applying changes remain under shared Readiness
  review, conflict handling, and explicit approval.

## Questions

No Wiki-specific answer is needed to install its files. Do not ask whether to
seed or repair Wiki data as part of module installation. If the user separately
requests a data operation, obtain its required explicit consent and follow that
operation's own workflow.

## Install and verify

Use this module's `manifest.json` as the sole source for its installable files,
host adapters, and destinations. Check that the selected module's declared
sources and targets are part of the shared approved plan. After installation,
verify the selected adapter files exist at their declared destinations and the
Wiki agent and skills route to the Wiki specialist.

Enabling the module does not create, seed, refresh, or repair `.opendevkit/wiki/`.
Seeding requires explicit invocation of `/odk-wiki-seed` or explicit opt-in
through Readiness and follows the seed workflow's screening requirements.
Repair or refresh of existing Wiki data is a separate operation requiring its
own explicit authorization. Wiki data operations may write only inside
`.opendevkit/wiki/`; module installation consent alone never authorizes them.
