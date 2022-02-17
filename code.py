"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm_l_foot = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm_r_foot = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
pwm_l_leg = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
pwm_r_leg = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)

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

def stuttered_twist(loops):
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

while(true):
       split(5);
       time.sleep(2);
       sleep(5);
       time.sleep(2);

