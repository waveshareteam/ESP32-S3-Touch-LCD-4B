# 第三方声明

[English](THIRD_PARTY_NOTICES.md) | [简体中文](THIRD_PARTY_NOTICES_ZH.md)

导入 `examples/` 的 Waveshare 官方 Demo 包含多个上游项目的运行库、字体、媒体、部分与
本板有关的数据手册和固件二进制。这些文件保留原始版权、许可证、署名和通知；收录并不
将其重新许可为仓库级 Apache-2.0。

上游测试、文档构建树、跨平台开发支持、随包库示例和本板未使用器件的数据手册有意
省略；需要时请使用各库元数据或 README 中的上游链接。

主要导入根包括：

- `examples/arduino/libraries/GFX_Library_for_Arduino/`
- `examples/arduino/libraries/lvgl/`
- `examples/arduino/libraries/SensorLib/`
- `examples/arduino/libraries/XPowersLib/`
- `examples/esp-idf/*/components/` 下的本地组件
- `firmware/ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin`

| 导入内容 | 记录版本/来源 | 仓库内许可证证据 |
| --- | --- | --- |
| Arduino GFX | 1.6.0，`library.properties` 含上游 URL | BSD 许可证文件 |
| LVGL | 9.3.0 压缩包基线 | MIT `LICENCE.txt` 及所含编解码/库许可证 |
| SensorLib | 0.3.1，Lewis He | MIT `LICENSE` 与包元数据 |
| XPowersLib | 0.3.0，Lewis He | MIT `LICENSE` 与包元数据 |
| `07_ES8311` 驱动 | Espressif 源码头 | Apache-2.0 SPDX 头 |
| `08_ES7210`/audio HAL | Espressif 源码头 | 每个源码/头文件中的 MIT 通知 |
| ESP-IDF 本地 `bsp_extra` | 产品示例胶水 | Apache-2.0 `LICENSE` |

ES8311 草图在运行时生成测试音；导入包中没有来源和许可信息的 PCM 录音不再分发。
ESP-IDF 构建期间下载的托管组件不复制进本仓库；再次分发构建包前，应核对各组件注册表
元数据和制品中的依赖锁。

转载或修改前请检查各导入根中的许可证和源码头。源码包、同步 Wiki 修订和校验值见
[资源清单](docs/wiki-resources_ZH.md)。
