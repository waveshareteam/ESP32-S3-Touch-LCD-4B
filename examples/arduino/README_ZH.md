# Arduino 示例

[English](README.md) | [简体中文](README_ZH.md)

这些资源导入自 `docs/wiki-resources_ZH.md` 链接的 Waveshare 官方 Demo，压缩包基线为
Arduino-ESP32 3.2.0。`examples/` 下的八个目录是第一方草图；`libraries/` 保留产品所需
Arduino GFX、LVGL、板级辅助库、SensorLib 和 XPowersLib。板级头文件集中定义了与
原理图一致的 I2C、RGB、TCA9554、显示和音频引脚。

库的许可证、通知、运行源码和本板使用器件的数据手册予以保留。库内上游示例、测试、
文档工具链和无关器件资料不进入产品矩阵；完整开发资源应从各库 README 或
`library.properties` 链接的上游获取。

CI 使用 Arduino-ESP32 3.3.11 和以下板级选项编译八个草图：

```text
esp32:esp32:esp32s3:USBMode=hwcdc,CDCOnBoot=cdc,FlashSize=16M,PartitionScheme=app3M_fat9M_16MB,PSRAM=opi
```

手工运行可选择 `all`、草图名或仓库相对路径。当前引脚已与原理图和托管 BSP 交叉
核对，但构建通过不证明指定实物修订的运行行为。详见 [CI 说明](../../docs/ci_ZH.md)。
