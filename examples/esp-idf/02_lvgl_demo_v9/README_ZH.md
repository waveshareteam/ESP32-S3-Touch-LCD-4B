# LVGL v9 显示与触摸示例

[English](README.md) | [简体中文](README_ZH.md)

本 ESP32-S3 工程通过官方 Waveshare 板级组件驱动 480 × 480 ST7701 RGB 显示和 GT911
触摸。`main/idf_component.yml` 固定 `waveshare/esp32_s3_touch_lcd_4b` 2.0.0 与
LVGL 9.5.0。

将目标设为 `esp32s3` 后使用标准 ESP-IDF 构建/烧录流程。CI 使用 ESP-IDF v5.5.5 和
v6.0.2 编译并打包成功输出，但编译结果不能代替指定硬件修订上的显示触摸实测；参见
[引脚审计](../../../hardware/pin-audit_ZH.md)。
