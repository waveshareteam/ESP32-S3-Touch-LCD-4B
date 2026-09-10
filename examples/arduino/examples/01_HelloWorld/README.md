# Display Hello World

[English](README.md) | [简体中文](README_ZH.md)

Initializes the ST7701 480 × 480 RGB panel through Arduino GFX and the TCA9554
control expander, then draws changing `Hello World!` text. Board pins come from
the shared `Mylibrary/pin_config.h` and match the schematic-backed
[pin audit](../../../../hardware/pin-audit.md).

CI compiles this sketch with Arduino-ESP32 3.3.11, 16 MB flash, OPI PSRAM, and
the bundled libraries. Compile success does not prove physical display behavior.
