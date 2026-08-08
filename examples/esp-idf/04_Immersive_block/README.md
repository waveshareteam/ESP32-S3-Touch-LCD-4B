# Immersive Block Example

[English](README.md) | [简体中文](README_ZH.md)

This ESP32-S3 example uses the QMI8658 accelerometer and LVGL to move colored
shapes on the ESP32-S3-Touch-LCD-4B display as the board is tilted. At startup,
keep the board level while the sensor calibration runs. The BOOT button can
request recalibration.

## Requirements

- ESP32-S3-Touch-LCD-4B
- ESP-IDF `>=5.5.0`, as declared by `main/idf_component.yml`
- Waveshare `esp32_s3_touch_lcd_4b` 2.0.0 and `qmi8658` 2.0.0 managed components
- LVGL 9.5.0

CI validates the project with ESP-IDF v5.5.5 and v6.0.2. Runtime calibration,
display, and sensor behavior still require physical-board validation.

## Build

After activating a compatible ESP-IDF environment:

```sh
idf.py set-target esp32s3
idf.py build
idf.py -p PORT flash monitor
```

## Project Files

| Path | Purpose |
| --- | --- |
| [main/main.c](main/main.c) | Display, calibration, QMI8658 input, and shape movement |
| [main/idf_component.yml](main/idf_component.yml) | Managed component and IDF version requirements |
| [sdkconfig.defaults](sdkconfig.defaults) | Project configuration defaults |

The generated `sdkconfig`, `sdkconfig.old`, and `.clangd` files from the
official archive are intentionally not stored in the repository.
