# LVGL v9 Arduino Demo

[English](README.md) | [简体中文](README_ZH.md)

Initializes the ST7701 RGB display and GT911 touch controller, then runs the
LVGL v9 Arduino demo. Touch reset/interrupt are routed through the TCA9554;
board assignments are centralized in `Mylibrary/pin_config.h` and documented in
the [pin audit](../../../../hardware/pin-audit.md).

CI compiles the sketch with Arduino-ESP32 3.3.11. Touch coordinates, timing,
memory behavior, and visual output require physical-board validation.
