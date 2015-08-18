from rrb2 import *
from bottle import route, run, template, request
import time

# Change these for your setup.
IP_ADDRESS = '192.168.1.19' # of your Pi

# Configure the RRB
rr = RRB2()
motor_speed = 0.6

# Handler for the home page
@route('/')
def index():
    cmd = request.GET.get('command', '')
    if cmd == 'f':
        rr.forward()
    elif cmd == 'l':
        rr.left(0, 0.5) # turn at half speed
    elif cmd == 's':
        rr.stop()
    elif cmd == 'r':
        rr.right(0, 0.5)
    elif cmd == 'b':
        rr.reverse(0, 0.3) # reverse slowly
    return template('home.tpl')
        
# Start the webserver running on port 80
try: 
    run(host=IP_ADDRESS, port=80)
finally:  
    rr.cleanup()

