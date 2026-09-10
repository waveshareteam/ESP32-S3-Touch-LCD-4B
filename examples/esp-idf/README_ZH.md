# ESP-IDF 示例

[English](README.md) | [简体中文](README_ZH.md)

五个第一方工程导入自 `docs/wiki-resources_ZH.md` 链接的 Waveshare 官方 Demo。
`ESP-IDF-v5.4.2` 只表示源码包基线；CI 当前会用 ESP-IDF v5.5.5 和 v6.0.2 验证每个工程。

| 工程 | 功能 |
| --- | --- |
| `01_AXP2101` | AXP2101 电源管理 |
| `02_lvgl_demo_v9` | LVGL v9 显示与触摸 |
| `03_esp-brookesia` | ESP-Brookesia 应用 |
| `04_Immersive_block` | QMI8658 沉浸式方块 |
| `05_Spec_Analyzer` | 麦克风 FFT 频谱分析 |

使用满足各工程清单要求的 ESP-IDF，并把目标设为 `esp32s3`。`04_Immersive_block` 要求
ESP-IDF `>=5.5.0`，03/05 的 `bsp_extra` 要求 `>=5.3.0`。

官方压缩包中的生成文件 `sdkconfig`、`sdkconfig.old`、`.clangd` 已排除；默认配置、
分区、资源和本地组件予以保留。工程清单固定直接托管组件版本；CI 生成的完整依赖锁会
写入固件制品。详见 [CI 覆盖说明](../../docs/ci_ZH.md)。
