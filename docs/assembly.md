# Assembly Guide

## Tools

- Small Phillips screwdriver
- Keycap puller
- Switch puller
- USB-C cable
- Optional: tweezers for controller reset buttons

No soldering iron is required when the PCB has been assembled by the board vendor.

## Steps

1. Inspect both PCBs.
   - Confirm all hot-swap sockets are installed.
   - Confirm all diodes are installed in the same orientation shown by the PCB silkscreen.
   - Confirm controller sockets are installed and straight.

2. Install standoffs on the bottom plates.
   - Use six M2 standoffs per half.
   - Keep screws snug, not overtightened.

3. Place each PCB on its bottom plate.
   - Align the controller end and switch grid.
   - Check that no component touches a screw head.

4. Add the top plates.
   - The switch cutouts should sit directly above the hot-swap sockets.
   - Do not force the plate if a socket or component is misaligned.

5. Press in switches.
   - Support the hot-swap socket area from below.
   - Insert switches straight down.
   - If a switch leg bends, remove the switch and straighten the leg before trying again.

6. Install controllers.
   - Match the USB-C side and pin-1 orientation from the PCB marking.
   - Press evenly into the sockets.

7. Flash firmware.
   - Copy `firmware/kmk/code.py` to the CIRCUITPY drive for each half.
   - Adjust handedness and pins if your final PCB differs from the reference matrix.

8. Test every key.
   - Use an online keyboard tester or a local text editor.
   - If one key fails, inspect the switch pins and hot-swap socket.
   - If an entire row or column fails, inspect the controller seating.

## Safety Notes

- Do not connect or disconnect the interconnect cable while powered if using TRRS.
- Do not force switches into the sockets.
- Confirm controller orientation before plugging in USB.
