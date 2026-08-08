# 发布制品

[English](README.md) | [简体中文](README_ZH.md)

`package_firmware.py` 将成功的 ESP-IDF 或 Arduino 构建转换为可烧录 ZIP。生成归档
只应位于 `releases/dist/`、`release-artifacts/` 或 CI 制品存储，均不提交到 Git。

ESP-IDF 打包器读取 `flasher_args.json`、保留所需分段、生成合并镜像，并在存在时复制
Component Manager 生成的 `dependencies.lock`，同时把其 SHA-256 写入清单。Arduino
打包器从稳定输出目录识别导出的二进制。

## 归档内容

每个归档包含 `manifest.json`、`flash.sh`、`flash.bat`、`flash_args.txt`、源固件分段、
`bin/*.combined.bin`，以及可用时的 ESP-IDF 依赖锁。Windows 使用 `flash.bat COMx`，
Linux 使用 `./flash.sh /dev/ttyACM0` 烧录合并镜像。

## 下载 CI 制品

按运行编号下载并安全解包全部固件制品：

```bash
python3 releases/download_artifacts.py --run-id <run-id> --clean
```

省略 `--run-id` 时选择当前分支最近一次成功的 `examples.yml` 运行。使用
`--artifact <name>` 精确选择，或用 `--pattern "firmware-arduino-*"` 按 glob 选择。
输出写入被 Git 忽略的 `releases/downloads/run-<run-id>/`。脚本优先复用 `gh auth login`，
也支持 `GH_TOKEN`/`GITHUB_TOKEN`；下载外层归档和嵌套 ZIP 都会安全校验。

`firmware/` 下已提交的出厂二进制是恢复输入，不会重新打包为 CI 输出。
