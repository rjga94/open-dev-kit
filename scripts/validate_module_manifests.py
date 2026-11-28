#!/usr/bin/env python3
"""Validate the ODK module discovery catalog and module-owned install manifests."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


DEFAULT_CATALOG = ".opendevkit/agents/manifest.json"
PATH_CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f]")


def _safe_relative_path(value: Any, label: str, errors: list[str]) -> str | None:
    if not isinstance(value, str) or not value:
        errors.append(f"{label}: expected a non-empty relative path")
        return None
    if (
        "\\" in value
        or ":" in value
        or PATH_CONTROL_CHARS.search(value)
        or value.startswith("/")
    ):
        errors.append(f"{label}: unsafe path {value!r}")
        return None
    path = PurePosixPath(value)
    if any(part in ("", ".", "..") for part in value.split("/")):
        errors.append(f"{label}: path must not contain empty, '.' or '..' components")
        return None
    if path.as_posix() != value or ".git" in path.parts:
        errors.append(f"{label}: unsafe or non-canonical path {value!r}")
        return None
    return value


def _read_json(root: Path, relative_path: str, label: str,
               errors: list[str]) -> Any | None:
    path = root / relative_path
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root.resolve())
    except (OSError, ValueError):
        errors.append(f"{label}: file does not exist inside repository: {relative_path}")
        return None
    if not resolved.is_file():
        errors.append(f"{label}: not a file: {relative_path}")
        return None
    try:
        return json.loads(resolved.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{label}: cannot read valid JSON ({exc})")
        return None


def _check_source(root: Path, source: Any, label: str,
                  errors: list[str]) -> None:
    relative = _safe_relative_path(source, label, errors)
    if relative is None:
        return
    path = root / relative
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root.resolve())
    except (OSError, ValueError):
        errors.append(f"{label}: source does not exist inside repository: {relative}")
        return
    if not resolved.is_file():
        errors.append(f"{label}: source is not a file: {relative}")


def _check_destination(destination: Any, label: str,
                       errors: list[str]) -> str | None:
    return _safe_relative_path(destination, label, errors)


def validate_catalog(root: Path, catalog_path: str = DEFAULT_CATALOG) -> list[str]:
    """Return all catalog/module validation errors; an empty list means valid."""
    root = root.resolve()
    errors: list[str] = []
    catalog_relative = _safe_relative_path(catalog_path, "catalog path", errors)
    if catalog_relative is None:
        return errors
    catalog = _read_json(root, catalog_relative, "catalog", errors)
    if not isinstance(catalog, dict):
        if catalog is not None:
            errors.append("catalog: expected a JSON object")
        return errors
    if catalog.get("schemaVersion") != 1:
        errors.append("catalog: schemaVersion must be 1")
    modules = catalog.get("optionalModules")
    if not isinstance(modules, dict):
        errors.append("catalog: optionalModules must be an object")
        return errors

    all_targets: dict[str, str] = {}
    for module_id, reference in modules.items():
        label = f"module {module_id!r}"
        if not isinstance(module_id, str) or not module_id:
            errors.append(f"{label}: invalid module id")
            continue
        if not isinstance(reference, dict):
            errors.append(f"{label}: catalog reference must be an object")
            continue

        manifest_path = _safe_relative_path(
            reference.get("manifest"), f"{label} manifest reference", errors
        )
        guide_path = _safe_relative_path(
            reference.get("installGuide"), f"{label} installGuide reference", errors
        )
        if guide_path is not None:
            guide_file = root / guide_path
            try:
                guide_resolved = guide_file.resolve(strict=True)
                guide_resolved.relative_to(root)
                if not guide_resolved.is_file():
                    raise ValueError
            except (OSError, ValueError):
                errors.append(f"{label}: install guide does not exist inside repository: {guide_path}")

        if manifest_path is None:
            continue
        manifest = _read_json(root, manifest_path, f"{label} manifest", errors)
        if not isinstance(manifest, dict):
            if manifest is not None:
                errors.append(f"{label} manifest: expected a JSON object")
            continue
        if manifest.get("schemaVersion") != 1:
            errors.append(f"{label} manifest: schemaVersion must be 1")
        if manifest.get("id") != module_id:
            errors.append(f"{label} manifest: id must match catalog key {module_id!r}")

        files = manifest.get("files")
        if not isinstance(files, list):
            errors.append(f"{label} manifest: files must be an array")
            continue
        file_by_id: dict[str, dict[str, Any]] = {}
        for index, file_entry in enumerate(files):
            file_label = f"{label} manifest files[{index}]"
            if not isinstance(file_entry, dict):
                errors.append(f"{file_label}: expected an object")
                continue
            file_id = file_entry.get("id")
            if not isinstance(file_id, str) or not file_id:
                errors.append(f"{file_label}: id must be a non-empty string")
            elif file_id in file_by_id:
                errors.append(f"{file_label}: duplicate file id {file_id!r}")
            else:
                file_by_id[file_id] = file_entry
            _check_source(root, file_entry.get("source"), f"{file_label} source", errors)
            target = _check_destination(
                file_entry.get("installAs"), f"{file_label} installAs", errors
            )
            host = file_entry.get("host")
            adapters = manifest.get("adapters")
            valid_hosts = {"core"}
            if isinstance(adapters, dict):
                valid_hosts.update(adapters.keys())
            if not isinstance(host, str) or host not in valid_hosts:
                errors.append(f"{file_label}: host must be 'core' or a declared adapter")
            if target is not None:
                previous = all_targets.get(target)
                if previous is not None:
                    errors.append(
                        f"{file_label}: duplicate install target {target!r} "
                        f"(also declared by {previous})"
                    )
                else:
                    all_targets[target] = file_label

        if "readinessWorkflow" in manifest:
            readiness_workflow = manifest["readinessWorkflow"]
            if not isinstance(readiness_workflow, str) or not readiness_workflow:
                errors.append(
                    f"{label} manifest: readinessWorkflow must reference a declared file id"
                )
            elif readiness_workflow not in file_by_id:
                errors.append(
                    f"{label} manifest: readinessWorkflow must reference a declared file id"
                )

        adapters = manifest.get("adapters")
        if not isinstance(adapters, dict):
            errors.append(f"{label} manifest: adapters must be an object")
            continue
        for adapter_id, adapter in adapters.items():
            adapter_label = f"{label} adapter {adapter_id!r}"
            if not isinstance(adapter, dict):
                errors.append(f"{adapter_label}: expected an object")
                continue
            agent = adapter.get("agent")
            if not isinstance(agent, dict):
                errors.append(f"{adapter_label}: agent must be an object")
            else:
                for field, expected_host in (
                    ("specialistFile", "core"),
                    ("profileFile", adapter_id),
                ):
                    file_id = agent.get(field)
                    declared = file_by_id.get(file_id) if isinstance(file_id, str) else None
                    if declared is None:
                        errors.append(f"{adapter_label}: {field} must reference a declared file id")
                    elif declared.get("host") != expected_host:
                        errors.append(
                            f"{adapter_label}: {field} must reference a {expected_host!r} file"
                        )
            commands = adapter.get("commands")
            if not isinstance(commands, list) or not all(
                isinstance(item, str) and item for item in commands
            ):
                errors.append(f"{adapter_label}: commands must be an array of names")
            skills = adapter.get("skills")
            if not isinstance(skills, list):
                errors.append(f"{adapter_label}: skills must be an array")
                continue
            for index, skill in enumerate(skills):
                skill_label = f"{adapter_label} skills[{index}]"
                if not isinstance(skill, dict):
                    errors.append(f"{skill_label}: expected an object")
                    continue
                file_id = skill.get("file")
                declared = file_by_id.get(file_id) if isinstance(file_id, str) else None
                if declared is None:
                    errors.append(f"{skill_label}: file must reference a declared file id")
                elif declared.get("host") != adapter_id:
                    errors.append(f"{skill_label}: file must reference its adapter's file")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--catalog", default=DEFAULT_CATALOG)
    args = parser.parse_args()
    errors = validate_catalog(args.root, args.catalog)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Valid module catalog and manifests: {args.catalog}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
