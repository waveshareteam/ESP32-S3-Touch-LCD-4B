# Waveshare Wiki Resources

[English](wiki-resources.md) | [简体中文](wiki-resources_ZH.md)

This repository imports product-specific resources from the official
[ESP32-S3-Touch-LCD-4B Wiki page](https://www.waveshare.net/wiki/ESP32-S3-Touch-LCD-4B).
The synchronized page revision is
[137986](https://www.waveshare.net/w/index.php?title=ESP32-S3-Touch-LCD-4B&oldid=137986),
retrieved on 2026-07-28.

## Stored Resources

| Resource | Repository path | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Schematic PDF | `hardware/schematics/ESP32-S3-Touch-LCD-4B.pdf` | 2,230,991 | `171d4d3a0041abe183746519dec6f7fa430bb5ae9acea11e02dda10b06014879` |
| Demo source archive | Imported into `examples/` and `firmware/`; archive not committed | 153,244,726 | `a9025815a1e51b81dcdc1936271c5bab528bfc7ea37cd0a790dcb9a81e7e84f` |
| Factory firmware | `firmware/ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin` | 16,732,160 | `06bc042509e018785b977bdb2e796d8ea555d68c9f22ebe1a64d9dad4f713c1f` |
| Product Wiki images | `docs/assets/wiki/` | 13,503,039 total | Original filenames retained |

Official attachment URLs:

- [Schematic PDF](https://www.waveshare.net/w/upload/8/82/ESP32-S3-Touch-LCD-4B.pdf)
- [Demo source archive](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-4B/ESP32-S3-Touch-LCD-4B-Demos.zip)

## Demo Import Map

| Archive path | Repository path | Notes |
| --- | --- | --- |
| `ESP-IDF-v5.4.2/*` | `examples/esp-idf/*` | Five first-party projects; generated `sdkconfig`, `sdkconfig.old`, and `.clangd` files excluded |
| `Arduino-v3.2.0/examples/*` | `examples/arduino/examples/*` | Eight first-party sketches |
| `Arduino-v3.2.0/libraries/*` | `examples/arduino/libraries/*` | Runtime sources and licenses retained; upstream tests, docs, examples, and unrelated datasheets omitted |
| `FirmWare/*.bin` | `firmware/*.bin` | Factory/recovery input, not a source-build CI artifact |

The `07_ES8311` archive example contained an embedded PCM recording with only a
filename/size comment and no source or license metadata. It is not
redistributed; the normalized sketch generates a low-amplitude test tone at
runtime instead. Driver sources and their license headers are retained.

The archive contained 5,756 ZIP entries and 5,116 files after extraction,
with 341,818,010 uncompressed bytes. It had no absolute paths, parent-directory
traversal entries, case-insensitive duplicate paths, or generated `build/`,
`managed_components/`, or `.git/` directories.

## Linked, Not Duplicated

These general or third-party references remain linked to their official Wiki
copies to avoid stale duplicates and unclear redistribution terms:

- [ESP32-S3 datasheet, Chinese](https://www.waveshare.net/w/upload/5/58/Esp32-s3_datasheet_cn.pdf)
- [ESP32-S3 technical reference manual, Chinese](https://www.waveshare.net/w/upload/8/88/Esp32-s3_technical_reference_manual_cn.pdf)
- [ESP32-S3 datasheet, English](https://www.waveshare.net/w/upload/b/bd/Esp32-s3_datasheet_en.pdf)
- [ESP32-S3 technical reference manual, English](https://www.waveshare.net/w/upload/1/11/Esp32-s3_technical_reference_manual_en.pdf)
- [QMI8658C datasheet](https://www.waveshare.net/w/upload/5/5f/QMI8658C.pdf)
- [PCF85063A datasheet](https://www.waveshare.net/w/upload/9/97/PCF85063A.pdf)
- [AXP2101 datasheet](https://www.waveshare.net/w/upload/e/ed/X-power-AXP2101_SWcharge_V1.0.pdf)
- [ES8311 datasheet](https://www.waveshare.net/w/upload/6/65/ES8311.DS.pdf)
- [ES8311 user guide](https://www.waveshare.net/w/upload/5/56/ES8311.user.Guide.pdf)
- [GT911 datasheet, Chinese](https://www.waveshare.net/w/upload/e/eb/GT911.pdf)
- [GT911 datasheet, English](https://www.waveshare.net/w/upload/d/d9/GT911_EN_Datasheet.pdf)
- [ES7210 datasheet](https://www.waveshare.net/w/upload/5/54/ES7210-datasheet.pdf)
- [Font extraction utility](https://www.waveshare.net/w/upload/c/c6/Zimo221.7z)
- [Image2Lcd utility](https://www.waveshare.net/w/upload/b/bd/Image2Lcd2.9.zip)
- [Espressif Flash Download Tool](https://dl.espressif.com/public/flash_download_tool.zip)

Some bundled Arduino libraries contain their own upstream datasheets, tests,
examples, and license files. They are retained as part of the official Demo
bundle, but are not treated as first-party product examples.

## Validation

- The schematic PDF contains two nonblank pages: the electrical schematic and
  a component-placement/board-outline page.
- Downloaded image sizes and SHA-1 values were obtained from the MediaWiki API.
- Active example pin definitions were cross-checked against the schematic and
  managed BSP; see [the pin audit](../hardware/pin-audit.md). Electrical and
  physical-board revision validation is still pending.
