# ESP32-S3-Touch-LCD-4B 硬件参考模板

[English](HARDWARE_REFERENCE_TEMPLATE.md) | [简体中文](HARDWARE_REFERENCE_TEMPLATE_ZH.md)

> 状态：未验证模板。在依据已发布硬件文件完成所有字段前，不得将本文件作为引脚表或
> 产品规格使用。

## 修订证据

| 字段 | 值 | 来源 |
| --- | --- | --- |
| 产品名 | ESP32-S3-Touch-LCD-4B | 仓库名 |
| PCB 丝印 | TODO | TODO |
| 硬件修订 | TODO | TODO |
| 原理图文件与修订 | TODO | TODO |
| PCB 文件与修订 | TODO | TODO |
| BOM 文件与修订 | TODO | TODO |

## 核心硬件

记录 SoC/模组、Flash、PSRAM、USB 接口以及供电输入和限制，并为每个值给出来源。

## 显示与触摸

记录 LCD 控制器、分辨率、接口、颜色格式、时钟/时序、复位、片选、命令/数据、背光和
全部数据脚；记录触摸控制器、总线、地址、中断、复位及共享信号。

## 其他外设

为存储、音频、传感器、RTC/PMU、按键、LED、扩展接口和共享总线限制添加有证据的表格。

## 验证

- [ ] 原理图与 PCB/网表一致。
- [ ] BOM 装配选项已记录。
- [ ] BSP 与托管组件默认值一致。
- [ ] ESP-IDF 配置和示例一致。
- [ ] Arduino 板级选项和引脚头文件一致。
- [ ] 已在指定硬件修订上完成实物测试。
