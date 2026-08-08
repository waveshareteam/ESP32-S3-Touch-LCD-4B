# 持续集成

[English](ci.md) | [简体中文](ci_ZH.md)

## 工作流

`Repository checks` 在每次推送和拉取请求中检查目录结构、本地 Markdown 链接、公开
文本隐私规则和静态单元测试。

`Build Examples` 先按变更路径分类，再动态发现第一方示例，只把受影响示例展开为独立
矩阵任务。完整运行包含一个分类任务、18 个固件构建任务和一个稳定聚合门禁：

| 表面 | 版本 | 示例 | 构建任务 |
| --- | --- | ---: | ---: |
| ESP-IDF | `v5.5.5`、`v6.0.2` | 5 | 10 |
| Arduino-ESP32 | `3.3.11` | 8 | 8 |

ESP-IDF 工程从 `examples/esp-idf/*/CMakeLists.txt` 发现；Arduino 草图从
`examples/arduino/examples/` 下的 `.ino` 发现，`libraries/` 内上游示例不会进入矩阵。
每个任务都有独立日志、结果和固件制品，一个示例失败不会取消其他示例。

工作流对每个拉取请求都运行，使分支保护始终能看到聚合状态 `Build examples`。Markdown、
协作模板和硬件参考等纯文档变更只运行分类与聚合任务。单个示例源码只选择该工程；随包
Arduino 库源码选择全部 Arduino 草图；工作流、发现、路由或打包工具变更选择两个完整
矩阵。无法分类的非文档路径采用安全回退，运行两个完整矩阵；空差异直接报错。

## 板卡配置

ESP-IDF 目标为 `esp32s3`。Arduino 使用随包库和以下配置：

```text
esp32:esp32:esp32s3:USBMode=hwcdc,CDCOnBoot=cdc,FlashSize=16M,PartitionScheme=app3M_fat9M_16MB,PSRAM=opi
```

官方压缩包的导入基线为 ESP-IDF v5.4.2 和 Arduino-ESP32 3.2.0；CI 使用上表版本验证
前向兼容。手工运行接受 `all`、示例目录名或仓库相对路径。例如选择
`05_Spec_Analyzer` 会生成两个 ESP-IDF 构建，不生成 Arduino 构建。

## 固件制品

成功任务上传以框架、示例和版本命名的可烧录 ZIP，其中包含：

- 含构建元数据和烧录命令的 `manifest.json`；
- ESP-IDF Component Manager 生成锁文件时的 `dependencies.lock`，以及清单中的 SHA-256；
- `flash.sh`、`flash.bat`、`flash_args.txt`；
- `bin/` 下的源固件分段；
- 可从偏移 `0x0` 烧录的合并镜像。

可使用以下命令按运行编号下载并解包：

```bash
python3 releases/download_artifacts.py --run-id <run-id> --clean
```

省略 `--run-id` 时选择当前分支最近的成功运行；下载只写入被忽略的
`releases/downloads/`。完整参数见[发布工具说明](../releases/README_ZH.md)。`firmware/`
中的出厂/恢复二进制是已提交发布输入，不会作为源码构建制品上传。

## 静态路由测试

`Repository checks` 会运行 `tests/` 下的合成测试，覆盖纯文档、单个 IDF/Arduino、随包
库、发布工具、不可变固件、重命名、未知路径和空差异失败。这些只是静态测试，不会在
本地编译固件。

## 验证边界

构建通过证明所选框架和板级选项的源码兼容性，不证明烧录、GPIO 电气行为或实物运行；
这些结论必须由对应硬件修订的资料和实测支持。
