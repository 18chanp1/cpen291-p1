import time
import board
import adafruit_hcsr04
import pwmio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A3)
piezo = pwmio.PWMOut(board.D10, duty_cycle=0, frequency=440, variable_frequency=True)

print("running")
while True:
    try:
        print(sonar.distance)
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