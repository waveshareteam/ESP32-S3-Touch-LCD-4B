# Firmware

[English](README.md) | [简体中文](README_ZH.md)

This directory contains the factory image imported from the official Waveshare
Demo archive.

| Item | Value |
| --- | --- |
| Product | ESP32-S3-Touch-LCD-4B |
| File | `ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin` |
| Archive identifier | `250807` |
| Size | 16,732,160 bytes |
| SHA-256 | `06bc042509e018785b977bdb2e796d8ea555d68c9f22ebe1a64d9dad4f713c1f` |
| Source | Official Waveshare Demo archive |

From the repository root, verify the file before flashing:

```sh
sha256sum -c firmware/checksums.sha256
```

PowerShell users can compare the output of:

```powershell
Get-FileHash firmware/ESP32-S3-Touch-LCD-4B-FactoryXiaozhi_250807.bin -Algorithm SHA256
```

Use the flashing procedure on the official
[product Wiki](https://www.waveshare.net/wiki/ESP32-S3-Touch-LCD-4B), and
confirm the current offset and flash settings there before writing the image.
The repository has not independently hardware-validated this binary.

This checked-in factory image is a release/recovery input and is excluded from
source-build CI. Source and build instructions for the factory firmware are not
included in this repository yet and may be added in a future update. Do not
replace this filename with different binary content; add a new versioned file
and checksum instead.
