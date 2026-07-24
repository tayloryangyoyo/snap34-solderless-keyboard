# PCBA Specification

This file defines the manufacturing intent for Snap34. It is not a substitute for a final schematic, PCB layout, or assembly drawing.

## Build Intent

The end user should not need to solder. Any soldered component must be installed by the PCB assembly vendor or supplied as a pre-assembled module.

## Required Assemblies Per Complete Keyboard

| Component | Quantity | Assembly Requirement |
| --- | ---: | --- |
| MX hot-swap socket | 34 | Vendor assembled |
| SMD diode | 34 | Vendor assembled |
| Controller socket/header | 2 sets | Vendor assembled |
| Reset switch | 2 | Vendor assembled |
| Interconnect connector | 2 | Vendor assembled |

## Suggested Electrical Matrix

- 4 rows x 5 columns per half, with unused positions omitted for thumbs.
- Diodes should be oriented consistently row-to-column or column-to-row.
- Firmware starter assumes row-to-column scanning.

## Suggested Controller Pins

Left half:

- Rows: GP0, GP1, GP2, GP3
- Columns: GP4, GP5, GP6, GP7, GP8

Right half:

- Rows: GP0, GP1, GP2, GP3
- Columns: GP4, GP5, GP6, GP7, GP8

The final split transport is intentionally left open. For wired split, use serial over TRRS or USB-C only if the electrical design protects against shorts and hot-plug issues.
