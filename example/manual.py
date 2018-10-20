from picar import front_wheels
from picar import back_wheels
from timeit import default_timer as timer
import time
import picar
import random

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


print "Type q to quit\n"
forward_speed = 70
backward_speed = 70

while True:
	uinput =getch();
	lastCommand = timer()
	current = timer()
	if lastCommand-current > .1:
		bw.stop()
	if uinput=='q':
		exit()
	elif uinput=='w':
		bw.forward()
		bw.speed = forward_speed
		lastCommand = timer()
	elif uinput=='s':
		bw.backward()
		bw.speed = backward_speed
		lastCommand = timer()
	else:
		print "Unrecognized command.\n"
	# 	time.sleep(.01)