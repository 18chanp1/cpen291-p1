# import relevant files, packages, and libraries
import time
import board
import pwmio
import adafruit_hcsr04
from adafruit_motor import servo
import adafruit_matrixkeypad
import digitalio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R
import random


# Servo Motor and Dance moves
"""
This section contains the LCD information
COMMON PINS:
    GND -> Ged Rail
    POWER -> Red Rail
UNIQUE PINS:
    LEFT FOOT -> SDA
    RIGHT FOOT -> TX
    LEFT LEG -> SCL
    RIGHT LEG -> D5
"""

# create PWMOut objects for the motors using SDA, TX, SCL, D5
pwm_l_foot = pwmio.PWMOut(board.SDA, duty_cycle=2 ** 15, frequency=50)
pwm_r_foot = pwmio.PWMOut(board.TX, duty_cycle=2 ** 15, frequency=50)
pwm_l_leg = pwmio.PWMOut(board.SCL, duty_cycle=2 ** 15, frequency=50)
pwm_r_leg = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create servo objects for each movable parts, default at 90 degrees
l_foot = servo.Servo(pwm_l_foot)
r_foot = servo.Servo(pwm_r_foot)
l_leg = servo.Servo(pwm_l_leg)
r_leg = servo.Servo(pwm_r_leg)

#------ DANCE MOVES ------#

#move legs in straight line, lift feet
def ankle(loops):
    theLCD.refresh()
    theLCD.displayBMP("/images/M1-Split.bmp")
    for i in range(loops):
        for angle in range(90, 0, -5):
            
            l_leg.angle = angle
            time.sleep(0.05)
        for angle in range(90, 180, 5):
            
            r_leg.angle = angle
            time.sleep(0.05)

        for angle in range(90, 45, -5):
            
            l_foot.angle = angle
            time.sleep(0.05)
        for angle in range(90, 135, 5):
            
            r_foot.angle = angle
            time.sleep(0.05)

        
        time.sleep(0.5)

        for angle in range(45, 90, 5):
            
            l_foot.angle = angle
            time.sleep(0.05)
        for angle in range(135, 90, -5):
            
            r_foot.angle = angle
            time.sleep(0.05)

        for angle in range(0, 90, 5):
            
            l_leg.angle = angle
            time.sleep(0.05)
        for angle in range(180, 90, -5):
            
            r_leg.angle = angle
            time.sleep(0.05)

        
        time.sleep(0.5)

    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")

def right_twist(loops):
    theLCD.ee += 2
    theLCD.refresh()
    theLCD.displayBMP("/images/M2-LegTwist.bmp")
    for i in range(loops):
        for angle in range(90, 0, -5):  #shift legs inward
            l_leg.angle = angle
            r_leg.angle = angle
            time.sleep(0.05)

        for angle in range(0, 90, 5):  #shift legs outward
            l_leg.angle = angle
            r_leg.angle = angle
            time.sleep(0.05)

        time.sleep(0.5)
    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")

def left_twist(loops):
    theLCD.refresh()
    theLCD.displayBMP("/images/M3-FootTwist.bmp")
    for i in range(loops):
        for angle in range(90, 0, -5):  #shift feet inward
            l_foot.angle = angle
            r_foot.angle = angle
            time.sleep(0.05)

        for angle in range(0, 90, 5):  #shift feet outward
            l_foot.angle = angle
            r_foot.angle = angle
            time.sleep(0.05)

        time.sleep(0.5)

    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")

def robot_move(loops):
    # lift foot to vertical, spin out and back, drop foot to horizontal
    theLCD.refresh()
    theLCD.displayBMP("/images/M4-RobotMove.bmp")
    for i in range(loops):
        for angle in range(90, 0, -5):
            l_foot.angle = angle
            time.sleep(0.05)
            r_foot.angle = angle
            time.sleep(0.05)
            r_leg.angle = angle
            time.sleep(0.05)
            l_leg.angle = angle
    #for i in range(loops):
        for angle in range(0, 90, 5):
            r_leg.angle = angle
            time.sleep(0.05)
            l_leg.angle = angle
            time.sleep(0.05)
            l_foot.angle = angle
            time.sleep(0.05)
            r_foot.angle = angle
            time.sleep(0.05)
    time.sleep(0.5)

    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")

