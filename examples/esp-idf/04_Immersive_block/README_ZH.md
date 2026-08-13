# 沉浸式方块示例

[English](README.md) | [简体中文](README_ZH.md)

本 ESP32-S3 示例使用 QMI8658 加速度计和 LVGL，让彩色图形随板卡倾斜移动。启动时
保持板卡水平以完成传感器校准，BOOT（GPIO0）可请求重新校准。

工程要求 ESP-IDF `>=5.5.0`，并固定 Waveshare BSP 2.0.0、QMI8658 2.0.0 和
LVGL 9.5.0。CI 使用 ESP-IDF v5.5.5 与 v6.0.2 编译。激活兼容环境后将目标设为
`esp32s3`，再使用标准 `idf.py` 构建/烧录命令。校准、显示和传感器运行行为仍需实物
验证。

这些版本固定用于保留当前已测试的 Waveshare 板卡、QMI8658 传感器和 LVGL 9 显示
API 契约。仅当候选版本能在 ESP-IDF v5.5.5 和 v6.0.2 上构建，且已重新核对原理图
支持的配置时，才重新评估版本组合；实物验证仍是独立步骤。

主要文件：`main/main.c` 包含显示、校准、QMI8658 输入和图形移动逻辑；
`main/idf_component.yml` 固定组件版本；`sdkconfig.defaults` 保存工程默认配置。
