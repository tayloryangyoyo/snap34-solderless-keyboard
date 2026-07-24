# Solderless 3D-Printed Keyboard Concept

This repository is a concept space for a keyboard that can be built without soldering.

The idea is simple: use 3D-printed parts for the body and switch plate, then combine them with off-the-shelf keyboard parts that already have connectors, sockets, or screw terminals. The goal is not to design a full PCB from scratch. The goal is to make a keyboard that a hobbyist can assemble with printed parts, screws, switches, keycaps, and ready-made electronic modules.

## Concept

Most DIY keyboards require soldering switches, diodes, controllers, or wires. This concept avoids that by using parts that can be plugged, screwed, clipped, or pressed together.

Possible approaches:

- Use a prebuilt hot-swap keyboard PCB or hot-swap macro pad PCB.
- Use hot-swap switch sockets mounted into a 3D-printed plate or carrier.
- Use a ready-made microcontroller board with USB-C.
- Use jumper wires, screw terminals, or pre-crimped cables instead of soldered wires.
- Use 3D-printed brackets to hold modules in place.
- Use screws, heat-set inserts, magnets, or clips for the case.

## Repository Structure

- `README.md` - the main concept and build direction
- `3d/` - place for Fusion 360 files, STEP files, STL files, renders, and 3D reference images
- `LICENSE` - license for the concept notes and files

## Parts Direction

This project should prefer parts that are easy to buy and do not require custom electronics manufacturing.

Examples:

- MX-compatible mechanical switches
- Keycaps
- Hot-swap sockets or a prebuilt hot-swap PCB
- A USB-C microcontroller board
- Pre-crimped jumper wires
- Screw terminal blocks
- M2 or M3 screws
- Heat-set inserts
- Rubber feet
- 3D-printed case and plate parts

## Build Direction

1. Design the keyboard shell and switch plate in Fusion 360.
2. 3D print the case, plate, and any brackets needed to hold modules.
3. Install heat-set inserts or use self-tapping screws.
4. Press switches into the printed plate or hot-swap PCB.
5. Mount the ready-made electronics inside the case.
6. Connect modules with plug-in cables, jumper wires, or screw terminals.
7. Close the case and test the keyboard.

## Design Notes

- The 3D model should leave enough room for switch pins, sockets, wires, and connectors.
- The case should make the electronics easy to remove and replace.
- The design should avoid glue where possible.
- The first prototype can be chunky. Reliability matters more than thinness.
- If a part normally needs soldering, look for a pre-soldered version or a connector-based alternative.

## 3D Files

Put future Fusion 360, STEP, STL, and render files in `3d/`.

Suggested file names:

- `keyboard-concept.f3d`
- `keyboard-case.step`
- `keyboard-case.stl`
- `plate.stl`
- `module-bracket.stl`
- `render-front.png`
- `render-exploded.png`

## Status

This is an early concept repository. It is meant to collect the idea, structure, and future 3D design files before becoming a finished build guide.
