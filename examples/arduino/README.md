# Arduino Examples

[English](README.md) | [简体中文](README_ZH.md)

These resources were imported from the official Waveshare Demo archive linked
in `docs/wiki-resources.md`. The archive baseline is Arduino-ESP32 3.2.0.

## First-party Sketches

- `examples/01_HelloWorld`
- `examples/02_GFX_AsciiTable`
- `examples/03_LVGL_PCF85063_simpleTime`
- `examples/04_LVGL_QMI8658_ui`
- `examples/05_LVGL_AXP2101_ADC_Data`
- `examples/06_LVGL_Arduino_v9`
- `examples/07_ES8311`
- `examples/08_ES7210`

## Bundled Libraries

The `libraries/` directory retains the versions of Arduino GFX, LVGL, the board
helper library, SensorLib, and XPowersLib required by the product sketches. The
first-party board header centralizes the schematic-backed I2C, RGB, TCA9554,
display, and audio assignments used by all sketches.
Licenses, notices, runtime sources, and datasheets for devices used by this
board are preserved.

Upstream test suites, documentation toolchains, cross-platform support files,
bundled-library examples, and unrelated device datasheets are omitted from this
product repository. Retrieve those development resources from the upstream
project linked by each library's `library.properties` or README.

## CI Configuration

CI currently compiles the eight first-party sketches with Arduino-ESP32 3.3.11
and the bundled libraries. The configured board options are:

```text
esp32:esp32:esp32s3:USBMode=hwcdc,CDCOnBoot=cdc,FlashSize=16M,PartitionScheme=app3M_fat9M_16MB,PSRAM=opi
```

The [Build Examples workflow](../../.github/workflows/examples.yml) accepts
`all`, a sketch name, or a repository-relative sketch path when dispatched
manually. See [CI Coverage](../../docs/ci.md) for the exact Arduino CLI command,
bundled-library include paths, and artifact format.

These options support compile validation. The active pin definitions were
cross-checked against the schematic and managed BSP, but a successful build
does not prove runtime behavior on a named physical-board revision.
