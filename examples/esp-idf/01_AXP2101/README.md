# AXP2101 Power-management Example

[English](README.md) | [简体中文](README_ZH.md)

This ESP32-S3 project initializes the board's AXP2101 PMIC over I2C and reports
rail enable/voltage state once per second. The board defaults are SDA GPIO47,
SCL GPIO48, device address `0x34`, and no direct PMU interrupt pin.

## Dependencies and Configuration

The project retains XPowersLib as a bundled upstream component under
`components/XPowersLib`; its upstream source is
[lewisxhe/XPowersLib](https://github.com/lewisxhe/XPowersLib). Select the PMU and
I2C values under `XPowers Configuration` when adapting the example to another
board. A negative interrupt value means the optional IRQ path is disabled.

## Build and Validation

After activating ESP-IDF, set the target to `esp32s3` and build or flash with
the standard `idf.py` commands. Repository CI compiles this project with ESP-IDF
v5.5.5 and v6.0.2 and packages each successful result. The I2C setup now returns
bus/device registration errors to `app_main`; CI does not prove PMIC electrical
behavior on a physical board.

Expected serial output begins with `I2C initialized successfully` and
`Init PMU SUCCESS!`, followed by the rail status table.
