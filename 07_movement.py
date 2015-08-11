# 07_movement.py
# Uses the ultrasonic rangefinder to measure changes
from rrb2 import *
import time

rr = RRB2()
reference = rr.get_distance()
rr.set_led1(0)
rr.set_led2(0)

while True:
    time.sleep(1)
    reading = rr.get_distance()
    difference = reading - reference    
    if difference < -1 or difference > 1:
        print("Movement detected")
        for a in range(5):        
            rr.set_led1(1)
            rr.set_led2(1) 
            time.sleep(0.3)
            
            rr.set_led1(0)
            rr.set_led2(0)
            time.sleep(0.3)
