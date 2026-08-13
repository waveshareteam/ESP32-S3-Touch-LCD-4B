# AXP2101 Power-management Example

[English](README.md) | [简体中文](README_ZH.md)

This ESP32-S3 project initializes the board's AXP2101 PMIC over I2C and reports
rail enable/voltage state once per second. The board defaults are SDA GPIO47,
SCL GPIO48, device address `0x34`, and no direct PMU interrupt pin.

## Dependencies and Configuration

The project retains a trimmed bundled copy of XPowersLib under
`components/XPowersLib`; its exact imported upstream revision is not recorded,
and its retained MIT license is at `components/XPowersLib/LICENSE`. No
semantically and hardware-equivalent managed component has been verified, so it
remains local. Revisit only after a candidate preserves the AXP2101 callback,
IRQ, and charger APIs and this board's I2C GPIO47/GPIO48/address `0x34`
configuration on ESP-IDF v5.5.5 and v6.0.2. Select the PMU and I2C values under
`XPowers Configuration` when adapting the example to another board. A negative
interrupt value means the optional IRQ path is disabled.

## Build and Validation

After activating ESP-IDF, set the target to `esp32s3` and build or flash with
the standard `idf.py` commands. Repository CI compiles this project with ESP-IDF
v5.5.5 and v6.0.2 and packages each successful result. The I2C setup now returns
bus/device registration errors to `app_main`; CI does not prove PMIC electrical
behavior on a physical board.

Expected serial output begins with `I2C initialized successfully` and
`Init PMU SUCCESS!`, followed by the rail status table.
