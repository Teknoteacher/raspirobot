#04_blink3.py
import time
from rrb2 import *

rr = RRB2()

while True:
    rr.set_led1(1)
    rr.set_led2(1)
    time.sleep(0.1)
    rr.set_led1(0)
    rr.set_led2(0)
    time.sleep(0.1)
