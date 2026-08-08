from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_repository import validate_checksum_manifests  # noqa: E402


class ChecksumManifestTests(unittest.TestCase):
    def make_manifest(self, directory: Path, name: str, content: bytes) -> None:
        directory.mkdir(parents=True, exist_ok=True)
        (directory / name).write_bytes(content)
        digest = hashlib.sha256(content).hexdigest()
        (directory / "checksums.sha256").write_text(
            f"{digest}  {name}\n", encoding="utf-8"
        )

    def test_valid_manifests(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_manifest(root / "firmware", "factory.bin", b"firmware")
            self.make_manifest(root / "hardware" / "schematics", "board.pdf", b"pdf")
            self.assertEqual(validate_checksum_manifests(root), [])

    def test_manifest_cannot_escape_its_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            firmware = root / "firmware"
            firmware.mkdir(parents=True)
            outside = root / "outside.bin"
            outside.write_bytes(b"outside")
            digest = hashlib.sha256(outside.read_bytes()).hexdigest()
            (firmware / "checksums.sha256").write_text(
                f"{digest}  ../outside.bin\n", encoding="utf-8"
            )
            self.make_manifest(root / "hardware" / "schematics", "board.pdf", b"pdf")

            errors = validate_checksum_manifests(root)

            self.assertTrue(any("checksum path leaves its directory" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
