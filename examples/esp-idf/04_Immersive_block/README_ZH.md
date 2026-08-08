# 沉浸式方块示例

[English](README.md) | [简体中文](README_ZH.md)

本 ESP32-S3 示例使用 QMI8658 加速度计和 LVGL，让彩色图形随板卡倾斜移动。启动时
保持板卡水平以完成传感器校准，BOOT（GPIO0）可请求重新校准。

工程要求 ESP-IDF `>=5.5.0`，并固定 Waveshare BSP 2.0.0、QMI8658 2.0.0 和
LVGL 9.5.0。CI 使用 ESP-IDF v5.5.5 与 v6.0.2 编译。激活兼容环境后将目标设为
`esp32s3`，再使用标准 `idf.py` 构建/烧录命令。校准、显示和传感器运行行为仍需实物
验证。

主要文件：`main/main.c` 包含显示、校准、QMI8658 输入和图形移动逻辑；
`main/idf_component.yml` 固定组件版本；`sdkconfig.defaults` 保存工程默认配置。
