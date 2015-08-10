#04_blink4.py
#This program blinks the LEDs randomly at random timed intervals

import time
import random
from rrb2 import *

rr = RRB2()

while True:
    rr.set_led1(random.randint(0,1))
    rr.set_led2(random.randint(0,1))
    time.sleep(random.uniform(0,0.2))
