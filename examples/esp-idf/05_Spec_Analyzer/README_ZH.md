# 音频频谱分析示例

[English](README.md) | [简体中文](README_ZH.md)

本 ESP32-S3 工程通过板载音频路径采集麦克风数据，使用 ESP-DSP 做 FFT，并以 LVGL
显示频谱。产品专属音频/BSP 胶水保存在 `components/bsp_extra`。

清单固定 LVGL 9.5.0、ESP-DSP 1.8.2、Waveshare BSP 2.0.0 和列出的音频/文件辅助
组件。BSP 要求 ESP-IDF `>=5.3`；CI 使用 v5.5.5 与 v6.0.2 构建，并把生成的依赖锁
加入成功制品。

目标必须设为 `esp32s3`。构建通过不证明实物上的麦克风、编解码器、功放、FFT 校准或
显示行为。
