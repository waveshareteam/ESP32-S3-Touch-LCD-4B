# ESP32-S3-Touch-LCD-4B Hardware Reference Template

[English](HARDWARE_REFERENCE_TEMPLATE.md) | [简体中文](HARDWARE_REFERENCE_TEMPLATE_ZH.md)

> Status: unverified template. Do not use this file as a pin map or product
> specification until every field is completed from released hardware files.

## Revision Evidence

| Field | Value | Source |
| --- | --- | --- |
| Product name | ESP32-S3-Touch-LCD-4B | Repository name |
| PCB marking | TODO | TODO |
| Hardware revision | TODO | TODO |
| Schematic filename and revision | TODO | TODO |
| PCB filename and revision | TODO | TODO |
| BOM filename and revision | TODO | TODO |

## Core Hardware

| Item | Value | Source |
| --- | --- | --- |
| SoC | ESP32-S3 family; exact part TODO | TODO |
| Flash | TODO | TODO |
| PSRAM | TODO | TODO |
| USB interfaces | TODO | TODO |
| Power input and limits | TODO | TODO |

## Display

Record the LCD controller, resolution, interface, color format, clocks and
timing, reset, chip-select, command/data, backlight, and all data pins.

| Signal or property | Value | Source |
| --- | --- | --- |
| Controller | TODO | TODO |
| Resolution | TODO | TODO |
| Interface | TODO | TODO |
| Pin and timing table | TODO | TODO |

## Touch

Record the controller, bus, address, clock/data pins, interrupt, reset, and any
signals shared with the display or other peripherals.

| Signal or property | Value | Source |
| --- | --- | --- |
| Controller | TODO | TODO |
| Interface and address | TODO | TODO |
| Pin table | TODO | TODO |

## Remaining Peripherals

Add evidence-backed tables for storage, audio, sensors, RTC/PMU, buttons, LEDs,
expansion connectors, and shared-bus constraints that exist on the board.

## Verification

- [ ] Schematic and PCB/netlist agree.
- [ ] BOM population options are documented.
- [ ] BSP and managed component defaults agree.
- [ ] ESP-IDF configuration and examples agree.
- [ ] Arduino board options and pin headers agree, if Arduino is supported.
- [ ] Physical testing is complete on the named hardware revision.
