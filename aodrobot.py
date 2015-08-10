import time 
from rrb2 import *

rr = RRB2()

while True:
    dist = rr.get_distance()
    print(dist)
#    time.sleep(1)
    if dist > 35:
        rr.forward(1)
    if dist < 30:
        rr.left(1) 
