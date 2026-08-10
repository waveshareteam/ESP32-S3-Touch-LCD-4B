from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_repository import validate_checksum_manifests, validate_homepage_policy  # noqa: E402


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


class HomepagePolicyTests(unittest.TestCase):
    H2_ICONS = ["✨", "🖥️", "📦", "🧪", "🗂️", "📚", "🤝", "📄"]

    def policy(self) -> dict:
        return {
            "homepage_pairs": [
                {
                    "english": "README.md",
                    "chinese": "README_ZH.md",
                    "profile": "single-product",
                    "required_components": [
                        "centered_header",
                        "html_h1",
                        "subtitle",
                        "badges",
                        "language_switch",
                        "quick_links",
                        "hero_image",
                        "separator",
                        "h2",
                    ],
                    "required_quick_links": ["product", "esp_idf", "arduino", "firmware", "documentation"],
                    "required_badges": ["build", "license"],
                    "required_h2_icons": self.H2_ICONS,
                }
            ]
        }

    def homepage(self, title: str, alt: str, hero: str = "docs/assets/hero.jpg") -> str:
        quick_links = "\n".join(
            (
                '  <a href="https://example.com/product">🌐 Product</a>',
                '  <a href="examples/esp-idf/">🧩 ESP-IDF</a>',
                '  <a href="examples/arduino/">🔧 Arduino</a>',
                '  <a href="firmware/">📦 Firmware</a>',
                '  <a href="docs/">📚 Documentation</a>',
            )
        )
        sections = "\n".join(f"## {icon} Section" for icon in self.H2_ICONS)
        return f'''<div align="center">
<h1>{title}</h1>
<strong>Localized subtitle</strong>
<p><a href="README.md">English</a> | <a href="README_ZH.md">简体中文</a></p>
<p><img src="https://example.com/actions/workflows/check.yml/badge.svg" alt="Build"></p>
<p><img src="https://img.shields.io/github/license/example/product" alt="License"></p>
<p>
{quick_links}
</p>
<a href="https://example.com/product"><img src="{hero}" width="800" alt="{alt}"></a>
</div>

---

{sections}
'''

    def write_contract(self, root: Path) -> None:
        hero = root / "docs" / "assets" / "hero.jpg"
        hero.parent.mkdir(parents=True)
        hero.write_bytes(b"hero")
        (root / "README.md").write_text(self.homepage("Product", "Product display"), encoding="utf-8")
        (root / "README_ZH.md").write_text(self.homepage("产品", "产品显示屏"), encoding="utf-8")

    def test_valid_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            self.assertEqual(validate_homepage_policy(root, self.policy()), [])

    def test_missing_hero_image_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            readme = root / "README.md"
            readme.write_text(
                readme.read_text(encoding="utf-8").replace(
                    '<a href="https://example.com/product"><img src="docs/assets/hero.jpg" width="800" alt="Product display"></a>',
                    "",
                ),
                encoding="utf-8",
            )
            errors = validate_homepage_policy(root, self.policy())
            self.assertTrue(any("missing local hero image" in item for item in errors))

    def test_missing_local_hero_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            (root / "README.md").write_text(self.homepage("Product", "Product display", "docs/assets/missing.jpg"), encoding="utf-8")
            errors = validate_homepage_policy(root, self.policy())
            self.assertTrue(any("missing hero image" in item for item in errors))

    def test_hero_image_cannot_leave_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            (root / "README.md").write_text(self.homepage("Product", "Product display", "../hero.jpg"), encoding="utf-8")
            errors = validate_homepage_policy(root, self.policy())
            self.assertTrue(any("hero image leaves repository" in item for item in errors))

    def test_missing_product_quick_link_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            readme = root / "README.md"
            readme.write_text(readme.read_text(encoding="utf-8").replace("🌐 Product", "Product"), encoding="utf-8")
            errors = validate_homepage_policy(root, self.policy())
            self.assertTrue(any("missing product quick link" in item for item in errors))

    def test_h2_sequence_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            readme = root / "README.md"
            readme.write_text(readme.read_text(encoding="utf-8").replace("## 🖥️ Section", "## 🔧 Section"), encoding="utf-8")
            errors = validate_homepage_policy(root, self.policy())
            self.assertTrue(any("H2 icon sequence" in item for item in errors))

    def test_malformed_policy_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            malformed = self.policy()
            malformed["homepage_pairs"] = {"english": "README.md"}
            errors = validate_homepage_policy(root, malformed)
            self.assertEqual(errors, ["config/markdown-audit.json: homepage_pairs must be a list"])

    def test_homepage_path_cannot_leave_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            policy = self.policy()
            policy["homepage_pairs"][0]["english"] = "../outside.md"
            errors = validate_homepage_policy(root, policy)
            self.assertTrue(any("english leaves repository" in item for item in errors))

    def test_single_product_policy_cannot_omit_hero_or_product(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_contract(root)
            for key, value, expected in (
                ("required_components", "hero_image", "single-product requirement(s): hero_image"),
                ("required_quick_links", "product", "single-product requirement: product"),
            ):
                with self.subTest(key=key):
                    policy = self.policy()
                    policy["homepage_pairs"][0][key].remove(value)
                    errors = validate_homepage_policy(root, policy)
                    self.assertTrue(any(expected in item for item in errors))


if __name__ == "__main__":
    unittest.main()