def step_forward(steps):
    theLCD.refresh()
    theLCD.displayBMP("/images/M5-StepForward.bmp")
    for i in range(steps):
        if steps % 2 == 0:
            for angle in range(90, 45, -5):
                r_foot.angle = angle
                time.sleep(0.05)
            for angle in range(90, 0, -5):
                r_leg.angle = angle
                time.sleep(0.05)
            for angle in range(45, 90, 5):
                r_foot.angle = angle
                time.sleep(0.05)
            for angle in range(0, 90, 5):
                r_leg.angle = angle
                time.sleep(0.05)
        else:
            for angle in range(90, 45, -5):
                l_foot.angle = angle
                time.sleep(0.05)
            for angle in range(90, 0, -5):
                l_leg.angle = angle
                time.sleep(0.05)
            for angle in range(45, 90, 5):
                l_foot.angle = angle
                time.sleep(0.05)
            for angle in range(0, 90, 5):
                l_leg.angle = angle
                time.sleep(0.05)
    time.sleep(0.5)

    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")

def step_backward(steps):
    # theLCD.refresh()
    theLCD.displayBMP("/images/M6-StepBackward.bmp")
    for i in range(steps):
        if steps % 2 == 0:
            for angle in range(90, 45, -5):
                r_foot.angle = angle
                time.sleep(0.05)
            for angle in range(90, 180, 5):
                r_leg.angle = angle
                time.sleep(0.05)
            for angle in range(45, 90, 5):
                r_foot.angle = angle
                time.sleep(0.05)
            for angle in range(180, 90, -5):
                r_leg.angle = angle
                time.sleep(0.05)
        else:
            for angle in range(90, 45, -5):
                l_foot.angle = angle
                time.sleep(0.05)
            for angle in range(90, 180, 5):
                l_leg.angle = angle
                time.sleep(0.05)
            for angle in range(45, 90, 5):
                l_foot.angle = angle
                time.sleep(0.05)
            for angle in range(180, 90, -5):
                l_leg.angle = angle
                time.sleep(0.05)
    time.sleep(0.5)

    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")


def all_moves(loops):
	step_backward(loops)
	time.sleep(0.5)

	step_forward(loops)
	time.sleep(0.5)

	robot_move(loops)
	time.sleep(0.5)

	left_twist(loops)
	time.sleep(0.5)

	right_twist(loops)
	time.sleep(0.5)

#------ LCD CLASS ------#
"""
This section contains the LCD information
PINS:
    3-5V Vin -> 3V
    GND -> GND
    SCK -> SCK
    SO -> MI
    MO/SI -> MO.
    TCS -> SPI Chip Select Pin. C7, No.13
    D/C -> SPI data/command select pin. D6, No12. 
    RST -> RST
"""

"""
A class to easily display common elements on the LCD. 
"""

# LCD Class
class myLCD:
    """
    Initialize LCD instance
    @:param chipSelect - pin for chipSelect (e.g. board.D13), pin 13
    @:param spiData - pin for spiData (e.g. board.D12), pin 12
    """
    def __init__(self, chipSelect, spiData) -> None:
        # Release any resources currently in use for the displays
        displayio.release_displays()

        spi = board.SPI()
        tft_cs = chipSelect
        tft_dc = spiData

        display_bus = displayio.FourWire(
            spi, command=tft_dc, chip_select=tft_cs, reset=board.D11
        )

        self.display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

        # Make the display context
        self.splash = displayio.Group()
        self.display.show(self.splash)
        self.time = time.time()
        self.ee = 1
    
    """
    refreshes the screen with a blank slate
    """
    def refresh(self):
        self.splash = displayio.Group()
        self.display.show(self.splash)
    """
    displays text on the lcd
    intext - text to display
    incolor - color in hex
    inx - x coordinate of the display
    iny - y coordinate of the display
    """
    def displayText(self, intext, incolor, inx, iny):
        color_bitmap = displayio.Bitmap(128, 128, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0x000000  # Black

        text_area = label.Label(terminalio.FONT, text = intext, color = incolor, x=inx, y=iny)
        self.splash.append(text_area)

    """
    displays a bitmap image. 
    location - directory of bmp file
    """
    def displayBMP(self, location):
        with open(location, "rb") as bitmap_file:

            # Setup the file as the bitmap data source
            bitmap = displayio.OnDiskBitmap(bitmap_file)

            # Create a TileGrid to hold the bitmap
            tile_grid = displayio.TileGrid(
                bitmap,
                pixel_shader=getattr(bitmap, 'pixel_shader', displayio.ColorConverter())
            )

            # Add the TileGrid to the Group
            self.splash.append(tile_grid)

            time.sleep(0.1)

    """
    displays the time since the LCD has started running, in seconds, on the screen
    @:param incolor - the color of the text. 
    """
    def displayTime(self, incolor):
        currentTime = time.time()
        theLocal = "Time running: " + str(currentTime - self.time) + "s"
        self.displayText(theLocal, incolor, 5, 110)

    """
    Removes the last element appended to the LCD group.
    """
    def popElement(self):
        self.splash.pop()

    def EE(self):
        self.refresh()
        self.displayBMP("images/E0.bmp")

        time.sleep(3)

        self.refresh()
        self.displayBMP("images/S0.bmp")

# LCD Display
theLCD = myLCD(board.D13, board.D12)
theLCD.displayBMP("/images/S0.bmp")


#------ SENSOR AND BUZZER ------#
"""
SENSOR PINS:
    TRIGGER -> A3
    ECHO -> A2
    GND -> GND
    
BUZZER PINS:
    GND -> GND
    OUTPUT -> D10
"""
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A3, echo_pin=board.A2)
piezo = pwmio.PWMOut(board.D10, duty_cycle=0, frequency=440, variable_frequency=True)


