<<<<<<< HEAD
import board
from mylcd import *

theLCD = myLCD(board.C7, board.D6)

theLCD.displayText("Gay", 0xFFFFFF, 0, 0)

while(True):
    pass
=======
from mylcd import *

theLCD = myLCD(board.D13, board.D12)

theLCD.displayText("Gay", 0xFFFFFF, 0, 0)

while True:
    pass
>>>>>>> 750c0f875adae164ec3f696dd30bc1621118556b
