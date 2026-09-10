# LVGL QMI8658 运动界面

[English](README.md) | [简体中文](README_ZH.md)

示例通过板级 I2C 读取 QMI8658 加速度计，并在 LVGL 图表中绘制运动数据。显示、扩展器
和 I2C 引脚集中定义于 `Mylibrary/pin_config.h`；本示例使用 QMI8658 地址 `0x6B`。

CI 使用 Arduino-ESP32 3.3.11 编译。传感器方向、校准、采样和显示行为仍需实物验证。
