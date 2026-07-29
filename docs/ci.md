# Continuous Integration

## Workflows

`Repository checks` validates the repository layout, local Markdown links, and
public-text hygiene on every push and pull request.

`Build Examples` discovers first-party demos dynamically and expands each demo
into an independent matrix job. A full run contains two discovery jobs and 18
firmware jobs:

| Surface | Versions | Demos | Build jobs |
| --- | --- | ---: | ---: |
| ESP-IDF | `v5.5.5`, `v6.0.2` | 5 | 10 |
| Arduino-ESP32 | `3.3.11` | 8 | 8 |

ESP-IDF projects are discovered from
`examples/esp-idf/*/CMakeLists.txt`. Arduino sketches are discovered from `.ino`
files under `examples/arduino/examples/`; examples bundled inside
`examples/arduino/libraries/` are excluded.

Each matrix job has its own log, result, and firmware artifact. One failed demo
does not hide or cancel the results of the other demos.

## Board Configuration

ESP-IDF builds target `esp32s3`. Arduino builds use the bundled libraries and
the board configuration below:

```text
esp32:esp32:esp32s3:USBMode=hwcdc,CDCOnBoot=cdc,FlashSize=16M,PartitionScheme=app3M_fat9M_16MB,PSRAM=opi
```

The official archive names ESP-IDF v5.4.2 and Arduino-ESP32 3.2.0 as its import
baselines. CI uses the newer versions above to verify forward compatibility.

## Manual Selection

`workflow_dispatch` accepts `all`, an example directory name, or a
repository-relative example path. For example, selecting `05_Spec_Analyzer`
generates one build for each ESP-IDF version and no Arduino builds.

## Firmware Artifacts

Every successful matrix job uploads one flashable ZIP named with the framework,
demo, and framework version. Each archive contains:

- `manifest.json` with build metadata and the flash command;
- `flash.sh`, `flash.bat`, and `flash_args.txt`;
- the source firmware segments under `bin/`; and
- a combined firmware image that can be flashed at offset `0x0`.

Download and extract the artifacts from a specific run with:

```bash
python3 releases/download_artifacts.py --run-id <run-id> --clean
```

Without `--run-id`, the helper selects the latest successful `examples.yml`
run for the current branch. `--artifact <name>` selects an exact artifact and
`--pattern "firmware-arduino-*"` selects artifacts by glob. The helper uses an
authenticated GitHub CLI session when available, or `GH_TOKEN`/
`GITHUB_TOKEN`, and writes only to the ignored `releases/downloads/` tree by
default. See [the release helper documentation](../releases/README.md) for the
complete interface.

Factory and recovery binaries under `firmware/` are checked-in release inputs
and are never uploaded as source-built CI artifacts.

## Validation Boundary

A passing build proves source compatibility for the selected framework and
board options. It does not prove successful flashing, correct GPIO assignments,
or physical-board behavior; those require the hardware reference and testing on
the named board revision.
