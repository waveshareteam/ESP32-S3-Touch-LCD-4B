# ES7210 音频采集与 VAD

[English](README.md) | [简体中文](README_ZH.md)

示例配置 ES7210 音频 ADC 和 ESP32-S3 I2S 接收器，再把采集的 16 kHz 样本送入 ESP
VAD。音频时钟/数据与 TCA9554 功放控制统一来自 `Mylibrary/pin_config.h`。

CI 使用 Arduino-ESP32 3.3.11 编译。麦克风装配、声道映射、增益、时钟完整性和语音检测
需在目标声学环境中实物测试。
