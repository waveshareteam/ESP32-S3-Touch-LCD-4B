# ESP-Brookesia 应用示例

[English](README.md) | [简体中文](README_ZH.md)

本工程运行 ESP-Brookesia LVGL 应用外壳，并包含计算器、绘图和音乐播放器。
`components/apps` 是第一方示例功能，`components/bsp_extra` 是产品专属板卡/音频胶水；
生成的 `managed_components/` 不提交。

清单固定 ESP-Brookesia 0.4.2、LVGL 8.4.0、`esp_lvgl_port` 2.8.0~1、Waveshare
BSP 2.0.0 以及列出的音频/文件辅助组件。ESP-IDF 必须满足 BSP 的 `>=5.3` 要求。CI
使用 v5.5.5 和 v6.0.2 构建，并把生成的依赖锁加入成功制品。

目标必须设为 `esp32s3`；存储、触摸、音频和 UI 运行行为仍需实物验证。
