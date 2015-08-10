#05_switch_binary.py
#This program uses both LEDs as a binary counter

from rrb2 import *
import time

rr = RRB2()
running = False

while True:
    while rr.sw1_closed() == False:
        rr.set_led1(0)
        rr.set_led2(0)
    time.sleep(0.3)
    while rr.sw1_closed() == False:
        rr.set_led1(1)
        rr.set_led2(0)
    time.sleep(0.3)
    while rr.sw1_closed() == False:
        rr.set_led1(0)
        rr.set_led2(1)
    time.sleep(0.3)
    while rr.sw1_closed() == False:
        rr.set_led1(1)
        rr.set_led2(1)
    time.sleep(0.3)



