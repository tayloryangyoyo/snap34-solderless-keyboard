import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

# Starter pin map for a XIAO RP2040-compatible controller.
# Update these pins to match the final PCB.
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.col_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

LOWER = KC.MO(1)
RAISE = KC.MO(2)

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.Z, KC.X, KC.C, KC.V, KC.B,
        KC.NO, KC.NO, KC.NO, LOWER, KC.SPC,
    ],
    [
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
        KC.TAB, KC.LCTL, KC.LALT, KC.LGUI, KC.ESC,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.TRNS, KC.ENT,
    ],
    [
        KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,
        KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.BSPC,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.DEL, KC.TRNS,
    ],
]

if __name__ == "__main__":
    keyboard.go()
