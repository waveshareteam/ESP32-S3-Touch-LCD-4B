# Waveshare Wiki 资源

[English](wiki-resources.md) | [简体中文](wiki-resources_ZH.md)

本仓库从官方 [ESP32-S3-Touch-LCD-4B Wiki](https://www.waveshare.net/wiki/ESP32-S3-Touch-LCD-4B)
同步产品资源。对应页面为[修订 137986](https://www.waveshare.net/w/index.php?title=ESP32-S3-Touch-LCD-4B&oldid=137986)，
获取日期 2026-07-28。

## 已存资源

| 资源 | 仓库路径 | 字节 | SHA-256 |
| --- | --- | ---: | --- |
| 原理图 PDF | `hardware/schematics/ESP32-S3-Touch-LCD-4B.pdf` | 2,230,991 | `171d4d3a0041abe183746519dec6f7fa430bb5ae9acea11e02dda10b06014879` |
| Demo 源码包 | 已导入 `examples/` 和 `firmware/`，原 ZIP 不提交 | 153,244,726 | `a9025815a1e51b81dcdc1936271c5bab528bfc7ea37cd0a790dcb9a81e7e84f` |
| 出厂固件 | `firmware/ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin` | 16,732,160 | `06bc042509e018785b977bdb2e796d8ea555d68c9f22ebe1a64d9dad4f713c1f` |
| 产品 Wiki 图片 | `docs/assets/wiki/` | 合计 13,503,039 | 保留原文件名 |

官方附件：

- [原理图 PDF](https://www.waveshare.net/w/upload/8/82/ESP32-S3-Touch-LCD-4B.pdf)
- [Demo 源码包](https://files.waveshare.com/wiki/ESP32-S3-Touch-LCD-4B/ESP32-S3-Touch-LCD-4B-Demos.zip)

## Demo 导入映射

| 压缩包路径 | 仓库路径 | 说明 |
| --- | --- | --- |
| `ESP-IDF-v5.4.2/*` | `examples/esp-idf/*` | 五个第一方工程；不导入生成的 `sdkconfig`、`sdkconfig.old`、`.clangd` |
| `Arduino-v3.2.0/examples/*` | `examples/arduino/examples/*` | 八个第一方草图 |
| `Arduino-v3.2.0/libraries/*` | `examples/arduino/libraries/*` | 保留运行源码和许可证；省略上游测试、文档工具链、库示例和无关手册 |
| `FirmWare/*.bin` | `firmware/*.bin` | 出厂/恢复输入，不是源码构建制品 |

压缩包中的 `07_ES8311` 内嵌 PCM 录音只有文件名/大小注释，没有来源或许可证元数据，
因此不再分发；规范化草图改为运行时生成低幅测试音。驱动源码及许可证头继续保留。

压缩包共 5,756 个条目，解压后 5,116 个文件、341,818,010 字节；未发现绝对路径、
父目录穿越、大小写重复路径或生成的 `build/`、`managed_components/`、`.git/` 目录。

## 仅链接、不重复收录

通用或第三方资料保留官方链接，避免过时副本和转载条款不清：

- [ESP32-S3 中文数据手册](https://www.waveshare.net/w/upload/5/58/Esp32-s3_datasheet_cn.pdf)
- [ESP32-S3 英文数据手册](https://www.waveshare.net/w/upload/b/bd/Esp32-s3_datasheet_en.pdf)
- [QMI8658C](https://www.waveshare.net/w/upload/5/5f/QMI8658C.pdf)、[PCF85063A](https://www.waveshare.net/w/upload/9/97/PCF85063A.pdf)、[AXP2101](https://www.waveshare.net/w/upload/e/ed/X-power-AXP2101_SWcharge_V1.0.pdf)
- [ES8311](https://www.waveshare.net/w/upload/6/65/ES8311.DS.pdf)、[GT911](https://www.waveshare.net/w/upload/d/d9/GT911_EN_Datasheet.pdf)、[ES7210](https://www.waveshare.net/w/upload/5/54/ES7210-datasheet.pdf)
- [Espressif Flash Download Tool](https://dl.espressif.com/public/flash_download_tool.zip)

随 Arduino 库分发的上游许可证、运行源码和与本板有关的数据手册予以保留；库内部示例
不视为本产品第一方示例。

## 校验

- 原理图 PDF 有两页非空页面：电路原理图和元件布局/板框图。
- Wiki 图片大小与 SHA-1 来自 MediaWiki API。
- 当前示例引脚已与原理图和托管 BSP 交叉核对，详见[引脚审计](../hardware/pin-audit_ZH.md)；
  电气和实物硬件修订验证仍未完成。
