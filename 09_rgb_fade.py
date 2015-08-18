# 09_rgb_cheer_fader.py
# uses the GPIO pins to fade an RGB LED

import RPi.GPIO as GPIO
import time 

# set LED pins
red = 16
green = 20
blue = 21

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

pwmLED = GPIO.PWM(blue, 100)
pwmLED.start(100)

# Start Pulse Width Modulation (PWM) on the red, green and blue channels to 
# control the brightness of the LEDs.
# Follow this link for more info on PWM: http://en.wikipedia.org/wiki/Pulse-width_modulation
try:
    while True:
        for fade in range(1,60):
            pwmLED.ChangeDutyCycle(fade)
            time.sleep(0.035)
        time.sleep(0.5)
        for fade in range(60,1,-1):
            pwmLED.ChangeDutyCycle(fade)
            time.sleep(0.035)
   
except KeyboardInterrupt:
    GPIO.cleanup()
