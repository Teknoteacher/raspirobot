# 09_rgb_cheer.py
# uses the GPIO pins to control an RGB LED

import RPi.GPIO as GPIO
import time 
import urllib

# set LED pins
red = 16
green = 20
blue = 21

RED = 100, 0, 0
GREEN = 0, 100, 0
BLUE = 0, 0, 100
CYAN = 0, 50, 100
WHITE = 50, 50, 50
WARMWHITE = 100, 100, 100
PURPLE = 50, 0, 100
MAGENTA = 100, 0, 100
YELLOW = 100, 100, 0
ORANGE = 100, 50, 0

# Setup parameters
cheerlights_url = "http://api.thingspeak.com/channels/1417/field/1/last.txt"
colour_map = {"red":RED,
             "green":GREEN,
             "blue":BLUE,
             "cyan":CYAN,
             "white":WHITE,
             "warmwhite":WARMWHITE,
             "purple":PURPLE,
             "magenta":MAGENTA,
             "yellow":YELLOW,
             "orange":ORANGE}



# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
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
time.sleep(1)
print("now")

# Loop indefinitely
while True:
    try:                                                # Attempt the following:
        cheerlights = urllib.urlopen(cheerlights_url)        # Open cheerlights file via URL
        chosen_colour = cheerlights.read()                     # Read the last cheerlights colour
        cheerlights.close()                                 # Close cheerlights file
        colour = colour_map[chosen_colour]               # Get the LedBorg colour to use from the name

        pwmRed.ChangeDutyCycle(colour[0])
        pwmGreen.ChangeDutyCycle(colour[1])
        pwmBlue.ChangeDutyCycle(colour[2])
    except:                                             # If we have an error
        pass                                                # Ignore it (do nothing)
    finally:                                            # Regardless of errors:
        time.sleep(1)                                       # Wait for 1 second 

    # These methods called whenever a slider moves
        # change the led brightness to match the slider
  #      pwmRed.ChangeDutyCycle(float(duty))

 #       pwmGreen.ChangeDutyCycle(float(duty))
    
#        pwmBlue.ChangeDutyCycle(float(duty))

#try:

#except KeyboardInterrupt:  
GPIO.cleanup()

