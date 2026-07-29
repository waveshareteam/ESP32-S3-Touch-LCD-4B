# ESP-IDF Examples

These five first-party projects were imported from the official Waveshare Demo
archive linked in `docs/wiki-resources.md`. The archive directory was named
`ESP-IDF-v5.4.2`; this is the source baseline, not a claim of compatibility
with newer ESP-IDF releases.

| Project | Feature |
| --- | --- |
| `01_AXP2101` | AXP2101 power-management example |
| `02_lvgl_demo_v9` | LVGL v9 display and touch demo |
| `03_esp-brookesia` | ESP-Brookesia application demo |
| `04_Immersive_block` | QMI8658 immersive block demo |
| `05_Spec_Analyzer` | Microphone FFT spectrum analyzer |

Activate an explicit ESP-IDF environment that satisfies each project's
component manifests. The archive directory name is not a uniform build
requirement: `04_Immersive_block` declares ESP-IDF `>=5.5.0`, while local
`bsp_extra` manifests in `03_esp-brookesia` and `05_Spec_Analyzer` declare
ESP-IDF `>=5.3.0`. After activating a compatible environment, for example:

```powershell
idf.py -C examples/esp-idf/01_AXP2101 set-target esp32s3 build
```

Generated `sdkconfig`, `sdkconfig.old`, and `.clangd` files from the archive
were intentionally excluded. Project `sdkconfig.defaults`, partitions, source
assets, and local components were retained. The imported projects have not yet
been build-validated as a complete set or migrated against the repository's
future v5.5/v6 CI matrix; see `docs/ci.md`.
