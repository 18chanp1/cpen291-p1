import time
import board
import pwmio
import adafruit_hcsr04
from adafruit_motor import servo
from mylcd import *
from ticTacToe import *
import adafruit_matrixkeypad
import digitalio
#for command no more


# create a PWMOut object on Pin A2.
pwm_l_foot = pwmio.PWMOut(board.SDA, duty_cycle=2 ** 15, frequency=50)
pwm_r_foot = pwmio.PWMOut(board.TX, duty_cycle=2 ** 15, frequency=50)
pwm_l_leg = pwmio.PWMOut(board.SCL, duty_cycle=2 ** 15, frequency=50)
pwm_r_leg = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
l_foot = servo.Servo(pwm_l_foot)
r_foot = servo.Servo(pwm_r_foot)
l_leg = servo.Servo(pwm_l_leg)
r_leg = servo.Servo(pwm_r_leg)

#REMEMBER SERVOS ARE BY DEFAULT AT 90

#move legs in straight line, lift feet
def ankle(loops):
    theLCD.refresh()
    theLCD.displayBMP("/images/M1-Split.bmp")
    for i in range(loops):
        for angle in range(90, 0, -5):  #don't remember which way it rotates
            l_leg.angle = angle
            time.sleep(0.05)
        for angle in range(90, 180, 5):
            r_leg.angle = angle
            time.sleep(0.05)

        for angle in range(90, 45, -5):  #don't remember which way it rotates
            l_foot.angle = angle
            time.sleep(0.05)
        for angle in range(90, 135, 5):
            r_foot.angle = angle
            time.sleep(0.05)

        time.sleep(0.5)

        for angle in range(45, 90, 5):  #don't remember which way it rotates
            l_foot.angle = angle
            time.sleep(0.05)
        for angle in range(135, 90, -5):
            r_foot.angle = angle
            time.sleep(0.05)

        for angle in range(0, 90, 5):  #don't remember which way it rotates
            l_leg.angle = angle
            time.sleep(0.05)
        for angle in range(180, 90, -5):
            r_leg.angle = angle
            time.sleep(0.05)

        time.sleep(0.5)

    theLCD.refresh()
    theLCD.displayBMP("/images/S0.bmp")

def right_twist(loops):
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


#LCD Display
theLCD = myLCD(board.D13, board.D12)
theLCD.displayBMP("/images/S0.bmp")


#Sensor and Buzzer
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A3, echo_pin=board.A2)
piezo = pwmio.PWMOut(board.D10, duty_cycle=0, frequency=440, variable_frequency=True)

#Keypad
cols = [digitalio.DigitalInOut(x) for x in (board.D2, board.D7, board.D9)]
rows = [digitalio.DigitalInOut(x) for x in (board.A5, board.A4, board.A1, board.A0)]
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
move_dict = {1: lambda x: all_moves(x), 2: lambda x: step_backward(x),
			 3: lambda x: step_forward(x), 4: lambda x: robot_move(x), 
			 5: lambda x: ankle(x), 6: lambda x: right_twist(x), 
			 7: lambda x: left_twist(x), 8: lambda x: playTTT(keypad),
             9: lambda x: rangefinder(keypad)}

"""
starts a game of tic-tac-toe
@param keyInput - contains the matrix keypad object which interfaces with the keypad
"""
def playTTT(keyInput: adafruit_matrixkeypad):
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
"""
Starts the rangefinder mode, which displays the distance detected by the sonar
sensor on the LCD. Press any key to exit.

@:param keyInput - the keypad used to detect any exit requests. 
"""
def rangefinder(keyInput: adafruit_matrixkeypad):
    theLCD.refresh()
    theLCD.displayBMP("/images/R0.bmp")
    theLCD.displayText("Press any key to exit", 0xffffff, 20, 120)
    theLCD.displayText("", 0xffffff, 30, 90)

    while(not keyInput.pressed_keys()):
        theLCD.popElement()
        dist = sonar.distance
        theLCD.displayText(str(round(dist, 2)), 0xfffff0, 20,90)
        time.sleep(0.2)

    theLCD.refresh()
    theLCD.displayBMP("images/S0.bmp")


while(True):
    try:
        X = sonar.distance
        if X >= 20:
            piezo.duty_cycle = 0
        if X < 20 and X >= 10:
            piezo.frequency = 392
            piezo.duty_cycle = 65535 // 10
        if X < 10:
            piezo.frequency = 523
            piezo.duty_cycle = 65535 // 10

    except RuntimeError:
        print("Retrying!")
        piezo.duty_cycle = 0

    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)
        if(int(keys[0]) == 0):
            break
        else:
            move_dict[int(keys[0])](2)          #repeat movement twice
    time.sleep(0.2)


