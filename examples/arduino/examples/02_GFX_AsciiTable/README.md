# Arduino GFX ASCII Table

[English](README.md) | [简体中文](README_ZH.md)

Initializes the board display and renders an ASCII character table with Arduino
GFX. RGB, I2C, and TCA9554 assignments are shared through
`Mylibrary/pin_config.h` and documented in the
[pin audit](../../../../hardware/pin-audit.md).

CI compiles this sketch with Arduino-ESP32 3.3.11 and the repository's fixed
ESP32-S3 board options; runtime display output still requires hardware testing.
