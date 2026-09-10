# Repository Structure

[English](repository-structure.md) | [简体中文](repository-structure_ZH.md)

This repository follows the normalized layout used by current Waveshare ESP32
product repositories. Directory names are lowercase and framework versions do
not appear in directory names.

| Path | Purpose | Inclusion rule |
| --- | --- | --- |
| `.github/` | Collaboration templates and automation | Always present |
| `docs/` | User and maintainer documentation | Always present |
| `examples/` | First-party framework examples | One project per directory |
| `firmware/` | Released binaries or maintained firmware source | Keep binary and source roles explicit |
| `hardware/` | Schematics and hardware design references | Identify every board revision |
| `releases/` | Packaging tools and generated-artifact documentation | Never commit generated archives |
| `scripts/` | Discovery, routing, and maintenance utilities | Keep scripts platform-neutral where practical |
| `tests/` | Static repository and routing tests | Must not compile firmware locally |
| `config/` | Shared audit policy | Add only maintained, repository-wide configuration |

Optional roots such as `config/` and `tests/` should be created only when they
contain shared configuration or maintained validation resources. Empty
placeholder directories are not kept.

## Example Roots

Create framework roots only when the repository contains maintained projects:

```text
examples/
|-- esp-idf/
|   `-- <example-name>/
`-- arduino/
    `-- <example-name>/
```

An ESP-IDF example is a complete project with a top-level `CMakeLists.txt`, a
`main/` component, an explicit `esp32s3` target, and `README.md`/`README_ZH.md`.
An Arduino example is a sketch directory with a matching `.ino` file and both
README languages. Bundled
library examples are not first-party product examples and must not enter the
default product CI matrix.

## Hardware and Firmware Boundaries

Hardware source, rendered documents, and revision metadata belong under
`hardware/`. Checked-in factory or recovery binaries belong under `firmware/`
with checksums and flash instructions. Firmware source projects may also live
under `firmware/<project-name>/`, but must be clearly labeled and built by CI
when they are maintained from source.

Generated firmware archives belong in workflow artifact storage or ignored
output directories under `releases/`; they are not source files.
