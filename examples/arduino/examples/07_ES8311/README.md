# ES8311 Audio Playback

[English](README.md) | [简体中文](README_ZH.md)

Initializes the ES8311 codec, enables the amplifier through TCA9554 EXIO3, and
plays a low-amplitude 440 Hz test tone generated at runtime over I2S. No
third-party recording is embedded. The schematic-backed audio assignments
are MCLK GPIO5, BCLK GPIO16, LRCK GPIO7, codec output-data GPIO6, and input-data
GPIO15, all defined in `Mylibrary/pin_config.h`.

CI compiles the sketch with Arduino-ESP32 3.3.11. Volume, channel routing,
speaker load, and audio quality require physical-board testing.
