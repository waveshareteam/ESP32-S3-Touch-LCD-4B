# ESP32-S3-Touch-LCD-4B

[English](README.md) | [简体中文](README_CN.md)

![ESP32-S3-Touch-LCD-4B](docs/assets/wiki/ESP32-S3-Touch-LCD-4B-inter001.jpg)

本仓库用于发布 Waveshare ESP32-S3-Touch-LCD-4B 的硬件资料、出厂固件和框架示例。

产品专属文件同步自官方
[Waveshare Wiki](https://www.waveshare.net/wiki/ESP32-S3-Touch-LCD-4B)，
对应页面[修订号 137986](https://www.waveshare.net/w/index.php?title=ESP32-S3-Touch-LCD-4B&oldid=137986)。
资源来源、导入映射、文件大小、校验值和转载说明见
[Wiki 资源清单](docs/wiki-resources_CN.md)。

## 资源入口

| 资源 | 位置 |
| --- | --- |
| 原理图 PDF | [hardware/schematics/ESP32-S3-Touch-LCD-4B.pdf](hardware/schematics/ESP32-S3-Touch-LCD-4B.pdf) |
| ESP-IDF 示例 | [examples/esp-idf/](examples/esp-idf/) |
| Arduino 示例与随包库 | [examples/arduino/](examples/arduino/) |
| 出厂固件 | [firmware/](firmware/) |
| CI 构建固件 | [Build Examples](https://github.com/waveshareteam/ESP32-S3-Touch-LCD-4B/actions/workflows/examples.yml) |
| 产品图与 Demo 截图 | [docs/assets/wiki/](docs/assets/wiki/) |
| Wiki 资源溯源 | [docs/wiki-resources_CN.md](docs/wiki-resources_CN.md) |

原始 Demo ZIP 未重复提交；其规范化内容已经存入 `examples/` 和 `firmware/`。

## 示例

ESP-IDF 导入基线为 ESP-IDF v5.4.2：

| 工程 | 功能 |
| --- | --- |
| `01_AXP2101` | AXP2101 电源管理示例 |
| `02_lvgl_demo_v9` | LVGL v9 显示与触摸示例 |
| `03_esp-brookesia` | ESP-Brookesia 应用示例 |
| `04_Immersive_block` | QMI8658 沉浸式方块示例 |
| `05_Spec_Analyzer` | 麦克风 FFT 频谱分析示例 |

Arduino 导入基线为 Arduino-ESP32 3.2.0：

| 草图 | 功能 |
| --- | --- |
| `01_HelloWorld` | 显示 Hello World |
| `02_GFX_AsciiTable` | Arduino GFX ASCII 表 |
| `03_LVGL_PCF85063_simpleTime` | LVGL 与 PCF85063 RTC |
| `04_LVGL_QMI8658_ui` | LVGL 与 QMI8658 UI |
| `05_LVGL_AXP2101_ADC_Data` | LVGL 与 AXP2101 ADC 数据 |
| `06_LVGL_Arduino_v9` | LVGL v9 Arduino 示例 |
| `07_ES8311` | ES8311 音频编解码器示例 |
| `08_ES7210` | ES7210 音频 ADC 示例 |

上述版本表示官方压缩包的导入基线。当前 CI 还会使用以下工具链验证规范化后的工程：

| 框架 | 工具链 | 第一方示例 | CI 任务数 |
| --- | --- | ---: | ---: |
| ESP-IDF | v5.5.5 | 5 | 5 |
| ESP-IDF | v6.0.2 | 5 | 5 |
| Arduino-ESP32 | 3.3.11 | 8 | 8 |

完整运行包含 2 个发现任务和 18 个独立固件构建任务。构建通过仅表示源码兼容和
固件打包验证，不代表已经完成实物硬件验证。详细规则见 [CI 说明](docs/ci.md)。

每个成功的示例任务都会上传独立、可烧录的 ZIP。维护者可以按运行编号批量下载并解包：

```bash
python3 releases/download_artifacts.py --run-id <run-id> --clean
```

省略 `--run-id` 时，脚本会查找当前分支最近一次成功的 `examples.yml` 运行。下载结果
存放在 `releases/downloads/run-<run-id>/`，并按制品名称分目录保存；该目录已被 Git
忽略。鉴权、筛选单个制品以及烧录包结构见
[固件打包与下载说明](releases/README.md)。

## 硬件与固件

官方两页原理图存放在 [hardware/schematics/](hardware/schematics/)：第 1 页为电路
原理图，第 2 页为元件布局/板框图。当前尚未完成原理图、示例引脚、BSP 源码与实物
硬件版本的逐引脚交叉核验，因此本仓库暂不声称已经完成硬件引脚审计。

出厂镜像 `ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin` 作为官方发布输入保留。
烧录前请使用 [firmware/checksums.sha256](firmware/checksums.sha256) 校验，并阅读
[固件说明](firmware/README_CN.md)。该文件不是源码构建 CI 的产物。

## 仓库目录

| 目录 | 用途 |
| --- | --- |
| `.github/` | Issue、Pull Request 模板与仓库检查 |
| `docs/` | 资源溯源与维护文档 |
| `examples/` | 导入的 ESP-IDF 与 Arduino 示例 |
| `firmware/` | 已发布的出厂/恢复固件 |
| `hardware/` | 原理图与硬件参考资料 |
| `releases/` | 源码构建固件的打包说明和工具 |
| `scripts/` | 仓库维护工具 |

各目录职责和命名约定见 [仓库结构说明](docs/repository-structure.md)。

## 贡献与支持

- 提交修改前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
- 支持渠道见 [SUPPORT.md](SUPPORT.md)。
- 安全问题请按 [SECURITY.md](SECURITY.md) 提交。

## 许可证

除非文件中另有说明，本仓库使用 [Apache License 2.0](LICENSE.txt)。第三方组件和文档
保留各自许可证与条款，详见
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
