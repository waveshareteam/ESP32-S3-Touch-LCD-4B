# Immersive Block Example

This ESP32-S3 example uses the QMI8658 accelerometer and LVGL to move colored
shapes on the ESP32-S3-Touch-LCD-4B display as the board is tilted. At startup,
keep the board level while the sensor calibration runs. The BOOT button can
request recalibration.

## Requirements

- ESP32-S3-Touch-LCD-4B
- ESP-IDF `>=5.5.0`, as declared by `main/idf_component.yml`
- Waveshare `esp32_s3_touch_lcd_4b` and `qmi8658` managed components
- LVGL 9.2 or a compatible 9.x release

The project was imported from the official Demo archive. It has not yet been
build-validated in this repository.

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
