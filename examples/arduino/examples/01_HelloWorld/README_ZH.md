# 显示 Hello World

[English](README.md) | [简体中文](README_ZH.md)

示例通过 Arduino GFX 和 TCA9554 控制扩展器初始化 ST7701 480 × 480 RGB 屏幕，随后
绘制不断变化的 `Hello World!`。板级引脚来自共享 `Mylibrary/pin_config.h`，并与
[引脚审计](../../../../hardware/pin-audit_ZH.md)一致。

CI 使用 Arduino-ESP32 3.3.11、16 MB Flash、OPI PSRAM 和随包库编译；编译通过不证明
实物显示行为。
