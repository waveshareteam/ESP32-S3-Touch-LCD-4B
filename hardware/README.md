# Hardware

[English](README.md) | [简体中文](README_ZH.md)

This directory is the source of truth for board-specific electrical and
mechanical information.

## Available Files

| Resource | Status |
| --- | --- |
| [Schematic PDF](schematics/ESP32-S3-Touch-LCD-4B.pdf) | Official two-page PDF imported from the product Wiki |
| [Pin audit](pin-audit.md) | Active example pins cross-checked against the PDF and managed BSP |
| Editable schematic source | Not included in the synchronized Wiki resources |
| PCB/BOM/manufacturing files | Not included in the synchronized Wiki resources |

The PDF contains an electrical schematic and a
component-placement/board-outline page. Its checksum is recorded in
[schematics/checksums.sha256](schematics/checksums.sha256), and provenance is
recorded in [docs/wiki-resources.md](../docs/wiki-resources.md).

## Validation Boundary

The active example pin definitions were cross-checked against the schematic and
managed BSP. The PDF is not revision-qualified, editable design files are not
available here, and physical-board testing remains open. Read
[pin-audit.md](pin-audit.md) before treating a value as verified, and use
[HARDWARE_REFERENCE_TEMPLATE.md](HARDWARE_REFERENCE_TEMPLATE.md) before
publishing a revision-specific reference.

Third-party datasheets may have redistribution restrictions. Prefer links to
the component manufacturer's canonical source when redistribution permission
is unclear. The product Wiki datasheet links are collected in
[docs/wiki-resources.md](../docs/wiki-resources.md#linked-not-duplicated).
