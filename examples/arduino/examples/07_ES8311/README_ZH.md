# ES8311 音频播放

[English](README.md) | [简体中文](README_ZH.md)

示例初始化 ES8311，通过 TCA9554 EXIO3 使能功放，并以 I2S 播放运行时生成的低幅
440 Hz 测试音，不嵌入第三方录音。原理图核对后的音频分配为 MCLK GPIO5、BCLK
GPIO16、LRCK GPIO7、编解码器输出数据 GPIO6、输入
数据 GPIO15，统一定义于 `Mylibrary/pin_config.h`。

CI 使用 Arduino-ESP32 3.3.11 编译。音量、声道、扬声器负载和音质需实物测试。
