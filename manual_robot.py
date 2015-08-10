# Attach: SR-04 Range finder, switch on SW1, and of course motors.

# The switch stops and starts the robot

from rrb2 import *
#import time, random
import sys
import tty
import termios

rr = RRB2()

motor_speed = 0.6

# if you dont have a switch, change the value below to True
running = False

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

# End of the functions that read your keyboard

while True:
    keyp = readkey()
    if keyp == UP:
        rr.forward(1, motor_speed)
        print 'forward'
    elif keyp == DOWN:
        rr.reverse(1, motor_speed)
        print 'backward'
    elif keyp == RIGHT:
        rr.right(1, motor_speed)
        print 'clockwise'
    elif keyp == LEFT:
        rr.left(1, motor_speed)
        print 'anti clockwise'

    elif keyp == 'q':
        motor_speed = 1
        print 'fast', speed
    elif keyp == 'a':
        motor_speed = 0.6
        print 'slow', speed

    elif keyp == ' ':
        rr.stop()
        print 'stop'
    elif ord(keyp) == 3:
        break
