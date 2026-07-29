# Waveshare Wiki 资源

本仓库从 Waveshare 官方
[ESP32-S3-Touch-LCD-4B Wiki](https://www.waveshare.net/wiki/ESP32-S3-Touch-LCD-4B)
同步产品专属资源。对应页面修订为
[137986](https://www.waveshare.net/w/index.php?title=ESP32-S3-Touch-LCD-4B&oldid=137986)，
获取日期为 2026-07-28。

## 已存入仓库

| 资源 | 仓库路径 | 大小 | SHA-256 |
| --- | --- | ---: | --- |
| 原理图 PDF | `hardware/schematics/ESP32-S3-Touch-LCD-4B.pdf` | 2,230,991 字节 | `171d4d3a0041abe183746519dec6f7fa430bb5ae9acea11e02dda10b06014879` |
| Demo 压缩包 | 已解包到 `examples/` 和 `firmware/`，不重复提交原 ZIP | 153,244,726 字节 | `a9025815a1e51b81dcdc1936271c5bab528bfc7ea37cd0a790dcb9a81e7e84f` |
| 出厂固件 | `firmware/ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin` | 16,732,160 字节 | `06bc042509e018785b977bdb2e796d8ea555d68c9f22ebe1a64d9dad4f713c1f` |
| 产品 Wiki 原图 | `docs/assets/wiki/` | 合计 13,503,039 字节 | 保留原始文件名 |

官方附件：

- [原理图 PDF](https://www.waveshare.net/w/upload/8/82/ESP32-S3-Touch-LCD-4B.pdf)
- [Demo 示例包](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-4B/ESP32-S3-Touch-LCD-4B-Demos.zip)

## Demo 目录映射

| 压缩包目录 | 仓库目录 | 说明 |
| --- | --- | --- |
| `ESP-IDF-v5.4.2/*` | `examples/esp-idf/*` | 5 个一方工程；排除生成的 `sdkconfig`、`sdkconfig.old` 和 `.clangd` |
| `Arduino-v3.2.0/examples/*` | `examples/arduino/examples/*` | 8 个一方草图 |
| `Arduino-v3.2.0/libraries/*` | `examples/arduino/libraries/*` | 保留运行源码与许可证；排除上游测试、开发文档、库内示例和无关数据手册 |
| `FirmWare/*.bin` | `firmware/*.bin` | 出厂/恢复输入，不作为源码构建产物 |

ZIP 包含 5,756 个条目，解压后为 5,116 个文件、341,818,010 字节。
未发现绝对路径、父目录穿越、大小写重复路径，也没有 `build/`、
`managed_components/` 或 `.git/` 生成目录。

## 仅保留链接

ESP32-S3、QMI8658C、PCF85063A、AXP2101、ES8311、GT911 和 ES7210
等通用芯片手册，以及字模、图片取模和烧录工具，不在仓库根资源区重复保存。
完整官方链接见 [英文资源清单](wiki-resources.md#linked-not-duplicated)。
随 Arduino 库一起分发的运行源码、许可证和本板相关数据手册予以保留；上游测试、
开发文档、库内示例及无关芯片数据手册不存入本产品仓库。

## 校验状态

- 原理图为 2 页非空 PDF，第 1 页为电路原理图，第 2 页为元件布局/板框图。
- Wiki 图片的大小和 SHA-1 来源于 MediaWiki API。
- 尚未完成原理图、示例引脚定义与实物硬件版本的逐引脚交叉核验。
