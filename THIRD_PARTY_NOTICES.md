# Third-party Notices

The official Waveshare Demo bundle imported into `examples/` contains bundled
runtime libraries, fonts, media, selected board-relevant datasheets, and
firmware blobs from multiple upstream projects. Those files retain their
original copyright, license, attribution, and notice files. Inclusion in this
repository does not relicense them under the repository-level Apache-2.0
license.

Upstream test suites, documentation build trees, cross-platform development
support, bundled-library examples, and datasheets for devices not present on
this board are intentionally omitted. Use the upstream project links in each
library's metadata or README when those development resources are needed.

Important imported roots include:

- `examples/arduino/libraries/GFX_Library_for_Arduino/`
- `examples/arduino/libraries/lvgl/`
- `examples/arduino/libraries/SensorLib/`
- `examples/arduino/libraries/XPowersLib/`
- local components under `examples/esp-idf/*/components/`
- `firmware/ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin`

Review the license files and source headers within each imported root before
redistribution or modification. The source archive, synchronized Wiki revision,
and cryptographic hashes are recorded in `docs/wiki-resources.md`.
