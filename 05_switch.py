#05_switch.py
#If switch is pressed, both LEDs will light for one second.

from rrb2 import *
import time

rr = RRB2()
running = False

while True:
    if rr.sw1_closed():
        running = not running
    if running:
        rr.set_led1(1)
        rr.set_led2(1)    
    if not running:
        rr.set_led1(0)
        rr.set_led2(0)
    time.sleep(0.3)
