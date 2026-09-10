# 脚本

[English](README.md) | [简体中文](README_ZH.md)

- `check_repository.py` 检查目录布局、本地 Markdown 链接和公开文本隐私。
- `discover_examples.py` 发现第一方 ESP-IDF 工程与 Arduino 草图，过滤手工选择器并生成矩阵。
- `route_examples.py` 对 Git 差异分类并生成最小安全矩阵；未知源码路径回退到两个完整矩阵。

`config/markdown-audit.json` 是 Waveshare 可复用 Markdown 审计使用的仓库策略；
`check_repository.py` 也会读取其中的排除项来强制双语配对，避免兼容路径与 CI 策略漂移。

手工选择器接受 `all`、示例目录名或仓库相对路径。随包 Arduino 库内部示例不会进入
产品矩阵。路由的合成测试位于 `tests/`，只做静态验证，不编译固件。

固件打包由 `releases/package_firmware.py` 实现，`releases/download_artifacts.py` 下载并
安全解包 CI 制品。生成的构建、打包和下载目录都由 Git 忽略。
