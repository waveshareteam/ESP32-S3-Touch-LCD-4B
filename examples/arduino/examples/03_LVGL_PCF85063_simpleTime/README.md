# LVGL PCF85063 Time Demo

[English](README.md) | [简体中文](README_ZH.md)

Displays time from the PCF85063 RTC on the 480 × 480 panel with LVGL. The RTC,
display control, and other board devices use the shared I2C bus on GPIO47/48;
RGB and TCA9554 assignments come from `Mylibrary/pin_config.h`.

CI compiles the sketch with Arduino-ESP32 3.3.11 and bundled libraries. RTC
accuracy, retained time, and display behavior require physical-board testing.
