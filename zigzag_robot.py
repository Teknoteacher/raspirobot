
#Sequence Robot

from rrb2 import *
#import time, random

rr = RRB2()

motor_speed = 0.6

rr.forward(4, motor_speed)
rr.right(0.5, motor_speed)
rr.forward(1, motor_speed)
rr.left(0.5, motor_speed)
rr.forward(2, motor_speed)
rr.right(0.5, motor_speed)
rr.forward(2, motor_speed)
rr.left(0.5, motor_speed)
