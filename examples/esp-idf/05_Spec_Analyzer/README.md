# Audio Spectrum Analyzer

[English](README.md) | [简体中文](README_ZH.md)

This ESP32-S3 project captures microphone audio through the board audio path,
runs FFT processing with ESP-DSP, and renders the spectrum with LVGL. The
project retains product-specific audio/BSP glue in `components/bsp_extra`.

Direct dependencies are fixed to LVGL 9.5.0, ESP-DSP 1.8.2, the Waveshare BSP
2.0.0, and the audio/file helpers listed in the manifests. The BSP requires
ESP-IDF `>=5.3`; CI builds v5.5.5 and v6.0.2 and packages the generated
dependency lock with successful artifacts.

These pins preserve the currently tested Waveshare board/audio, ESP-DSP, and
LVGL 9 display API contract. Revisit the version set only after candidate
versions build with ESP-IDF v5.5.5 and v6.0.2 and the schematic-backed audio
configuration is rechecked; physical-board validation remains separate.

Set the target to `esp32s3`. A successful build does not prove microphone,
codec, amplifier, FFT calibration, or display behavior on physical hardware.
