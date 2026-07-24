# Flashing KMK

1. Install CircuitPython on both controllers.
2. Copy the KMK library to the `lib` folder on each CIRCUITPY drive.
3. Copy `firmware/kmk/code.py` to the root of each CIRCUITPY drive.
4. Set the handedness flag for each half if you split the firmware into left and right files.
5. Reboot the controller and test the matrix.

The included firmware is a starter file. Update pin assignments after the final PCB schematic is complete.
