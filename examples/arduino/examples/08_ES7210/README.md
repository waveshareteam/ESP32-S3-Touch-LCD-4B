# ES7210 Audio Capture and VAD

[English](README.md) | [简体中文](README_ZH.md)

Configures the ES7210 audio ADC and ESP32-S3 I2S receiver, then feeds captured
16 kHz samples to the ESP VAD API. The audio clock/data and TCA9554 amplifier
control assignments are shared through `Mylibrary/pin_config.h`.

CI compiles the sketch with Arduino-ESP32 3.3.11. Microphone population,
channel mapping, gain, clock integrity, and voice detection require hardware
testing in the intended acoustic environment.
