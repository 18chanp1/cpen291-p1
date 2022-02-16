import board
from mylcd import *

theLCD = myLCD(board.C7, board.D6)

theLCD.displayText("Gay", 0xFFFFFF, 0, 0)

while(True):
    pass
