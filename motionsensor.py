from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
derp = 0

while True:
	pir.wait_for_motion()
	camera.start_preview()
	# camera.capture('/home/pi/Desktop/testing.jpg')
	camera.capture('/home/pi/Desktop/testing-' + str(derp) + '.jpg')
	derp += 1
	pir.wait_for_no_motion()
	camera.stop_preview()
