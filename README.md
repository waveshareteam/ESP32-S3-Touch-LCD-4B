<div align="center">

# ESP32-S3-Touch-LCD-4B

### ESP32-S3 4-inch 480 × 480 RGB LCD touch development board

[![Build Examples](https://github.com/waveshareteam/ESP32-S3-Touch-LCD-4B/actions/workflows/examples.yml/badge.svg)](https://github.com/waveshareteam/ESP32-S3-Touch-LCD-4B/actions/workflows/examples.yml)
[![Repository Checks](https://github.com/waveshareteam/ESP32-S3-Touch-LCD-4B/actions/workflows/repository-checks.yml/badge.svg)](https://github.com/waveshareteam/ESP32-S3-Touch-LCD-4B/actions/workflows/repository-checks.yml)
[![License](https://img.shields.io/github/license/waveshareteam/ESP32-S3-Touch-LCD-4B)](LICENSE.txt)

[English](README.md) | [简体中文](README_CN.md)

[Product Page](https://www.waveshare.com/esp32-s3-touch-lcd-4b.htm) ·
[Waveshare Wiki](https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-4B) ·
[CI Firmware Artifacts](https://github.com/waveshareteam/ESP32-S3-Touch-LCD-4B/actions/workflows/examples.yml) ·
[ESP-IDF Examples](examples/esp-idf/) ·
[Arduino Examples](examples/arduino/) ·
[Documentation](docs/)

![ESP32-S3-Touch-LCD-4B](docs/assets/wiki/ESP32-S3-Touch-LCD-4B-inter001.jpg)

</div>

## Overview

ESP32-S3-Touch-LCD-4B is a Waveshare smart control panel development board
built around the ESP32-S3-WROOM-1-N16R8 module. It combines a 4-inch
480 × 480 RGB LCD, 5-point capacitive touch, audio input and output, motion
sensing, RTC, battery power management, and expansion interfaces in an
86-box form factor.

This repository provides the official schematic and factory firmware,
normalized ESP-IDF and Arduino examples, reproducible CI builds, and
per-example flashable firmware artifacts.

Product resources were synchronized from the official
[Waveshare Wiki](https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-4B).
The [resource manifest](docs/wiki-resources.md) records source URLs, import
mapping, file sizes, checksums, and redistribution notes.

## Hardware Overview

| Feature | Specification |
| --- | --- |
| Processor module | ESP32-S3-WROOM-1-N16R8, dual-core Xtensa LX7 up to 240 MHz |
| Memory | 16 MB Flash and 8 MB PSRAM |
| Wireless | 2.4 GHz Wi-Fi and Bluetooth 5 (LE) |
| Display | 4-inch IPS LCD, 480 × 480, 65K colors, ST7701 controller, RGB interface |
| Touch | GT911 capacitive touch controller, I2C interface, 5-point touch |
| Power | AXP2101 PMIC, USB-C power, and 3.7 V lithium battery header with charging support |
| Audio | ES7210 audio ADC, ES8311 codec, onboard microphones, and 8 Ω / 2 W speaker header |
| Motion and timekeeping | QMI8658 6-axis IMU and PCF85063 RTC |
| Expansion | TCA9554PWR GPIO expander, USB, UART, and 2.0 mm GPIO header |
| Board support | ESP-IDF managed component `waveshare/esp32_s3_touch_lcd_4b` |
| Hardware files | [Schematic and hardware notes](hardware/) |

The public schematic and example code are included, but a complete
pin-by-pin audit against every hardware revision is still in progress.
Treat passing builds as compile and packaging validation, not proof of
operation on physical hardware.

## CI Firmware Artifacts

The [Build Examples](https://github.com/waveshareteam/ESP32-S3-Touch-LCD-4B/actions/workflows/examples.yml)
workflow builds every first-party example independently. Each successful job
uploads a flashable ZIP containing a manifest, split binaries, a combined
binary, and platform flash scripts.

To use an artifact:

1. Open a successful **Build Examples** workflow run and download the
   `firmware-*` artifact for the framework, example, and toolchain version
   you need.
2. Extract the ZIP and install
   [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32/installation.html).
3. Run `flash.bat COMx` on Windows or `./flash.sh /dev/ttyACM0` on Linux.

Maintainers can download and extract every matching package from a run with:

```bash
python3 releases/download_artifacts.py --run-id <run-id> --clean
```

Omit `--run-id` to select the latest successful run for the current branch.

The combined image is flashed at offset `0x0`. See
[Firmware Packaging and Flashing](releases/README.md) for the artifact layout
and manual flashing commands.

The official factory image is maintained separately under
[firmware/](firmware/). Verify it with
[firmware/checksums.sha256](firmware/checksums.sha256) and read the
[factory firmware notes](firmware/README.md) before flashing. It is not a
source-built CI artifact.

## Examples

### ESP-IDF

| Project | Description |
| --- | --- |
| [01_AXP2101](examples/esp-idf/01_AXP2101/) | AXP2101 power-management example |
| [02_lvgl_demo_v9](examples/esp-idf/02_lvgl_demo_v9/) | LVGL v9 display and touch demo |
| [03_esp-brookesia](examples/esp-idf/03_esp-brookesia/) | ESP-Brookesia application demo |
| [04_Immersive_block](examples/esp-idf/04_Immersive_block/) | QMI8658 motion-controlled immersive block demo |
| [05_Spec_Analyzer](examples/esp-idf/05_Spec_Analyzer/) | Microphone FFT spectrum analyzer |

### Arduino

| Sketch | Description |
| --- | --- |
| [01_HelloWorld](examples/arduino/examples/01_HelloWorld/) | Display hello-world example |
| [02_GFX_AsciiTable](examples/arduino/examples/02_GFX_AsciiTable/) | Arduino GFX ASCII table |
| [03_LVGL_PCF85063_simpleTime](examples/arduino/examples/03_LVGL_PCF85063_simpleTime/) | LVGL and PCF85063 RTC example |
| [04_LVGL_QMI8658_ui](examples/arduino/examples/04_LVGL_QMI8658_ui/) | LVGL and QMI8658 motion UI |
| [05_LVGL_AXP2101_ADC_Data](examples/arduino/examples/05_LVGL_AXP2101_ADC_Data/) | LVGL display of AXP2101 ADC data |
| [06_LVGL_Arduino_v9](examples/arduino/examples/06_LVGL_Arduino_v9/) | LVGL v9 Arduino demo |
| [07_ES8311](examples/arduino/examples/07_ES8311/) | ES8311 audio codec example |
| [08_ES7210](examples/arduino/examples/08_ES7210/) | ES7210 audio ADC example |

The imported archive baselines are ESP-IDF v5.4.2 and Arduino-ESP32 3.2.0.
CI additionally validates the normalized projects with current repository
toolchains:

| Framework | Toolchain | First-party examples | CI jobs |
| --- | --- | ---: | ---: |
| ESP-IDF | v5.5.5 | 5 | 5 |
| ESP-IDF | v6.0.2 | 5 | 5 |
| Arduino-ESP32 | 3.3.11 | 8 | 8 |

A full run expands into 2 discovery jobs and 18 independent firmware build
jobs. Bundled Arduino library examples are intentionally excluded. See
[CI Coverage](docs/ci.md) for discovery rules, target configuration, and
artifact details.

## Repository Layout

| Path | Purpose |
| --- | --- |
| [examples/esp-idf/](examples/esp-idf/) | ESP-IDF projects |
| [examples/arduino/](examples/arduino/) | Arduino sketches and bundled libraries |
| [firmware/](firmware/) | Official factory and recovery binaries |
| [releases/](releases/) | Source-built firmware packaging tools and documentation |
| [hardware/](hardware/) | Schematic and hardware reference material |
| [docs/](docs/) | CI, resource provenance, bring-up, and maintainer documentation |
| [scripts/](scripts/) | Example discovery and repository maintenance tools |

See [Repository Structure](docs/repository-structure.md) for directory
ownership and naming rules.

## Documentation

- [Waveshare Wiki](https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-4B)
- [Wiki Resource Manifest](docs/wiki-resources.md)
- [Hardware Resources](hardware/README.md)
- [Bring-up Checklist](docs/bring-up-checklist.md)
- [CI Coverage](docs/ci.md)
- [Firmware Packaging and Flashing](releases/README.md)
- [Repository Structure](docs/repository-structure.md)

The original Demo ZIP is not committed because its normalized contents are
already stored under `examples/` and `firmware/`.

## Contributing and Support

- Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a change.
- Use [SUPPORT.md](SUPPORT.md) to choose the correct support channel.
- Report security issues according to [SECURITY.md](SECURITY.md).

## License

Unless a file states otherwise, this repository is licensed under the
[Apache License 2.0](LICENSE.txt). Imported components, examples, documents,
and images retain their original terms; see
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
