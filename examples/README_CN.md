# 示例

官方 Waveshare Demo 压缩包已规范化到两个框架目录：

| 框架 | 导入基线 | 一方示例数 | 说明 |
| --- | --- | ---: | --- |
| ESP-IDF | v5.4.2 | 5 | [esp-idf/README.md](esp-idf/README.md) |
| Arduino-ESP32 | 3.2.0 | 8 | [arduino/README.md](arduino/README.md) |

Arduino 目录还保留了产品草图依赖的随包库。随包库内部的示例属于上游库示例，不计入
本产品的一方示例。

ESP-IDF 生成文件 `sdkconfig`、`sdkconfig.old` 和 `.clangd` 未导入；官方压缩包内的
工程配置默认值、分区表、资源文件和本地组件均已保留。

## 兼容状态

上述版本号只表示源码压缩包的导入基线，并非持续维护的兼容范围。目前尚未声称完成：

- ESP-IDF v5.5 或 v6 编译验证；
- Arduino-ESP32 3.2.0 之后版本的编译验证；
- 示例引脚、原理图与实物硬件版本交叉核验之前的硬件功能验证。

当前验证边界见 [docs/ci.md](../docs/ci.md)，资源来源见
[docs/wiki-resources_CN.md](../docs/wiki-resources_CN.md)。
