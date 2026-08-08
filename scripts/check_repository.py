#!/usr/bin/env python3
"""Validate the public repository scaffold without requiring ESP-IDF."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = (
    ".gitattributes",
    ".gitignore",
    "CONTRIBUTING.md",
    "LICENSE.txt",
    "README.md",
    "README_CN.md",
    "README_ZH.md",
    "SECURITY.md",
    "SUPPORT.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/pull_request_template.md",
    ".github/workflows/repository-checks.yml",
    "docs/README.md",
    "docs/wiki-resources_CN.md",
    "examples/README.md",
    "examples/README_CN.md",
    "firmware/README.md",
    "firmware/README_CN.md",
    "hardware/README.md",
    "releases/README.md",
    "releases/download_artifacts.py",
    "releases/download_artifacts_impl.py",
    "releases/package_firmware.py",
    "scripts/check_repository.py",
    "scripts/discover_examples.py",
    "scripts/route_examples.py",
    "config/markdown-audit.json",
    "tests/test_ci_routing.py",
    "tests/test_package_firmware.py",
    "tests/test_repository_checks.py",
)

REQUIRED_DIRECTORIES = (
    ".github",
    "docs",
    "examples",
    "firmware",
    "hardware",
    "releases",
    "scripts",
    "config",
    "tests",
)

DISALLOWED_ROOT_NAMES = (
    "Arduino_Libraries",
    "Examples",
    "Firmware",
    "Hardware",
    "example",
    "example-idf",
    "examples_idf",
)

PUBLIC_TEXT_SUFFIXES = {".json", ".md", ".rst", ".txt", ".yaml", ".yml"}
SKIPPED_PARTS = {
    ".codex",
    ".git",
    ".pytest_cache",
    "__pycache__",
    "build",
    "components",
    "dist",
    "downloads",
    "libraries",
    "managed_components",
    "release-artifacts",
}

LOCAL_PATH_PATTERNS = (
    ("Windows absolute path", re.compile(r"(?i)(?<![A-Za-z])\b[A-Z]:[\\/]")),
    ("macOS user path", re.compile(r"/Users/[^/\s]+/")),
    ("Linux user path", re.compile(r"/home/[^/\s]+/")),
    ("UNC network path", re.compile(r"\\\\[^\\\s]+\\[^\\\s]+")),
)


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_skipped(path: Path, root: Path) -> bool:
    parts = path.relative_to(root).parts
    return any(part in SKIPPED_PARTS or part.startswith("build-") for part in parts)


def validate_required_paths(root: Path) -> list[str]:
    errors: list[str] = []

    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")

    for name in REQUIRED_DIRECTORIES:
        if not (root / name).is_dir():
            errors.append(f"missing required directory: {name}/")

    root_names = {path.name for path in root.iterdir()}
    for name in DISALLOWED_ROOT_NAMES:
        if name in root_names:
            errors.append(f"non-canonical root path: {name}")

    return errors


def validate_framework_layout(root: Path) -> list[str]:
    errors: list[str] = []
    examples_root = root / "examples"
    arduino_root = examples_root / "arduino"
    idf_root = examples_root / "esp-idf"

    ino_files = [
        path
        for path in root.rglob("*.ino")
        if path.is_file() and not is_skipped(path, root)
    ]
    for path in ino_files:
        if arduino_root not in path.parents:
            errors.append(
                f"Arduino sketch is outside examples/arduino/: {relative(path, root)}"
            )

    product_ino_files = [path for path in ino_files if arduino_root in path.parents]
    if arduino_root.is_dir() and not product_ino_files:
        errors.append("examples/arduino/ exists but contains no Arduino sketch")

    idf_projects: list[Path] = []
    for path in root.rglob("CMakeLists.txt"):
        if not path.is_file() or is_skipped(path, root):
            continue
        try:
            contents = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            errors.append(f"cannot read {relative(path, root)}: {exc}")
            continue
        if re.search(r"(?im)^\s*project\s*\(", contents):
            idf_projects.append(path.parent)

    allowed_firmware_root = root / "firmware"
    for project in idf_projects:
        if idf_root not in project.parents and allowed_firmware_root not in project.parents:
            errors.append(
                "ESP-IDF project is outside examples/esp-idf/ or firmware/: "
                f"{relative(project, root)}"
            )

    if idf_root.is_dir() and not any(idf_root in project.parents for project in idf_projects):
        errors.append("examples/esp-idf/ exists but contains no ESP-IDF project")

    return errors


def validate_public_text(root: Path) -> list[str]:
    errors: list[str] = []

    for path in root.rglob("*"):
        if (
            not path.is_file()
            or path.suffix.lower() not in PUBLIC_TEXT_SUFFIXES
            or is_skipped(path, root)
        ):
            continue

        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError as exc:
            errors.append(f"cannot read {relative(path, root)}: {exc}")
            continue

        for line_number, line in enumerate(lines, start=1):
            for label, pattern in LOCAL_PATH_PATTERNS:
                if pattern.search(line):
                    errors.append(
                        f"{relative(path, root)}:{line_number}: contains {label}"
                    )

    return errors


def validate_markdown_links(root: Path) -> list[str]:
    errors: list[str] = []
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    uri_scheme = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")

    for path in root.rglob("*.md"):
        if not path.is_file() or is_skipped(path, root):
            continue

        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError as exc:
            errors.append(f"cannot read {relative(path, root)}: {exc}")
            continue

        in_fence = False
        for line_number, line in enumerate(lines, start=1):
            if re.match(r"^\s*(```|~~~)", line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in link_pattern.finditer(line):
                destination = match.group(1).strip().strip("<>")
                if (
                    not destination
                    or destination.startswith(("#", "//"))
                    or uri_scheme.match(destination)
                ):
                    continue

                destination = destination.split("#", maxsplit=1)[0].split("?", maxsplit=1)[0]
                linked_path = (path.parent / destination).resolve()
                try:
                    linked_path.relative_to(root)
                except ValueError:
                    errors.append(
                        f"{relative(path, root)}:{line_number}: link leaves repository: "
                        f"{destination}"
                    )
                    continue

                if not linked_path.exists():
                    errors.append(
                        f"{relative(path, root)}:{line_number}: missing link target: "
                        f"{destination}"
                    )

    return errors


def load_markdown_policy(root: Path) -> tuple[dict, list[str]]:
    path = root / "config" / "markdown-audit.json"
    try:
        policy = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {}, [f"cannot read Markdown audit policy: {exc}"]
    if not isinstance(policy, dict):
        return {}, ["config/markdown-audit.json: top-level value must be an object"]
    patterns = policy.get("exclude_patterns", [])
    if not isinstance(patterns, list) or not all(isinstance(item, str) for item in patterns):
        return {}, ["config/markdown-audit.json: exclude_patterns must be a string list"]
    return policy, []


def validate_bilingual_markdown(root: Path, policy: dict) -> list[str]:
    errors: list[str] = []
    excluded = policy.get("exclude_patterns", [])

    for english in root.rglob("*.md"):
        if not english.is_file() or is_skipped(english, root):
            continue
        rel = relative(english, root)
        if any(fnmatch.fnmatchcase(rel, pattern) for pattern in excluded):
            continue
        if english.stem.endswith(("_ZH", "_CN")):
            continue

        chinese = english.with_name(f"{english.stem}_ZH.md")
        if not chinese.is_file():
            errors.append(f"missing Simplified-Chinese companion: {relative(chinese, root)}")
            continue

        try:
            english_text = english.read_text(encoding="utf-8", errors="replace")
            chinese_text = chinese.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            errors.append(f"cannot read bilingual pair for {rel}: {exc}")
            continue

        if chinese.name not in english_text:
            errors.append(f"{rel}: missing language link to {chinese.name}")
        if english.name not in chinese_text:
            errors.append(
                f"{relative(chinese, root)}: missing language link to {english.name}"
            )

    return errors


def validate_checksum_manifests(root: Path) -> list[str]:
    errors: list[str] = []
    for manifest in (
        root / "firmware" / "checksums.sha256",
        root / "hardware" / "schematics" / "checksums.sha256",
    ):
        if not manifest.is_file():
            errors.append(f"missing checksum manifest: {relative(manifest, root)}")
            continue
        for line_number, raw_line in enumerate(
            manifest.read_text(encoding="utf-8", errors="replace").splitlines(), start=1
        ):
            line = raw_line.strip()
            if not line:
                continue
            match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
            if not match:
                errors.append(
                    f"{relative(manifest, root)}:{line_number}: invalid SHA-256 entry"
                )
                continue
            expected, filename = match.groups()
            target = (manifest.parent / filename).resolve()
            try:
                target.relative_to(manifest.parent.resolve())
            except ValueError:
                errors.append(
                    f"{relative(manifest, root)}:{line_number}: checksum path leaves its directory"
                )
                continue
            if not target.is_file():
                errors.append(
                    f"{relative(manifest, root)}:{line_number}: missing checksummed file: {filename}"
                )
                continue
            with target.open("rb") as source:
                actual = hashlib.file_digest(source, "sha256").hexdigest()
            if actual.lower() != expected.lower():
                errors.append(
                    f"{relative(manifest, root)}:{line_number}: checksum mismatch: {filename}"
                )
    return errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    policy, policy_errors = load_markdown_policy(root)
    errors.extend(policy_errors)
    errors.extend(validate_required_paths(root))
    errors.extend(validate_framework_layout(root))
    errors.extend(validate_public_text(root))
    errors.extend(validate_markdown_links(root))
    if not policy_errors:
        errors.extend(validate_bilingual_markdown(root, policy))
    errors.extend(validate_checksum_manifests(root))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root; defaults to the parent of scripts/",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = validate(root)

    if errors:
        print("Repository checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
