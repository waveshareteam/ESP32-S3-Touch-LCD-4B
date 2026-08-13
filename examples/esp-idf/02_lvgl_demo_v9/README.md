# LVGL v9 Display and Touch Demo

[English](README.md) | [简体中文](README_ZH.md)

This ESP32-S3 project exercises the 480 × 480 ST7701 RGB display and GT911
touch controller through the official Waveshare board-support component. It
pins `waveshare/esp32_s3_touch_lcd_4b` 2.0.0 and LVGL 9.5.0 in
`main/idf_component.yml`.

These pins preserve the currently tested Waveshare board/display/touch and
LVGL 9 API contract. Revisit the version set only after candidate versions
build with ESP-IDF v5.5.5 and v6.0.2 and the schematic-backed configuration is
rechecked; physical-board validation remains separate.

Set the target to `esp32s3` and use the standard ESP-IDF build/flash workflow.
CI compiles the project with ESP-IDF v5.5.5 and v6.0.2 and packages successful
outputs. The compile result does not replace display/touch testing on a named
hardware revision; see the [pin audit](../../../hardware/pin-audit.md).
