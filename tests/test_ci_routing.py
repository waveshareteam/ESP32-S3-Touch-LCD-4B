from __future__ import annotations

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


if __name__ == "__main__":
    unittest.main()
