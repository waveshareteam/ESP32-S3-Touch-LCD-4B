# Schematic-backed Pin Audit

[English](pin-audit.md) | [简体中文](pin-audit_ZH.md)

## Scope and Evidence

This audit covers the pin definitions actively used by the first-party examples.
The primary source is page 1 of the official two-page
[schematic PDF](schematics/ESP32-S3-Touch-LCD-4B.pdf). Values were compared with
the Arduino board header and sketches in `examples/arduino/`, the ESP-IDF
projects in `examples/esp-idf/`, and version 2.0.0 of the official
[`waveshare/esp32_s3_touch_lcd_4b`](https://components.espressif.com/components/waveshare/esp32_s3_touch_lcd_4b)
managed BSP.

The attachment filename does not identify a PCB revision, and editable
schematic/PCB/netlist sources are not published in this repository. Therefore
this is a source cross-check for the published PDF, not a revision-qualified
electrical sign-off or physical-board validation.

## Verified Active Assignments

### Shared I2C and control expander

| Signal | Assignment | Cross-check |
| --- | --- | --- |
| Shared I2C SDA / SCL | GPIO47 / GPIO48 | Schematic, ESP-IDF defaults, BSP, all Arduino sketches |
| TCA9554 address | `0x20` | Address pins grounded in schematic; BSP and sketches agree |
| TCA9554 EXIO0 | LCD chip select | Schematic, BSP, Arduino header |
| TCA9554 EXIO1 | LCD serial data | Schematic, BSP, Arduino header |
| TCA9554 EXIO2 | LCD serial clock | Schematic, BSP, Arduino header |
| TCA9554 EXIO3 | Audio amplifier control | Schematic, BSP, audio sketches |
| TCA9554 EXIO5 | GT911 reset | Schematic, BSP, display/touch sketches |
| TCA9554 EXIO6 | GT911 interrupt | Schematic, BSP, display/touch sketches |
| TCA9554 EXIO7 | LCD reset | Schematic, BSP, Arduino header |

The AXP2101 example uses address `0x34`; the QMI8658 examples/BSP use `0x6B`.
GT911 reset and interrupt are routed through the TCA9554 rather than directly to
ESP32-S3 GPIOs.

### RGB display

| Function | GPIO assignments |
| --- | --- |
| DE / VSYNC / HSYNC / PCLK | 17 / 3 / 46 / 9 |
| R0..R4 | 10, 11, 12, 13, 14 |
| G0..G5 | 21, 8, 18, 45, 38, 39 |
| B0..B4 | 40, 41, 42, 2, 1 |
| Backlight | GPIO4 |
| Geometry | 480 × 480 |

The imported sketches already passed these values to `Arduino_ESP32RGBPanel`
in the correct constructor order, but their inline R/B labels were reversed.
The values and correct color names are now centralized in
`examples/arduino/libraries/Mylibrary/pin_config.h`.

### Audio and other active pins

| Signal | GPIO | Use |
| --- | ---: | --- |
| I2S MCLK | 5 | ES8311 / ES7210 |
| I2S BCLK | 16 | ES8311 / ES7210 |
| I2S LRCK | 7 | ES8311 / ES7210 |
| ESP32 to ES8311 data | 6 | Speaker/output path |
| ES7210 to ESP32 data | 15 | Microphone/input path |
| Calibration button | 0 | `04_Immersive_block` |

The QMI8658, PCF85063, AXP2101, GT911, ES8311, and ES7210 share the board I2C
pins where applicable. The schematic and examples agree on the active I2S pins
and TCA9554 amplifier enable.

## Repository Changes From This Audit

- Centralized board I2C, RGB, TCA9554, display geometry, backlight, and audio
  assignments in the first-party Arduino board header.
- Replaced duplicated numeric pins in all eight first-party sketches.
- Corrected the R/B comments by naming the constructor inputs from the
  schematic instead of changing the already-correct electrical values.
- Kept generated `managed_components/` trees ignored; the product projects use
  the official Component Registry BSP rather than committing dependency caches.

## Open Verification Items

- Identify and record the PCB marking and hardware revision corresponding to
  the published PDF.
- Compare against editable schematic/PCB/netlist and BOM sources if released.
- Verify flash/PSRAM electrical mode, USB routing, power limits, connector pins,
  AXP2101 interrupt routing, and any storage interface from revisioned sources.
- Perform display, touch, audio, sensor, RTC/PMU, USB, battery, and expansion
  tests on the named physical revision.

Until those items are complete, CI success is only compile, dependency
resolution, packaging, and artifact evidence.
