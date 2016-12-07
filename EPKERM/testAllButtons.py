import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN,pull_up_down=GPIO.PUD_UP)



while True:
	left = GPIO.input(8)
	right = GPIO.input(10)
	up = GPIO.input(12)
	down = GPIO.input(16)
	b = GPIO.input(18)
	a = GPIO.input(22)
	if left == False:
		print('left button pressed')
	if right == False:
		print('right button pressed')
	if up == False:
		print('up button pressed')
	if down == False:
		print('down button pressed')
	if b == False:
		print('b button pressed')
	if a == False:
		print('a button pressed')
	time.sleep(0.2)
