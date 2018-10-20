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
angle = 0
while True:
	for x in range (181):
		print "angle: {}".format(angle)
		angle = x
		time.sleep(.5)