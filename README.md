# Snap34 Solderless Keyboard

Snap34 is a compact 34-key split ergonomic keyboard design intended for builders who want a custom keyboard without hand soldering.

The no-solder build path assumes the PCB is ordered with assembly service: hot-swap sockets, diodes, reset switches, TRRS or USB-C interconnect parts, and controller sockets are populated by the board house. The builder only presses switches into the plate, installs stabilizing hardware, plugs in the controllers, and flashes firmware.

## Goals

- 34 keys, split ergonomic layout
- MX-compatible hot-swap switches
- No hand soldering for the end user
- KMK firmware starter layout
- Simple acrylic or FR4 sandwich case
- Easy-to-audit matrix and manufacturing notes

## Repository Contents

- `docs/bom.md` - parts list and no-solder sourcing notes
- `docs/assembly.md` - assembly steps for the solderless build
- `docs/fabrication.md` - PCB and plate fabrication notes
- `hardware/matrix.csv` - row/column map
- `hardware/keyboard-layout.json` - Keyboard Layout Editor compatible layout
- `hardware/pcba-spec.md` - assembly-service requirements
- `case/plate.svg` - laser-cut or CNC plate reference
- `firmware/kmk/code.py` - KMK starter firmware

## Layout

Each half has 17 keys:

- 5 columns x 3 rows for fingers
- 2 thumb keys
- Mirrored left/right halves

The default keymap is QWERTY with two layer keys on the thumbs.

## No-Solder Build Path

1. Order the PCB with SMT and through-hole assembly where available.
2. Ask the assembler to populate all hotswap sockets, diodes, reset switches, and controller sockets.
3. Use a socketed controller such as a XIAO RP2040-compatible module.
4. Press MX switches through the plate into the hotswap sockets.
5. Plug in keycaps and flash KMK.

If you order bare PCBs, this is no longer a solderless build.

## License

This design is published under the MIT License. Hardware dimensions are provided as a starter reference; verify footprints, clearances, and fabrication constraints before manufacturing.
