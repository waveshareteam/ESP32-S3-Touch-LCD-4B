# ESP32-S3-Touch-LCD-4B Bring-up Checklist

[English](bring-up-checklist.md) | [简体中文](bring-up-checklist_ZH.md)

Complete this checklist for every released hardware revision. Record evidence
in `hardware/` before publishing a value in the README, board support package,
or example configuration.

## Source Material

- [x] Add the released two-page schematic PDF.
- [ ] Add PCB source or manufacturing outputs that are intended for release.
- [ ] Add the BOM and identify do-not-populate parts where applicable.
- [ ] Add the mechanical drawing and connector locations where applicable.
- [ ] Record the product name, PCB marking, and hardware revision.
- [ ] Record source-file tool names and versions.

## Power and Boot

- [ ] Verify every supply rail, enable signal, and power-up dependency.
- [ ] Verify USB connector roles, ESD protection, and USB signal routing.
- [ ] Verify reset, boot, and ESP32-S3 strapping pins.
- [ ] Record safe input voltage and current requirements from released data.

## Memory and Storage

- [ ] Verify flash type, bus mode, and capacity.
- [ ] Verify PSRAM type, bus mode, and capacity.
- [ ] Verify SD-card or other storage pins and shared-bus constraints, if used.

## Display and Touch

- [x] Cross-check the LCD controller, resolution, RGB bus, and active timing constants.
- [x] Cross-check LCD reset, chip-select, command/data, and backlight controls.
- [x] Cross-check the GT911 bus, interrupt, and reset signals used by the BSP/examples.
- [x] Confirm the TCA9554-mediated LCD/touch control assignments.

## Other Peripherals

- [x] Cross-check ES8311/ES7210 clocks, data signals, and amplifier enable used by examples.
- [x] Cross-check QMI8658, PMU, RTC, and GPIO0 assignments used by examples.
- [ ] Identify GPIO conflicts and peripherals that cannot operate concurrently.

## Cross-check

- [ ] Compare the schematic with the PCB source or netlist.
- [x] Compare active pin definitions with the managed BSP header.
- [x] Compare active pin definitions with all first-party examples and the shared Arduino header.
- [ ] Test the affected revision on physical hardware.
- [ ] Update `hardware/HARDWARE_REFERENCE_TEMPLATE.md` and rename it to a
      revision-specific reference when verification is complete.

Completed cross-checks and unresolved evidence are recorded in
[the pin audit](../hardware/pin-audit.md). Checked items above mean a source
cross-check, not electrical or physical-board validation.
