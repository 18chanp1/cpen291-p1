import time
import pwmio
import board


# Define a list of tones/music notes to play.
tones = {
"A": 262, "B": 294, "C": 330, "D": 349, "E": 392, "F": 440, "G": 494
}

piezo = pwmio.PWMOut(board.D10, duty_cycle=0, frequency=440, variable_frequency=True)

song = ["A","B","C","C","D","B","A", "G", "P", "P", "A", "A", "B", "C", "A", "P", "G", "G", "G", "D"]

def playtone(frequency):
    piezo.duty_cycle = 65535 // 10
    piezo.frequency = frequency

def bequiet():
    piezo.duty_cycle = 0

def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P"):
            bequiet()
            time.sleep(0.3)
        else:
            playtone(tones[mysong[i]])
            time.sleep(0.3)
            bequiet()
            time.sleep(0.02)
    bequiet()

while True:
    playsong(song)