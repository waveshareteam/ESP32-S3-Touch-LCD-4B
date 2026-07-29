## Summary

Describe the change and why it is needed.

## Scope

- [ ] Hardware files or pin definitions
- [ ] ESP-IDF example or source firmware
- [ ] Arduino example or bundled library
- [ ] Factory/recovery firmware metadata
- [ ] Documentation or repository maintenance

## Validation

List the exact framework versions, project paths, commands, and hardware
revisions tested. Use repository-relative paths and generic command forms.

| Surface | Version | Project or check | Result |
| --- | --- | --- | --- |
| Repository checks | Python 3 | `python scripts/check_repository.py` | |
| ESP-IDF | | | |
| Arduino-ESP32 | | | |
| Hardware | | | |

## Hardware and BSP Evidence

For board-facing changes, link the schematic, PCB revision, datasheet, or
measurement that supports the change. Describe affected display, touch, audio,
storage, USB, sensor, power, boot, or shared-bus behavior.

## Dependencies and Artifacts

- Managed component changes:
- Local component changes and why they remain local:
- Firmware artifact or flash-layout impact:
- Compatibility impact:

## Checklist

- [ ] Public text contains no local paths, usernames, credentials, or machine-specific details.
- [ ] Changed examples include current build and usage documentation.
- [ ] Pin or board-option changes were checked against hardware evidence.
- [ ] Generated build output and release archives are not committed.
- [ ] Remaining work and intentional CI exclusions are documented.
