import time
import digitalio
import board
import adafruit_matrixkeypad

cols = [digitalio.DigitalInOut(x) for x in (board.D2, board.D7, board.D9)]
rows = [digitalio.DigitalInOut(x) for x in (board.A5, board.A4, board.A1, board.A0)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
    time.sleep(0.2)