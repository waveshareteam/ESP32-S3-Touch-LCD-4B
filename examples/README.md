# Examples

The official Waveshare Demo archive has been normalized into two framework
roots:

| Framework | Imported baseline | First-party examples | Documentation |
| --- | --- | ---: | --- |
| ESP-IDF | v5.4.2 | 5 | [esp-idf/README.md](esp-idf/README.md) |
| Arduino-ESP32 | 3.2.0 | 8 | [arduino/README.md](arduino/README.md) |

The Arduino tree also contains the bundled libraries required by the product
sketches. Examples contained inside those libraries are upstream library
examples and are not counted as first-party product examples.

Generated ESP-IDF files (`sdkconfig`, `sdkconfig.old`, and `.clangd`) were not
imported. Project configuration defaults, partitions, assets, and local
components were retained from the official archive.

## Compatibility Status

The imported version numbers describe the source archive, not a maintained
compatibility range. No build claim is made yet for:

- ESP-IDF v5.5 or v6;
- Arduino-ESP32 releases newer than 3.2.0; or
- hardware behavior before the example pin definitions are cross-checked
  against the schematic and physical board revision.

See [docs/ci.md](../docs/ci.md) for the current validation boundary and
[docs/wiki-resources.md](../docs/wiki-resources.md) for resource provenance.
