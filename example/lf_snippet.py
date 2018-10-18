	while True:
		lt_status_now = lf.read_flashlight()
		print lt_status_now
		# Angle calculate
		if	lt_status_now == [0,1,0]:
			step = 0
		elif lt_status_now == [1,1,0] or lt_status_now == [0,1,1]:
			step = a_step
		elif lt_status_now == [1,0,0] or lt_status_now == [0,0,1]:
			step = b_step
		
		# Direction calculate
		if	lt_status_now in ([0,1,0],[1,1,1]):
			fw.turn(90)
			bw.forward()
			bw.speed = forward_speed
		# turn right
		elif lt_status_now in ([1,1,0],[1,0,0]):
			fw.turn(90 - step)
			bw.forward()
			bw.speed = forward_speed
		# turn left
		elif lt_status_now in ([0,1,1],[0,0,1]):
			fw.turn(90 + step)
			bw.forward()
			bw.speed = forward_speed
		# backward
		elif lt_status_now == [1,0,1]:
			fw.turn(90)
			bw.backward()
			bw.speed = forward_speed
		# none of all above
		elif lt_status_now == [0,0,0]:
			fw.turn(90)
			bw.stop()

def stop():