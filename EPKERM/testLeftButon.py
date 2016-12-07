import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

left = False
while True:
	
	print GPIO.input(8)
	if GPIO.input(8) == False:
		print('left button pressed')
	print("loop")
	time.sleep(0.5)
