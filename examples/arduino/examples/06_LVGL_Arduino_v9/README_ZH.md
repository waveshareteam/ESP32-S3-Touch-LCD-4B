# LVGL v9 Arduino 示例

[English](README.md) | [简体中文](README_ZH.md)

示例初始化 ST7701 RGB 显示和 GT911 触摸，并运行 LVGL v9 Arduino Demo。触摸复位与
中断通过 TCA9554 转接；板级分配集中在 `Mylibrary/pin_config.h`，详见
[引脚审计](../../../../hardware/pin-audit_ZH.md)。

CI 使用 Arduino-ESP32 3.3.11 编译。触摸坐标、时序、内存行为和画面仍需实物验证。
