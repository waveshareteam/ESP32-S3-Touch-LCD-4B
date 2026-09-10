# LVGL QMI8658 Motion UI

[English](README.md) | [简体中文](README_ZH.md)

Reads the QMI8658 accelerometer over the board I2C bus and plots motion data in
an LVGL chart. Display, expander, and I2C pins are centralized in
`Mylibrary/pin_config.h`; QMI8658 uses address `0x6B` in this example.

CI compiles the sketch with Arduino-ESP32 3.3.11. Sensor orientation,
calibration, sampling, and display behavior require physical-board validation.
