# Scripts

[English](README.md) | [简体中文](README_ZH.md)

- `check_repository.py` validates repository layout, local Markdown links, and
  public-text hygiene.
- `discover_examples.py` discovers first-party ESP-IDF projects and Arduino
  sketches, filters a manual selector, and emits the GitHub Actions matrix.
- `route_examples.py` classifies a Git diff and emits the smallest safe ESP-IDF
  and Arduino matrices; unknown source paths fall back to both full matrices.

`config/markdown-audit.json` is the repository policy consumed by the reusable
Waveshare Markdown audit. `check_repository.py` also reads its exclusions when
enforcing bilingual companions, so compatibility paths and CI policy cannot
drift independently.

The discovery script accepts `all`, an example directory name, or a
repository-relative example path. Arduino examples inside bundled libraries are
excluded from the product matrix.

Firmware packaging is implemented by `releases/package_firmware.py`, while
`releases/download_artifacts.py` retrieves and safely extracts CI packages.
Generated build output, package directories, and downloaded artifacts remain
ignored by Git.
