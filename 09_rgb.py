# 09_rgb.py
# uses the GPIO pins to control an RGB LED

import RPi.GPIO as GPIO
import time 

red = 16
green = 20
blue = 21

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
pwmRed.ChangeDutyCycle(0)
pwmGreen.ChangeDutyCycle(100)
pwmBlue.ChangeDutyCycle(0)
time.sleep(1)
    # These methods called whenever a slider moves
        # change the led brightness to match the slider
  #      pwmRed.ChangeDutyCycle(float(duty))

 #       pwmGreen.ChangeDutyCycle(float(duty))
    
#        pwmBlue.ChangeDutyCycle(float(duty))

#try:
time.sleep(1)

#except KeyboardInterrupt:  
GPIO.cleanup()

