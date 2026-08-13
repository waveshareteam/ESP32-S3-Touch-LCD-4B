#!/usr/bin/env python3
"""Route changed files to the smallest safe example-build matrix.

The router is deliberately fail-closed: an empty diff is an error and an
unrecognised non-documentation path schedules every example instead of silently
skipping product builds.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from discover_examples import discover_arduino, discover_esp_idf, normalize, selector_matches


IDF_VERSIONS = ("v5.5.5", "v6.0.2")
ARDUINO_CORE = "3.3.11"
ARDUINO_FQBN = (
    "esp32:esp32:esp32s3:USBMode=hwcdc,CDCOnBoot=cdc,FlashSize=16M,"
    "PartitionScheme=app3M_fat9M_16MB,PSRAM=opi"
)

DOCUMENT_SUFFIXES = {
    ".md",
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".sha256",
}
DOCUMENT_NAMES = {
    ".gitattributes",
    ".gitignore",
    "license",
    "license.md",
    "license.txt",
    "notice",
    "notice.md",
    "notice.txt",
}


@dataclass
class Route:
    idf_names: set[str] = field(default_factory=set)
    arduino_names: set[str] = field(default_factory=set)
    all_idf: bool = False
    all_arduino: bool = False
    firmware_changed: bool = False
    release_review: bool = False
    non_documentation_change: bool = False
    unknown_paths: list[str] = field(default_factory=list)

    def select_all(self) -> None:
        self.all_idf = True
        self.all_arduino = True


def is_documentation(path: str) -> bool:
    candidate = Path(path)
    lower = normalize(path).lower()
    return (
        candidate.suffix.lower() in DOCUMENT_SUFFIXES
        or candidate.name.lower() in DOCUMENT_NAMES
        or lower.startswith("docs/")
        or lower.startswith(".github/issue_template/")
        or lower == ".github/pull_request_template.md"
    )


def project_for(path: str, prefix: str, entries: list[dict[str, str]]) -> str | None:
    lower = normalize(path).lower()
    for entry in entries:
        entry_path = normalize(entry["path"]).lower()
        if lower == entry_path or lower.startswith(entry_path + "/"):
            return entry["name"]
    if lower.startswith(prefix):
        return None
    return None


def classify_paths(repo: Path, paths: list[str]) -> Route:
    if not paths:
        raise ValueError("changed-file set is empty; refusing to infer a build route")

    idf_entries = discover_esp_idf(repo)
    arduino_entries = discover_arduino(repo)
    route = Route()

    for raw_path in paths:
        path = normalize(raw_path)
        lower = path.lower()
        if not path:
            continue

        idf_name = project_for(path, "examples/esp-idf/", idf_entries)
        if idf_name:
            if not is_documentation(path):
                route.idf_names.add(idf_name)
            continue

        arduino_name = project_for(path, "examples/arduino/examples/", arduino_entries)
        if arduino_name:
            if not is_documentation(path):
                route.arduino_names.add(arduino_name)
            continue

        if lower.startswith("examples/arduino/libraries/"):
            if not is_documentation(path):
                route.all_arduino = True
            continue

        if lower.startswith("firmware/"):
            route.firmware_changed = True
            if lower == "firmware/checksums.sha256" or not is_documentation(path):
                route.release_review = True
            continue

        if lower.startswith("releases/"):
            if is_documentation(path):
                continue
            if lower.endswith(".py"):
                route.select_all()
            else:
                route.release_review = True
            continue

        if lower in {
            ".github/workflows/examples.yml",
            "scripts/discover_examples.py",
            "scripts/route_examples.py",
        } or lower.startswith("tests/test_ci_routing"):
            route.select_all()
            continue

        if is_documentation(path):
            continue

        if lower.startswith("examples/esp-idf/"):
            # A new, deleted, or renamed project may not exist in the checked-out
            # tree, so discovery cannot map it safely to one current project.
            route.all_idf = True
            continue

        if lower.startswith("examples/arduino/examples/"):
            route.all_arduino = True
            continue

        if (
            lower in {
                ".github/workflows/repository-checks.yml",
                ".github/dependabot.yml",
                ".github/codeql.yml",
                "scripts/check_repository.py",
            }
            or lower.startswith("config/")
        ):
            route.non_documentation_change = True
            continue

        route.unknown_paths.append(path)
        route.select_all()

    return route


def parse_name_status(text: str) -> list[str]:
    paths: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        fields = line.split("\t")
        if len(fields) == 1:
            paths.append(fields[0])
        elif fields[0].startswith(("R", "C")) and len(fields) >= 3:
            paths.extend((fields[1], fields[2]))
        else:
            paths.append(fields[-1])
    return list(dict.fromkeys(normalize(path) for path in paths if normalize(path)))


def git_changed_paths(repo: Path, base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-status", "--find-renames", f"{base}...{head}"],
        cwd=repo,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    return parse_name_status(result.stdout)


def select_entries(
    entries: list[dict[str, str]], selected: set[str], select_all: bool, selector: str
) -> list[dict[str, str]]:
    candidates = entries if select_all else [entry for entry in entries if entry["name"] in selected]
    return [entry for entry in candidates if selector_matches(entry, selector)]


def make_outputs(repo: Path, route: Route, selector: str) -> dict[str, object]:
    idf_entries = select_entries(discover_esp_idf(repo), route.idf_names, route.all_idf, selector)
    arduino_entries = select_entries(
        discover_arduino(repo), route.arduino_names, route.all_arduino, selector
    )
    idf_include = [entry | {"idf": version} for entry in idf_entries for version in IDF_VERSIONS]
    arduino_include = [
        entry | {"core": ARDUINO_CORE, "fqbn": ARDUINO_FQBN} for entry in arduino_entries
    ]
    no_builds = not idf_include and not arduino_include
    return {
        "idf_matrix": {"include": idf_include},
        "idf_count": len(idf_include),
        "arduino_matrix": {"include": arduino_include},
        "arduino_count": len(arduino_include),
        "docs_only": (
            no_builds
            and not route.release_review
            and not route.non_documentation_change
        ),
        "firmware_changed": route.firmware_changed,
        "release_review": route.release_review,
        "route": (
            "all"
            if route.all_idf and route.all_arduino and selector == "all"
            else "selected"
            if not no_builds
            else "no-example-builds"
        ),
        "unknown_paths": route.unknown_paths,
    }


def write_github_output(path: Path, outputs: dict[str, object]) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        for key, value in outputs.items():
            if isinstance(value, bool):
                rendered = str(value).lower()
            elif isinstance(value, (dict, list)):
                rendered = json.dumps(value, separators=(",", ":"))
            else:
                rendered = str(value)
            handle.write(f"{key}={rendered}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--all", action="store_true", help="schedule all discovered examples")
    mode.add_argument("--changed-files-from", type=Path)
    mode.add_argument("--base", help="base revision for a three-dot git diff")
    parser.add_argument("--head", help="head revision; required with --base")
    parser.add_argument("--selector", default="all")
    parser.add_argument("--github-output", type=Path)
    parser.add_argument("--strict-unknown", action="store_true")
    parser.add_argument("--expect-docs-only", action="store_true")
    parser.add_argument("--expect-no-example-builds", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    selector = normalize(args.selector)
    if args.base and not args.head:
        print("error: --head is required with --base", file=sys.stderr)
        return 2
    if args.head and not args.base:
        print("error: --head requires --base", file=sys.stderr)
        return 2

    try:
        if args.all:
            route = Route(all_idf=True, all_arduino=True)
        elif args.changed_files_from:
            paths = parse_name_status(args.changed_files_from.read_text(encoding="utf-8"))
            route = classify_paths(repo, paths)
        else:
            route = classify_paths(repo, git_changed_paths(repo, args.base, args.head))
        outputs = make_outputs(repo, route, selector)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    total = int(outputs["idf_count"]) + int(outputs["arduino_count"])
    if args.all and total == 0:
        print(f"error: selector {selector!r} matched no example", file=sys.stderr)
        return 2
    if args.strict_unknown and outputs["unknown_paths"]:
        print("error: unclassified paths: " + ", ".join(outputs["unknown_paths"]), file=sys.stderr)
        return 3
    if args.expect_docs_only and not outputs["docs_only"]:
        print("error: changed files were not classified as documentation-only", file=sys.stderr)
        return 4
    if args.expect_no_example_builds and total:
        print("error: changed files unexpectedly scheduled example builds", file=sys.stderr)
        return 4

    if args.github_output:
        write_github_output(args.github_output, outputs)
    print(json.dumps(outputs, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
