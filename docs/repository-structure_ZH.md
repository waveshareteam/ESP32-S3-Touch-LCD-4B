# 仓库结构

[English](repository-structure.md) | [简体中文](repository-structure_ZH.md)

本仓库采用 Waveshare ESP32 产品仓库的规范化布局。目录名使用小写，框架版本不写入
目录名。

| 路径 | 用途 | 收录规则 |
| --- | --- | --- |
| `.github/` | 协作模板与自动化 | 始终存在 |
| `docs/` | 用户与维护文档 | 始终存在 |
| `examples/` | 第一方框架示例 | 每个目录一个工程 |
| `firmware/` | 已发布二进制或维护中的固件源码 | 明确区分二进制与源码职责 |
| `hardware/` | 原理图和硬件设计参考 | 标识硬件修订 |
| `releases/` | 打包工具与生成制品说明 | 不提交生成的归档 |
| `scripts/` | 发现、路由和维护工具 | 尽量保持跨平台 |
| `tests/` | 仓库和路由静态测试 | 不在本地编译固件 |
| `config/` | 共享审计策略 | 只放仓库级、持续维护的配置 |

只有在实际包含共享配置或维护测试时才创建 `config/`、`tests/` 等可选根目录，不保留
空占位目录。

## 示例目录

ESP-IDF 示例必须是带顶层 `CMakeLists.txt`、`main/` 组件、明确 `esp32s3` 目标以及
`README.md`/`README_ZH.md` 的完整工程。Arduino 示例必须是含同名 `.ino` 和两种
README 的草图目录。随包库内部示例属于上游内容，不进入默认产品 CI 矩阵。

## 硬件与固件边界

硬件源文件、渲染文档和修订元数据放入 `hardware/`。已提交的出厂或恢复二进制放入
`firmware/`，同时提供校验值和烧录说明。若 `firmware/<project-name>/` 包含持续维护的
固件源码，必须明确标识并由 CI 构建。生成的固件归档只存于 Actions 制品或
`releases/` 下被忽略的输出目录，不作为源码提交。
