from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from route_examples import classify_paths, make_outputs, parse_name_status  # noqa: E402


class RoutingTests(unittest.TestCase):
    def route(self, *paths: str):
        return make_outputs(ROOT, classify_paths(ROOT, list(paths)), "all")

    def make_routing_repo(self, directory: str) -> Path:
        repo = Path(directory) / "repo"
        (repo / "scripts").mkdir(parents=True)
        for name in ("route_examples.py", "discover_examples.py"):
            shutil.copy2(SCRIPTS / name, repo / "scripts" / name)
        (repo / "examples/esp-idf/demo").mkdir(parents=True)
        (repo / "examples/esp-idf/demo/CMakeLists.txt").touch()
        (repo / "examples/arduino/examples/demo").mkdir(parents=True)
        (repo / "examples/arduino/examples/demo/demo.ino").touch()
        self.git(repo, "init", "--quiet")
        self.git(repo, "config", "user.name", "Routing test")
        self.git(repo, "config", "user.email", "routing-test@example.invalid")
        self.git(repo, "add", ".")
        self.git(repo, "commit", "--quiet", "-m", "baseline")
        return repo

    def git(self, repo: Path, *args: str) -> str:
        result = subprocess.run(
            ["git", *args],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def commit_path(self, repo: Path, path: str) -> tuple[str, str]:
        base = self.git(repo, "rev-parse", "HEAD")
        changed = repo / path
        changed.parent.mkdir(parents=True, exist_ok=True)
        changed.write_text("test fixture\n", encoding="utf-8")
        self.git(repo, "add", "--", path)
        self.git(repo, "commit", "--quiet", "-m", "change")
        return base, self.git(repo, "rev-parse", "HEAD")

    def run_git_route(self, repo: Path, base: str, head: str, *expectations: str):
        output = repo / "github-output"
        result = subprocess.run(
            [
                sys.executable,
                "scripts/route_examples.py",
                "--base",
                base,
                "--head",
                head,
                "--github-output",
                str(output),
                *expectations,
            ],
            cwd=repo,
            check=False,
            capture_output=True,
            text=True,
        )
        values = {}
        if output.exists():
            for line in output.read_text(encoding="utf-8").splitlines():
                key, value = line.split("=", 1)
                values[key] = json.loads(value) if value.startswith(("{", "[")) else value
        return result, values

    def test_inventory_is_stable(self):
        output = self.route(".github/workflows/examples.yml")
        self.assertEqual(output["idf_count"], 10)
        self.assertEqual(output["arduino_count"], 8)

    def test_docs_and_governance_skip_product_builds(self):
        output = self.route(
            "README.md",
            "docs/ci.md",
            "hardware/schematics/ESP32-S3-Touch-LCD-4B.pdf",
            "hardware/schematics/checksums.sha256",
            ".github/ISSUE_TEMPLATE/bug_report.md",
            "examples/esp-idf/README.md",
            "examples/esp-idf/02_lvgl_demo_v9/README.md",
            "examples/arduino/examples/01_HelloWorld/README_ZH.md",
        )
        self.assertEqual(output["idf_count"], 0)
        self.assertEqual(output["arduino_count"], 0)
        self.assertTrue(output["docs_only"])

    def test_unknown_hardware_source_fails_closed_to_all(self):
        output = self.route("hardware/tools/program_board.c")
        self.assertEqual(output["idf_count"], 10)
        self.assertEqual(output["arduino_count"], 8)
        self.assertEqual(output["unknown_paths"], ["hardware/tools/program_board.c"])

    def test_direct_projects_select_smallest_matrix(self):
        output = self.route(
            "examples/esp-idf/04_Immersive_block/main/main.c",
            "examples/arduino/examples/06_LVGL_Arduino_v9/06_LVGL_Arduino_v9.ino",
        )
        self.assertEqual(output["idf_count"], 2)
        self.assertEqual(output["arduino_count"], 1)
        self.assertEqual(
            {entry["name"] for entry in output["idf_matrix"]["include"]},
            {"04_Immersive_block"},
        )

    def test_bundled_library_source_selects_all_arduino(self):
        output = self.route("examples/arduino/libraries/Mylibrary/pin_config.h")
        self.assertEqual(output["idf_count"], 0)
        self.assertEqual(output["arduino_count"], 8)

    def test_firmware_boundary_never_builds_examples(self):
        output = self.route("firmware/factory.bin", "firmware/README.md")
        self.assertEqual(output["idf_count"], 0)
        self.assertEqual(output["arduino_count"], 0)
        self.assertTrue(output["firmware_changed"])
        self.assertTrue(output["release_review"])
        self.assertFalse(output["docs_only"])

    def test_firmware_readme_is_docs_only_but_tracks_firmware_boundary(self):
        output = self.route("firmware/README.md")
        self.assertEqual(output["idf_count"], 0)
        self.assertEqual(output["arduino_count"], 0)
        self.assertTrue(output["firmware_changed"])
        self.assertFalse(output["release_review"])
        self.assertTrue(output["docs_only"])

    def test_firmware_non_documentation_requires_release_review_without_example_builds(self):
        for path in (
            "firmware/release.tar.gz",
            "firmware/source.c",
            "firmware/config.json",
            "firmware/package.py",
            "firmware/checksums.sha256",
            "firmware/factory.bin",
        ):
            with self.subTest(path=path):
                output = self.route(path)
                self.assertEqual(output["idf_count"], 0)
                self.assertEqual(output["arduino_count"], 0)
                self.assertTrue(output["firmware_changed"])
                self.assertTrue(output["release_review"])
                self.assertFalse(output["docs_only"])

    def test_firmware_documentation_does_not_require_release_review_or_example_builds(self):
        for path in ("firmware/cover.png", "firmware/manual.pdf", "firmware/README.md"):
            with self.subTest(path=path):
                output = self.route(path)
                self.assertEqual(output["idf_count"], 0)
                self.assertEqual(output["arduino_count"], 0)
                self.assertTrue(output["firmware_changed"])
                self.assertFalse(output["release_review"])
                self.assertTrue(output["docs_only"])

    def test_release_helper_is_global_build_input(self):
        output = self.route("releases/package_firmware.py")
        self.assertEqual(output["idf_count"], 10)
        self.assertEqual(output["arduino_count"], 8)

    def test_static_checker_change_skips_builds_but_is_not_docs_only(self):
        output = self.route("scripts/check_repository.py")
        self.assertEqual(output["idf_count"], 0)
        self.assertEqual(output["arduino_count"], 0)
        self.assertFalse(output["docs_only"])

    def test_unknown_source_fails_closed_to_all(self):
        output = self.route("new-framework/tool.c")
        self.assertEqual(output["idf_count"], 10)
        self.assertEqual(output["arduino_count"], 8)
        self.assertEqual(output["unknown_paths"], ["new-framework/tool.c"])

    def test_rename_accounts_for_old_and_new_paths(self):
        paths = parse_name_status(
            "R100\texamples/esp-idf/01_AXP2101/main/main.cpp\t"
            "examples/esp-idf/02_lvgl_demo_v9/main/moved.cpp\n"
        )
        output = make_outputs(ROOT, classify_paths(ROOT, paths), "all")
        self.assertEqual(
            {entry["name"] for entry in output["idf_matrix"]["include"]},
            {"01_AXP2101", "02_lvgl_demo_v9"},
        )

    def test_empty_changed_file_is_hard_error(self):
        with tempfile.TemporaryDirectory() as directory:
            changed = Path(directory) / "changed.txt"
            changed.write_text("", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "route_examples.py"),
                    "--repo",
                    str(ROOT),
                    "--changed-files-from",
                    str(changed),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(result.returncode, 2)
        self.assertIn("changed-file set is empty", result.stderr)

    def test_cli_github_output_honors_documentation_expectations(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_routing_repo(directory)
            base, head = self.commit_path(repo, "firmware/README.md")
            result, output = self.run_git_route(
                repo, base, head, "--expect-docs-only", "--expect-no-example-builds"
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(output["docs_only"], "true")
        self.assertEqual(output["idf_count"], "0")
        self.assertEqual(output["arduino_count"], "0")
        self.assertEqual(output["release_review"], "false")

    def test_cli_github_output_rejects_docs_expectation_for_firmware_binary(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_routing_repo(directory)
            base, head = self.commit_path(repo, "firmware/factory.bin")
            success, output = self.run_git_route(repo, base, head, "--expect-no-example-builds")
            failure, _ = self.run_git_route(repo, base, head, "--expect-docs-only")
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(output["firmware_changed"], "true")
        self.assertEqual(output["release_review"], "true")
        self.assertEqual(output["docs_only"], "false")
        self.assertEqual(failure.returncode, 4)
        self.assertIn("not classified as documentation-only", failure.stderr)

    def test_cli_unknown_path_is_json_and_never_runs_shell_content(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_routing_repo(directory)
            sentinel = repo / "routing-sentinel"
            path = "new-framework/$(touch routing-sentinel).c"
            base, head = self.commit_path(repo, path)
            result, output = self.run_git_route(repo, base, head)
            self.assertFalse(sentinel.exists())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(output["unknown_paths"], [path])
        self.assertEqual(json.loads(result.stdout)["unknown_paths"], [path])
        self.assertEqual(output["idf_count"], "2")
        self.assertEqual(output["arduino_count"], "1")

    def test_brookesia_c_only_warning_suppressions_do_not_apply_to_cxx(self):
        cmake = (
            ROOT / "examples/esp-idf/03_esp-brookesia/components/apps/CMakeLists.txt"
        ).read_text(encoding="utf-8")
        for warning in ("-Wno-incompatible-pointer-types", "-Wno-int-conversion"):
            self.assertIn(f"$<$<COMPILE_LANGUAGE:C>:{warning}>", cmake)
            self.assertNotIn(f"COMPILE_LANGUAGE:CXX>:{warning}", cmake)
        self.assertIn("-Wno-format", cmake)
        self.assertIn("-DLV_LVGL_H_INCLUDE_SIMPLE", cmake)

    def test_workflow_exposes_routing_review_signals(self):
        workflow = (ROOT / ".github/workflows/examples.yml").read_text(encoding="utf-8")
        self.assertIn("--expect-docs-only --expect-no-example-builds", workflow)
        self.assertIn("unknown_paths", workflow)
        self.assertIn("release_review", workflow)
        self.assertIn("steps.route.outputs.docs_only == 'true'", workflow)
        self.assertIn("github.event_name != 'workflow_dispatch'", workflow)
        self.assertIn("github.ref_type != 'tag'", workflow)
        self.assertIn('test "$CLASSIFY_RESULT" = "success"', workflow)
        self.assertIn('[[ "$IDF_RESULT" == "success" || "$IDF_RESULT" == "skipped" ]]', workflow)
        self.assertIn(
            '[[ "$ARDUINO_RESULT" == "success" || "$ARDUINO_RESULT" == "skipped" ]]',
            workflow,
        )


if __name__ == "__main__":
    unittest.main()
