# Fabrication Notes

## Plate

The included `case/plate.svg` is a reference plate for two mirrored halves.

Recommended plate materials:

- 1.5 mm FR4
- 1.5 mm aluminum
- 3.0 mm acrylic

Switch cutouts are 14 mm square. Depending on your manufacturing process and switch brand, you may need to tune the cutout between 13.9 mm and 14.1 mm.

## PCB

Recommended PCB design constraints:

- 1.6 mm FR4
- 1 oz copper minimum
- ENIG finish preferred for durability
- MX hot-swap socket footprints
- Per-key diode
- Socketed XIAO RP2040-compatible controller
- Reset button per half
- Optional power switch if adapting to wireless

## PCBA Requirement

For a no-solder user experience, order assembly for:

- 34 hot-swap sockets
- 34 diodes
- 2 reset switches
- 2 controller socket sets
- 2 interconnect connectors

If any of these are left unpopulated, the builder will need soldering or a revised mechanical connector strategy.

## Verification Checklist

- Plate switch centers match the PCB switch footprints.
- Hot-swap sockets do not collide with standoffs.
- Controller USB-C ports are accessible after case assembly.
- Bottom plate clears all SMD components.
- Left and right halves have distinct silkscreen labels.
