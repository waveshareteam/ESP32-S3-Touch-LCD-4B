# ESP32-S3-Touch-LCD-4B Bring-up Checklist

Complete this checklist for every released hardware revision. Record evidence
in `hardware/` before publishing a value in the README, board support package,
or example configuration.

## Source Material

- [ ] Add the schematic source and a rendered PDF.
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

- [ ] Verify LCD controller, resolution, bus, color format, and timing.
- [ ] Verify LCD reset, chip-select, command/data, and backlight controls.
- [ ] Verify touch controller, address, bus, interrupt, and reset signals.
- [ ] Confirm whether display and touch reset or bus signals are actually shared.

## Other Peripherals

- [ ] Verify audio codec, amplifier, clocks, data signals, and enable pins, if used.
- [ ] Verify sensors, PMU, RTC, buttons, LEDs, and expansion connectors, if used.
- [ ] Identify GPIO conflicts and peripherals that cannot operate concurrently.

## Cross-check

- [ ] Compare the schematic with the PCB source or netlist.
- [ ] Compare hardware files with all BSP headers and managed component defaults.
- [ ] Compare hardware files with every example and shared configuration overlay.
- [ ] Test the affected revision on physical hardware.
- [ ] Update `hardware/HARDWARE_REFERENCE_TEMPLATE.md` and rename it to a
      revision-specific reference when verification is complete.
