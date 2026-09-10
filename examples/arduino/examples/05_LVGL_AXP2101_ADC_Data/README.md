# LVGL AXP2101 ADC Data

[English](README.md) | [简体中文](README_ZH.md)

Reads AXP2101 power and ADC information over the shared GPIO47/48 I2C bus and
renders it with LVGL. The sketch uses the bundled XPowersLib and the common
RGB/TCA9554 definitions in `Mylibrary/pin_config.h`.

CI compiles the sketch with Arduino-ESP32 3.3.11. Reported voltage/current
values and battery behavior must be checked on physical hardware before use.
