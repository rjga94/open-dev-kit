# Open Development Kit (ODK)

ODK is a modular AI development kit for AI assisted software development. It provides an orchestrator plus focused specialist agents for project readiness,
implementation, OpenSpec workflows, and optional modules.

## What is included

- **ODK orchestrator**: the main user-facing agent and delegation coordinator.
- **Readiness specialist**: assesses project guidance and prepares approved
  updates for AI-assisted development.
- **Implementation specialist**: carries out approved software changes.
- **OpenSpec workflows**: explore, propose, apply, and archive project changes.
- **Optional modules**: capabilities such as the Wiki module can be installed
  only when selected.

ODK core installation and optional-module setup are intentionally separate.
Core installation does not enable optional modules or seed module data.

## Install

Follow [INSTALL.md](INSTALL.md) to install ODK into an existing or new project.
Installation guidance resolves the requested GitHub repository revision,
preserves existing files, and reports conflicts before writing.

After core installation, select **ODK** in the VS Code Agent picker. Run
`/odk-readiness-check` to assess the project and choose optional modules.

## Documentation

- [Installation guide](INSTALL.md)
- [Module maintenance and contribution guide](CONTRIBUTING.md)
- [OpenSpec project specifications](openspec/specs/)

## Contributing

Repository maintenance guidance is in [CONTRIBUTING.md](CONTRIBUTING.md).
Changes to observable behavior should also update the relevant OpenSpec
specifications.

## License

This project is licensed under the [MIT License](LICENSE).
