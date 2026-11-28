# Tasks

## 1. Core module-readiness dispatch

- [x] 1.1 Add an optional manifest reference to a module-owned readiness workflow; update manifest validation and tests for valid, missing, and absent references; verify with `python3 scripts/validate_module_manifests.py` and `python3 -m unittest discover -s tests -p 'test_module_manifest_validator.py'`.
- [x] 1.2 Make core readiness a generic dispatcher: ask the per-module Yes/No question, resolve install-guide questions immediately after Yes, then invoke a declared module readiness workflow only after successful enablement; remove Wiki-specific readiness branches from core guidance and test sequencing and skip conditions with `python3 -m unittest discover -s tests -p 'test_readiness_module_guidance.py'`.

## 2. Wiki-owned readiness

- [x] 2.1 Add a manifest-declared Wiki readiness workflow for post-enable health checks and Wiki-specific prompts; move the missing/integrity, seed/repair/reseed, and post-Archive opt-in behavior out of core readiness while preserving separate opt-ins and approvals; extend focused tests and verify with `python3 -m unittest discover -s tests -p 'test_readiness_module_guidance.py'`, `python3 scripts/validate_module_manifests.py`, and `python3 -m unittest discover -s tests -p 'test_module_manifest_validator.py'`.

## 3. Integration

- [x] 3.1 Run the complete test suite with `python3 -m unittest discover -s tests` and validate the change with `openspec validate define-readiness-question-prompts --type change --strict`.
