# Scripts

- `check_repository.py` validates repository layout, local Markdown links, and
  public-text hygiene.
- `discover_examples.py` discovers first-party ESP-IDF projects and Arduino
  sketches, filters a manual selector, and emits the GitHub Actions matrix.

The discovery script accepts `all`, an example directory name, or a
repository-relative example path. Arduino examples inside bundled libraries are
excluded from the product matrix.

Firmware packaging is implemented by `releases/package_firmware.py`, while
`releases/download_artifacts.py` retrieves and safely extracts CI packages.
Generated build output, package directories, and downloaded artifacts remain
ignored by Git.
