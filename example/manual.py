#Program written by Charlie Didear.
#picar libraries were made by Dream at SunFounder.
from picar import front_wheels
from picar import back_wheels
from timeit import default_timer as timer
import time
import picar
import random
import atexit
picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

forward_speed = 70
backward_speed = 70

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
getch = _GetchUnix()

def exitFunc():
	bw.stop()
	fw.turn_straight()
	print "Program terminating.  Goodbye!\n"
	

print "Type q to quit\n"
atexit.register(exitFunc)

forward_speed = 70
backward_speed = 70
lastCommand = 0
current = 0
turn_angle = 0 
going_forward = False;
going_backward = False;
while True:
	uinput =getch();
	current = timer()
	

	print "current: {}".format(current)
	if uinput=='q':
		exit()
	elif uinput=='w':
		if going_backward == True:
			bw.stop()
			going_backward = False;
		else:
			bw.forward()
			bw.speed = forward_speed
			going_forward = True
		lastCommand = timer()
	elif uinput=='s':
		if going_forward == True:
			bw.stop()
			going_forward = False;
		else:
			bw.backward()
			bw.speed = backward_speed
			going_backward = True
		lastCommand = timer()
	elif uinput=='d':
#		if(turn_angle < 180):
#			turn_angle+=1
#		fw.turn(turn_angle)
		if(turn_angle<90): #if going leftwards at any degree, set to straight
			turn_angle = 90
		elif(turn_angle<180): #if not full right, set to full right
			turn_angle =180
		fw.turn(turn_angle)
		lastCommand = timer()
	elif uinput=='a':
#		if(turn_angle>0):
#			turn_angle-=1
#		fw.turn(turn_angle)
		if(turn_angle>90):
			turn_angle =90
		elif(turn_angle>0):
			turn_angle=0
		fw.turn(turn_angle)			
		lastCommand = timer()

	else:
		print "Unrecognized command.\n"
	
	if current-lastCommand > 0.30:
		print "Stopping car.\n"
		bw.stop()
	
	time.sleep(.1)