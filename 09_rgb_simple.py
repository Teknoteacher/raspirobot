# 09_rgb_simple.py
# Uses the GPIO to turn on the RGB LED colours

import RPi.GPIO as GPIO
import time

red = 16
green = 20
blue = 21


# GPIO Setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    for colour in [red,green,blue]:
        GPIO.output(colour, 1)
        time.sleep(1)
        GPIO.output(colour, 0)
except KeyboardInterrupt: 
    GPIO.cleanup()
