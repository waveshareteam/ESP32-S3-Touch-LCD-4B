# 原理图引脚审计

[English](pin-audit.md) | [简体中文](pin-audit_ZH.md)

## 范围与证据

本审计覆盖第一方示例当前实际使用的引脚。主要证据为官方两页
[原理图 PDF](schematics/ESP32-S3-Touch-LCD-4B.pdf) 第 1 页，并与
`examples/arduino/` 的共享板级头文件和八个草图、`examples/esp-idf/` 工程，以及官方
[`waveshare/esp32_s3_touch_lcd_4b`](https://components.espressif.com/components/waveshare/esp32_s3_touch_lcd_4b)
托管 BSP 2.0.0 交叉比较。

附件文件名没有标识 PCB 修订，仓库也没有可编辑原理图、PCB 或网表。因此这是一份针对
公开 PDF 的源码交叉核对，不是按硬件修订出具的电气签核或实物验证。

## 已核对的当前分配

### 共享 I2C 与扩展器

| 信号 | 分配 | 交叉证据 |
| --- | --- | --- |
| 共享 I2C SDA / SCL | GPIO47 / GPIO48 | 原理图、ESP-IDF 默认值、BSP、全部 Arduino 草图 |
| TCA9554 地址 | `0x20` | 原理图地址脚接地，BSP 与草图一致 |
| EXIO0 / EXIO1 / EXIO2 | LCD 片选 / 串行数据 / 串行时钟 | 原理图、BSP、Arduino 头文件 |
| EXIO3 | 音频功放控制 | 原理图、BSP、音频草图 |
| EXIO5 / EXIO6 | GT911 复位 / 中断 | 原理图、BSP、显示触摸草图 |
| EXIO7 | LCD 复位 | 原理图、BSP、Arduino 头文件 |

AXP2101 示例使用地址 `0x34`，QMI8658 示例/BSP 使用 `0x6B`。GT911 复位和中断由
TCA9554 转接，不是 ESP32-S3 直连 GPIO。

### RGB 显示

| 功能 | GPIO 分配 |
| --- | --- |
| DE / VSYNC / HSYNC / PCLK | 17 / 3 / 46 / 9 |
| R0..R4 | 10、11、12、13、14 |
| G0..G5 | 21、8、18、45、38、39 |
| B0..B4 | 40、41、42、2、1 |
| 背光 | GPIO4 |
| 分辨率 | 480 × 480 |

导入草图传给 `Arduino_ESP32RGBPanel` 的数值和构造顺序原本正确，但行内 R/B 注释相反。
现在数值与正确颜色名统一定义在 `examples/arduino/libraries/Mylibrary/pin_config.h`。

### 音频与其他当前引脚

| 信号 | GPIO | 用途 |
| --- | ---: | --- |
| I2S MCLK / BCLK / LRCK | 5 / 16 / 7 | ES8311、ES7210 |
| ESP32 到 ES8311 数据 | 6 | 扬声器/输出路径 |
| ES7210 到 ESP32 数据 | 15 | 麦克风/输入路径 |
| 校准按键 | 0 | `04_Immersive_block` |

QMI8658、PCF85063、AXP2101、GT911、ES8311、ES7210 在适用处共享板级 I2C。原理图
与示例对当前 I2S 引脚和 TCA9554 功放使能的定义一致。

## 本次落地修改

- 将 I2C、RGB、TCA9554、显示尺寸、背光和音频分配集中到第一方 Arduino 板级头文件。
- 八个第一方草图不再重复硬编码板级数字引脚。
- 依据原理图纠正 R/B 名称，保留原本正确的电气数值。
- 继续忽略生成的 `managed_components/`；工程通过官方组件注册表获取 BSP，不提交依赖缓存。

## 待完成验证

- 确认公开 PDF 对应的 PCB 丝印和硬件修订。
- 若发布可编辑原理图、PCB、网表和 BOM，逐项比较。
- 从带修订证据核验 Flash/PSRAM 电气模式、USB、供电限制、连接器、AXP2101 中断和存储接口。
- 在指定实物修订上测试显示、触摸、音频、传感器、RTC/PMU、USB、电池和扩展接口。

完成前，CI 通过只代表编译、依赖解析、打包和制品证据。
