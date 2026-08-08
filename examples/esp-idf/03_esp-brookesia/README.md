# ESP-Brookesia Application Demo

[English](README.md) | [简体中文](README_ZH.md)

This project runs an ESP-Brookesia LVGL application shell with the bundled
calculator, drawing, and music-player applications. `components/apps` is
first-party demo functionality; `components/bsp_extra` is product-specific
board/audio glue. Generated `managed_components/` content is intentionally not
committed.

Direct dependencies are fixed to ESP-Brookesia 0.4.2, LVGL 8.4.0,
`esp_lvgl_port` 2.8.0~1, the Waveshare BSP 2.0.0, and the audio/file helpers
listed in the component manifests. ESP-IDF must satisfy the BSP requirement
(`>=5.3`). CI builds v5.5.5 and v6.0.2 and packages the generated dependency
lock with successful artifacts.

Set the target to `esp32s3`; runtime storage, touch, audio, and UI behavior still
require physical-board validation.
