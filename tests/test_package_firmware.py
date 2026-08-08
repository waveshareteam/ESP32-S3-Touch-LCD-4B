from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "releases"))

from package_firmware import copy_dependency_lock  # noqa: E402


class DependencySnapshotTests(unittest.TestCase):
    def test_dependency_lock_is_copied_with_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            package = root / "package"
            project.mkdir()
            package.mkdir()
            content = b'dependencies:\n  lvgl/lvgl:\n    version: "9.5.0"\n'
            (project / "dependencies.lock").write_bytes(content)

            metadata = copy_dependency_lock(project, package)

            self.assertEqual((package / "dependencies.lock").read_bytes(), content)
            self.assertEqual(
                metadata,
                {
                    "file": "dependencies.lock",
                    "sha256": hashlib.sha256(content).hexdigest(),
                },
            )

    def test_missing_dependency_lock_is_explicitly_absent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "project"
            package = root / "package"
            project.mkdir()
            package.mkdir()
            self.assertIsNone(copy_dependency_lock(project, package))


if __name__ == "__main__":
    unittest.main()
