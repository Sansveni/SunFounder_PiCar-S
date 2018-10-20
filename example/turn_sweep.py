#Program written by Charlie Didear.
#picar libraries were made by Dream at SunFounder.
from picar import front_wheels
from picar import back_wheels
from timeit import default_timer as timer
import time
import picar
import random

picar.setup()

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
#fw.turning_max = 45

forward_speed = 70
backward_speed = 70

while True:
#	for x in range (180):
#		print "angle: {}".format(x)
#		fw.turn(x)
#		time.sleep(.5)
	fw.turn(0)
	print "angle is 0.\n"
	time.sleep(1)
	fw.turn(90)
	print "angle is 90.\n"
	time.sleep(1)

	fw.turn(180)
	print "angle is 180.\n"
	time.sleep(1)

