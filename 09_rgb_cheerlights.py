# 09_rgb_cheer.py
# uses the GPIO pins to control an RGB LED

import RPi.GPIO as GPIO
import time 
import urllib

# set LED pins
red = 16
green = 20
blue = 21

# setup a map data structure with the RGB values for the different colours 
cheerlights_url = "http://api.thingspeak.com/channels/1417/field/1/last.txt"
colour_map = {"red":(100,0,0),
             "green":(0,100,0),
             "blue":(0,0,100),
             "cyan":(0,50,100),
             "white":(50,50,50),
             "warmwhite":(100,100,100),
             "purple":(50,0,100),
             "magenta":(100,0,100),
             "yellow":(100,100,0),
             "orange":(100,50,0),
             "pink":(100,0,100),
             "oldlace":(100,100,100)}

# configure the Raspberry Pi to use the Broadcom pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Start Pulse Width Modulation (PWM) on the red, green and blue channels to 
# control the brightness of the LEDs.
# Follow this link for more info on PWM: http://en.wikipedia.org/wiki/Pulse-width_modulation
pwmRed = GPIO.PWM(red, 500)
pwmRed.start(100)
pwmGreen = GPIO.PWM(green, 500)
pwmGreen.start(100)
pwmBlue = GPIO.PWM(blue, 500)
pwmBlue.start(100)

# repeat until interrupted 
try:
    while True:
        cheerlights = urllib.urlopen(cheerlights_url)# Open cheerlights file via URL
        chosen_colour = cheerlights.read()           # Read the last cheerlights colour
        cheerlights.close()                          # Close cheerlights file

        pwmRed.ChangeDutyCycle(colour_map[chosen_colour][0])
        pwmGreen.ChangeDutyCycle(colour_map[chosen_colour][1])
        pwmBlue.ChangeDutyCycle(colour_map[chosen_colour][2])
        time.sleep(0.5)
except:                                              # if there is an error
        pass                                         # ignore error (do nothing)
finally:                                             # then no matter what happens
        time.sleep(1)                                # wait 1 second 

GPIO.cleanup()

