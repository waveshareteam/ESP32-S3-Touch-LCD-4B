# Contributing

Contributions that improve the ESP32-S3-Touch-LCD-4B hardware resources,
examples, firmware documentation, and validation are welcome.

## Before Opening a Pull Request

1. Open an issue for changes that alter hardware behavior, public paths,
   firmware formats, or framework support.
2. Keep each change focused and use repository-relative paths in public text.
3. Add hardware evidence when changing pins, display or touch configuration,
   power control, storage, USB, audio, or other board-facing behavior.
4. Run `python scripts/check_repository.py` from the repository root.
5. Build every changed first-party example with its documented framework
   version. Hardware-facing changes should also be tested on the affected board
   revision.

## Examples

- Put ESP-IDF projects under `examples/esp-idf/<example-name>/`.
- Put Arduino sketches under `examples/arduino/<example-name>/` only when the
  repository officially supports Arduino.
- Do not add examples from bundled third-party libraries to the product CI
  matrix.
- Prefer managed components over copied reusable BSP, display, touch, sensor,
  audio, video, or bus driver components.

Each example README should list the target, supported framework version,
dependencies, configuration, build and flash commands, hardware revision, and
expected output.

## Hardware Files

Include the board revision in filenames or nearby metadata. Schematics, PCB
sources, manufacturing outputs, mechanical files, pin tables, and rendered
previews must agree. When source formats require a proprietary tool, also add a
portable PDF, image, or neutral interchange format where practical.

## Commit and Pull Request Hygiene

Use concise, neutral branch and commit names. Do not include usernames, local
paths, drive letters, network paths, IDE state, or machine-specific commands in
public repository text.
