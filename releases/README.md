# Release Artifacts

[English](README.md) | [简体中文](README_ZH.md)

`package_firmware.py` converts a successful ESP-IDF or Arduino build into a
flashable ZIP. Generated archives belong in `releases/dist/`,
`release-artifacts/`, or CI artifact storage and are ignored by Git.

## ESP-IDF

Build an example and package its build directory:

```bash
idf.py -C examples/esp-idf/05_Spec_Analyzer \
  -B build/05_Spec_Analyzer-v6.0.2 \
  set-target esp32s3 build

python3 releases/package_firmware.py \
  --framework esp-idf \
  --project examples/esp-idf/05_Spec_Analyzer \
  --build-dir build/05_Spec_Analyzer-v6.0.2 \
  --name ESP32-S3-Touch-LCD-4B-05_Spec_Analyzer-v6.0.2 \
  --framework-version v6.0.2 \
  --target esp32s3
```

The script reads ESP-IDF's `flasher_args.json`, preserves the required source
segments, creates a combined image, and copies the generated
`dependencies.lock` with a SHA-256 manifest entry when it exists.

## Arduino

Export binaries to a stable directory before packaging:

```bash
arduino-cli compile \
  --fqbn "esp32:esp32:esp32s3:USBMode=hwcdc,CDCOnBoot=cdc,FlashSize=16M,PartitionScheme=app3M_fat9M_16MB,PSRAM=opi" \
  --libraries examples/arduino/libraries \
  --export-binaries \
  --output-dir build/01_HelloWorld-3.3.11 \
  examples/arduino/examples/01_HelloWorld

python3 releases/package_firmware.py \
  --framework arduino \
  --project examples/arduino/examples/01_HelloWorld \
  --build-dir build/01_HelloWorld-3.3.11 \
  --name ESP32-S3-Touch-LCD-4B-01_HelloWorld-arduino-3.3.11 \
  --framework-version 3.3.11 \
  --target esp32s3
```

## Archive Contents

Each archive includes `manifest.json`, `flash.sh`, `flash.bat`,
`flash_args.txt`, the source firmware segments, `bin/*.combined.bin`, and the
ESP-IDF dependency lock when available. Flash
the combined image with `flash.bat COMx` on Windows or
`./flash.sh /dev/ttyACM0` on Linux.

The `Build Examples` workflow uploads one artifact for every successful demo and
framework version.

## Download CI Artifacts

Download and extract all firmware artifacts from a completed workflow run:

```bash
python3 releases/download_artifacts.py --run-id <run-id> --clean
```

If `--run-id` is omitted, the script finds the latest successful `examples.yml`
run for the current branch:

```bash
python3 releases/download_artifacts.py --clean
```

Extracted packages are written to `releases/downloads/run-<run-id>/`, with one
directory per artifact. Use `--artifact <name>` to download an exact artifact;
the option may be repeated. Use a glob when selecting a family of artifacts:

```bash
python3 releases/download_artifacts.py \
  --pattern "firmware-esp-idf-*v6.0.2" \
  --clean
```

The downloader reuses `gh auth login` when GitHub CLI is installed. It can also
read `GH_TOKEN` or `GITHUB_TOKEN`. Run the script with `--repo owner/name` when
downloading from a fork or another repository. The downloaded outer archive is
verified during extraction, nested firmware ZIPs are unpacked safely, and a
run-level `artifacts.json` summary is generated.

Checked-in factory binaries under `firmware/` are recovery inputs and are not
repackaged as CI output.