"""
Starts the rangefinder mode, which displays the distance detected by the sonar
sensor on the LCD. Press any key to exit.

@:param keyInput - the keypad used to detect any exit requests. 
"""


def rangefinder(keyInput: adafruit_matrixkeypad):
    theLCD.ee += 1
    theLCD.refresh()
    theLCD.displayBMP("/images/R0.bmp")
    theLCD.displayText("Hold any key \n to exit", 0xffffff, 30, 105)
    theLCD.displayText("", 0xffffff, 30, 90)

    time.sleep(0.3)

    while (True):
        if keyInput.pressed_keys:
            break
        theLCD.popElement()
        try:
            dist = sonar.distance
            theLCD.displayText(str(dist) + " cm", 0xfffff0, 30, 80)
        except:
            theLCD.displayText("Out of range", 0xfffff0, 30, 80)

        time.sleep(0.2)

    theLCD.refresh()
    theLCD.displayBMP("images/S0.bmp")
    
#------ KEYPAD ------#
"""
KEYPAD PINS:
    ROWS: 
        1 -> D2
        2 -> D7
        3 -> D9
    COLS:
        1 -> A5
        2 -> A4
        3 -> A1
        4 -> A0
"""
cols = [digitalio.DigitalInOut(x) for x in (board.D2, board.D7, board.D9)]
rows = [digitalio.DigitalInOut(x) for x in (board.A5, board.A4, board.A1, board.A0)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

#Keys 1-7 = dance moves, 8 = tic tac toe, 9 = range finder
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
move_dict = {1: lambda x: all_moves(x), 2: lambda x: step_backward(x),
			 3: lambda x: step_forward(x), 4: lambda x: robot_move(x), 
			 5: lambda x: ankle(x), 6: lambda x: right_twist(x), 
			 7: lambda x: left_twist(x), 8: lambda x: playTTT(keypad),
             		 9: lambda x: rangefinder(keypad)}

#------ TIC TAC TOE ON LCD ------#
"""
The TIC TAC Toe Mode can be enabled by pressing 0. 
Tic tac toe class contains the tic tac toe object 
and relevant functions to play the game (modified from lab 1)
"""
class TicTacToe:
    def __init__(self, lcdDisplay: myLCD, inpad:adafruit_matrixkeypad): # Use as is
        """ initializes data fields (board and played)
            and prints the banner messages
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell,
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells
        self.display = lcdDisplay
        self.keypad = inpad
        self.boardPrinted = False
        self.display.refresh()
        self.display.displayText("Tic-Tac-Toe! \n", 0xffffff, 5,5)
        self.printBoard()
        self.boardPrinted = False

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        if(self.boardPrinted):
            self.display.popElement
        

        r1c1 = f"   {self.board[0]} | {self.board[1]} | {self.board[2]}\n"    # prints first row of game board
        r1c2 = ""                                                     # prints board labels on first row
        r2 = "   --+---+--\n"                                          # prints the row separators in board

        r3c1 = f"   {self.board[3]} | {self.board[4]} | {self.board[5]}\n"   # prints second row of game board
        r3c2 = ""                                                  # prints board labels on second row
        r4 = "   --+---+--\n"                                          # prints row separators

        r5c1 = f"   {self.board[6]} | {self.board[7]} | {self.board[8]}\n"   # prints third row of game board
        r5c2 = ""                                                    # prints board labels on third row

        self.display.displayText(r1c1 + r1c2 + r2 + r3c1 + r3c2 + r4 + r5c1 + r5c2, 0xffffff, 5, 25)
        self.boardPrinted = True

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number;
            error checks that the input is a valid cell number;
            and prints the info and the updated self.board;
        """
        validInput = False             # set valid to false so user will be prompted on first run
        displayedWarning = False
        time.sleep(1)



        while not validInput:       # keep prompting while input is invalid               # check that input is an integer - no exceptions when casting.
            while True:
                if self.keypad.pressed_keys:
                    move = self.keypad.pressed_keys[0] - 1
                    break
            
            if (not isinstance(move, int)) or self.played.__contains__(move) or move < 0:
                if not displayedWarning:
                    self.display.displayText("invalid input", 0xfffff0, 5, 110)
                    displayedWarning = True
                time.sleep(0.3)
                
            else: 
                if displayedWarning:
                    self.display.popElement()
                self.display.popElement()
                self.board[move] = 'X'
                self.played.add(move)
                self.printBoard()
                validInput = True


    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell,
            and prints the info and the updated self.board
        """
        valid = False                                   # valid is false so computer can generate random cell on board

        while not(valid):                             # keep generating random cells from 0-8 until generated cell
            move = random.randint(0, 8)                 # is not taken

            if not (self.played.__contains__(move)):  # if random cell selected has not been used, computer chooses
                self.played.add(move)
                self.board[move] = 'O'
                self.printBoard()
                valid = True                            # move is valid and exit loop
            else:
                continue                                # keep looping until valid move is generated by random int
                                                        # selector

    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        whoWins = False         # set self as not won as default

        # check whether self wins by vertical columns, and set selfWon to true if who won.
        for x in range(3):
            if self.board[x] == who and self.board[x+3] == who and self.board[x+6] == who:
                whoWins = True
        # check whether self wins by horizontal rows and set selfWon to true if who won.
        for y in range(0, 9, 3):
            if self.board[y] == who and self.board[y+1] == who and self.board[y+2] == who:
                whoWins = True
        # check whether self wins by diagonals and set selfWon to true if who won.
        if self.board[0] == who and self.board[4] == who and self.board[8] == who:
            whoWins = True
        if self.board[2] == who and self.board[4] == who and self.board[6] == who:
            whoWins = True

        # return true if any of the win conditions are satisfied above. Otherwise, returns false
        return whoWins

    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or
                 "You lost! Thanks for playing." or
                 "A draw! Thanks for playing."
        """

        # determines whether board is completely full. Returns true if completely full. False otherwise.
        allFilled = True
        for i in range(0,9):
            if self.board[i] == ' ':
                allFilled = False

        # if board is full and no one has the winning condition, set tie to true. Otherwise, false.
        tie = not(self.hasWon('X')) and not(self.hasWon('O')) and allFilled

        # prints corresponding message based on players/computer winning condition and spec.
        if tie:
            self.display.displayText("A draw!", 0xfffff, 10, 110)
            return True    # returns true for a tie

        if self.hasWon('X'):
            self.display.displayText("You won! ", 0xfffff, 10, 110)
        elif self.hasWon('O'):
            self.display.displayText("You lost!", 0xfffff, 10, 110)

        # returns value depending on whether "who" wins or not based on spec.
        if self.hasWon(who):
            return True
        else:
            return False

def playTTT(keyInput: adafruit_matrixkeypad):
    """
        starts a game of tic-tac-toe
        @param keyInput - contains the matrix keypad object which interfaces with the keypad
    """
    theLCD.refresh()
    ttt = TicTacToe(theLCD, keyInput)  # initialize a game
    while True:
        ttt.playerNextMove()  # X starts first
        if (ttt.terminate('X')): break  # if X won or a draw, print message and terminate
        ttt.computerNextMove()  # computer plays O
        if (ttt.terminate('O')): break  # if O won or a draw, print message and terminate

    print("finish ttt")
    time.sleep(3)
    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")


#------ MAIN LOOP ------#

while(True):
    
    # make a buzzer noise based on distance from object in front
    try:
        X = sonar.distance
        if X >= 20:
            piezo.duty_cycle = 0
        if X < 20 and X >= 10:
            piezo.frequency = 392
            piezo.duty_cycle = 65535 // 10
        if X < 10:
            piezo.frequency = 784
            piezo.duty_cycle = 65535 // 10
            theLCD.displayBMP("/images/P0.bmp")
            time.sleep(3)
            theLCD.displayBMP("images/S0.bmp")
    except RuntimeError:
        piezo.duty_cycle = 0
        
    keys = keypad.pressed_keys
    if keys:
        if(int(keys[0]) == 0): #terminate program with key 0
            break
        else:
            # move_dict is a list of functions (returned from closures)
            move_dict[int(keys[0])](2)  #repeat movement twice if selected
    time.sleep(0.2)

    if theLCD.ee % 3 == 1 and theLCD.ee != 1:
        theLCD.ee = 0
        theLCD.EE()
