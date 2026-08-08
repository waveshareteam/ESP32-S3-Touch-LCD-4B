# LVGL AXP2101 ADC 数据

[English](README.md) | [简体中文](README_ZH.md)

示例通过 GPIO47/48 共享 I2C 读取 AXP2101 电源和 ADC 信息，并用 LVGL 显示。草图使用
随包 XPowersLib，以及 `Mylibrary/pin_config.h` 中统一的 RGB/TCA9554 定义。

CI 使用 Arduino-ESP32 3.3.11 编译。电压、电流和电池行为必须在实物上核验后使用。
