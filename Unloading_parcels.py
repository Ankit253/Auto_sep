# robonox'20 team voltage
# Code of unloading part

import RPi.GPIO
from time import sleep

# motor 1
m1 = 4
#  Motor2
m2 = 14  

# main setup
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor1, GPIO.out)
    GPIO.setup(motor2, GPIO.out)

# Working of motor 
def loop():
    GPIO.output(motor1, HIGH)
    GPIO.output(motor2, LOW)


def forward():
    setup()
    loop()
    sleep(10)
    GPIO.cleanup()
