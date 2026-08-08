# 硬件

[English](README.md) | [简体中文](README_ZH.md)

本目录是板卡专属电气和机械信息的事实来源。

| 资源 | 状态 |
| --- | --- |
| [原理图 PDF](schematics/ESP32-S3-Touch-LCD-4B.pdf) | 从产品 Wiki 导入的官方两页 PDF |
| [引脚审计](pin-audit_ZH.md) | 当前示例引脚已与 PDF 和托管 BSP 交叉核对 |
| 可编辑原理图源文件 | 同步的 Wiki 资源未提供 |
| PCB/BOM/生产文件 | 同步的 Wiki 资源未提供 |

PDF 包含电路原理图和元件布局/板框页，校验值见
[schematics/checksums.sha256](schematics/checksums.sha256)，来源见
[Wiki 资源清单](../docs/wiki-resources_ZH.md)。

当前示例引脚已与原理图和托管 BSP 交叉核对，但 PDF 没有硬件修订标识，仓库没有可编辑
设计文件，也未完成实物测试。使用任何数值前请阅读[引脚审计](pin-audit_ZH.md)；发布
修订专属参考前应填写[硬件参考模板](HARDWARE_REFERENCE_TEMPLATE_ZH.md)。

第三方数据手册可能有限制；转载权限不明确时优先链接芯片厂商的权威来源。
