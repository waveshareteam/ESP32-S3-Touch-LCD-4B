# 固件

本目录包含从官方 Waveshare Demo 压缩包导入的出厂镜像。

| 项目 | 内容 |
| --- | --- |
| 产品 | ESP32-S3-Touch-LCD-4B |
| 文件 | `ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin` |
| 压缩包标识 | `250807` |
| 大小 | 16,732,160 字节 |
| SHA-256 | `06bc042509e018785b977bdb2e796d8ea555d68c9f22ebe1a64d9dad4f713c1f` |
| 来源 | Waveshare 官方 Demo 压缩包 |

在仓库根目录执行以下命令校验文件：

```sh
sha256sum -c firmware/checksums.sha256
```

PowerShell 用户可比较以下命令的输出：

```powershell
Get-FileHash firmware/ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin -Algorithm SHA256
```

请按照官方[产品 Wiki](https://www.waveshare.net/wiki/ESP32-S3-Touch-LCD-4B)
的烧录流程操作，并在写入前核对 Wiki 当前给出的烧录地址和 Flash 参数。本仓库尚未在
实物上独立验证该镜像。

该出厂镜像属于发布/恢复输入，不参与源码构建 CI。对应固件的源码与构建说明目前尚未
包含在本仓库中，后续可再补充。不得用不同内容覆盖现有文件名；更新固件时应新增带版本
标识的文件和校验值。
