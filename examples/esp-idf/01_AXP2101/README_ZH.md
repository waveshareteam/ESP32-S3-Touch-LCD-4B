# AXP2101 电源管理示例

[English](README.md) | [简体中文](README_ZH.md)

本 ESP32-S3 工程通过 I2C 初始化板载 AXP2101 PMIC，并每秒输出各电源轨的使能和电压
状态。板卡默认 SDA GPIO47、SCL GPIO48、器件地址 `0x34`，不使用直连 PMU 中断脚。

工程在 `components/XPowersLib` 保留经裁剪的随包 XPowersLib 副本；未记录其精确导入的
上游修订，保留的 MIT 许可证路径为 `components/XPowersLib/LICENSE`。尚未验证存在语义和
硬件等效的托管组件，因此继续保留本地副本。仅当候选组件能在 ESP-IDF v5.5.5 和 v6.0.2
上保留 AXP2101 的回调、IRQ 和充电器 API，以及本板 I2C GPIO47/GPIO48/地址 `0x34`
配置时，才重新评估。移植到其他板卡时可在 `XPowers Configuration` 中选择 PMU 与 I2C；
中断值为负表示可选 IRQ 路径关闭。

激活 ESP-IDF 后将目标设为 `esp32s3`，再使用标准 `idf.py` 命令构建或烧录。CI 会以
ESP-IDF v5.5.5 和 v6.0.2 编译并打包；I2C 总线/设备注册失败现在会返回到 `app_main`。
CI 不证明实物 PMIC 的电气行为。串口正常输出以 `I2C initialized successfully`、
`Init PMU SUCCESS!` 开始，随后显示电源轨状态表。
