# Hardware

This directory is the source of truth for board-specific electrical and
mechanical information.

## Available Files

| Resource | Status |
| --- | --- |
| [Schematic PDF](schematics/ESP32-S3-Touch-LCD-4B.pdf) | Official two-page PDF imported from the product Wiki |
| Editable schematic source | Not included in the synchronized Wiki resources |
| PCB/BOM/manufacturing files | Not included in the synchronized Wiki resources |

The PDF contains an electrical schematic and a
component-placement/board-outline page. Its checksum is recorded in
[schematics/checksums.sha256](schematics/checksums.sha256), and provenance is
recorded in [docs/wiki-resources.md](../docs/wiki-resources.md).

## Validation Boundary

The PDF was checked for page count and visible content, but the schematic,
example pin definitions, BSP code, and physical hardware revision have not yet
been cross-checked pin by pin. Use
[HARDWARE_REFERENCE_TEMPLATE.md](HARDWARE_REFERENCE_TEMPLATE.md) for that
audit before publishing a verified board revision reference.

Third-party datasheets may have redistribution restrictions. Prefer links to
the component manufacturer's canonical source when redistribution permission
is unclear. The product Wiki datasheet links are collected in
[docs/wiki-resources.md](../docs/wiki-resources.md#linked-not-duplicated).
