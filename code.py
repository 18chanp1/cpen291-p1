"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import adafruit_hcsr04
from adafruit_motor import servo
from mylcd import *

# create a PWMOut object on Pin A2.
pwm_l_foot = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
pwm_r_foot = pwmio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)
pwm_l_leg = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm_r_leg = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
l_foot = servo.Servo(pwm_l_foot)
r_foot = servo.Servo(pwm_r_foot)
l_leg = servo.Servo(pwm_l_leg)
r_leg = servo.Servo(pwm_r_leg)

#REMEMBER SERVOS ARE BY DEFAULT AT 90

#move legs in straight line, lift feet
def split(loops):
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

def leg_twist(loops):
    for i in range(loops):
        for angle in range(90, 0, -5):  #shift legs inward
            l_leg.angle = angle
            r_leg.angle = 180 - angle
            time.sleep(0.05)

        for angle in range(0, 90, 5):  #shift legs outward
            l_leg.angle = angle
            r_leg.angle = 180 - angle
            time.sleep(0.05)

        time.sleep(0.5)

def foot_twist(loops):
    for i in range(loops):
        for angle in range(90, 0, -5):  #shift feet inward
            l_foot.angle = angle
            r_foot.angle = 180 - angle
            time.sleep(0.05)

        for angle in range(0, 90, 5):  #shift feet outward
            l_foot.angle = angle
            r_foot.angle = 180 - angle
            time.sleep(0.05)

        time.sleep(0.5)
        
def robot_move(loops):
    # lift foot to vertical, spin out and back, drop foot to horizontal 
    for i in range(loops):
        for angle in range(90, 0, -5):
            l_foot.angle = angle
            time.sleep(0.05)
            r_foot.angle = angle
            time.sleep(0.05)
            r_leg.angle = angle
            time.sleep(0.05)
            l_leg.angle = angle
    for i in range(loops):
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

def step_forward(steps):
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

def step_backward(steps):
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
    

#LCD Display
theLCD = myLCD(board.D13, board.D12)
theLCD.displayText("Gay", 0xFFFFFF, 0, 0)

#Sensor and Buzzer
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A3)
piezo = pwmio.PWMOut(board.D10, duty_cycle=0, frequency=440, variable_frequency=True)


while(True):
    try:
        X = sonar.distance
        if X >= 0:
            piezo.duty_cycle = 0
        if X < 10 and X >= 5:
            piezo.frequency = 392
            piezo.duty_cycle = 65535 // 10
        if X < 5:
            piezo.frequency = 523
            piezo.duty_cycle = 65535 // 10
    except RuntimeError:
        print("Retrying!")
        piezo.duty_cycle = 0

    time.sleep(0.1)
    
  
