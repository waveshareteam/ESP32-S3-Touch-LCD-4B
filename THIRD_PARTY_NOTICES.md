# Third-party Notices

[English](THIRD_PARTY_NOTICES.md) | [简体中文](THIRD_PARTY_NOTICES_ZH.md)

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

| Imported content | Recorded version/source | License evidence in tree |
| --- | --- | --- |
| Arduino GFX | 1.6.0, upstream URL in `library.properties` | BSD license file |
| LVGL | 9.3.0 archive baseline | MIT `LICENCE.txt` plus licenses for enabled bundled codecs/libraries |
| SensorLib | 0.3.1, Lewis He | MIT `LICENSE` and package metadata |
| XPowersLib | 0.3.0, Lewis He | MIT `LICENSE` and package metadata |
| ES8311 driver in `07_ES8311` | Espressif source headers | Apache-2.0 SPDX headers |
| ES7210/audio HAL in `08_ES7210` | Espressif source headers | MIT notice in each source/header |
| Local ESP-IDF `bsp_extra` components | Product demo glue | Apache-2.0 `LICENSE` files |

The ES8311 sketch generates its test tone at runtime; the imported PCM recording
with no source or license metadata is intentionally not redistributed. Managed
components downloaded during ESP-IDF builds are not vendored here; consult each
package's Component Registry metadata and artifact dependency lock before
redistributing a built package.

Review the license files and source headers within each imported root before
redistribution or modification. The source archive, synchronized Wiki revision,
and cryptographic hashes are recorded in `docs/wiki-resources.md`.
