# LVGL PCF85063 时间示例

[English](README.md) | [简体中文](README_ZH.md)

示例使用 LVGL 在 480 × 480 屏幕上显示 PCF85063 RTC 时间。RTC、显示控制和其他板载
器件共享 GPIO47/48 I2C，总线、RGB 和 TCA9554 定义来自 `Mylibrary/pin_config.h`。

CI 使用 Arduino-ESP32 3.3.11 和随包库编译。RTC 精度、掉电保持和显示行为需实物测试。
