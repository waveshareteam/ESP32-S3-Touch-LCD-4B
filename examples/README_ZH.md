# 示例

[English](README.md) | [简体中文](README_ZH.md)

Waveshare 官方 Demo 压缩包已规范化为两个框架目录：

| 框架 | 导入基线 | 第一方示例 | 文档 |
| --- | --- | ---: | --- |
| ESP-IDF | v5.4.2 | 5 | [esp-idf/README_ZH.md](esp-idf/README_ZH.md) |
| Arduino-ESP32 | 3.2.0 | 8 | [arduino/README_ZH.md](arduino/README_ZH.md) |

Arduino 目录还保留产品草图所需的随包库；库内部的上游示例不计为产品第一方示例。
ESP-IDF 生成的 `sdkconfig`、`sdkconfig.old`、`.clangd` 未导入，官方工程默认配置、
分区、资源和本地组件予以保留。

## 兼容状态

导入版本号只说明源码包基线，不是当前维护范围。CI 会验证：

- 五个 ESP-IDF 工程分别使用 v5.5.5 和 v6.0.2；
- 八个第一方草图使用 Arduino-ESP32 3.3.11；
- 每个成功任务生成可烧录固件制品。

当前示例引脚已与原理图和托管 BSP 交叉核对，但 CI 不声称实物板卡行为。详细范围见
[CI 说明](../docs/ci_ZH.md)，资源来源见[Wiki 资源清单](../docs/wiki-resources_ZH.md)。
