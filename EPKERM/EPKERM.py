def playSound(SOUNDFILE):
#sound file will be a shell script.
#see test.sh for an example on how the sound works
	import subprocess
	subprocess.call(['/bin/bash', SOUNDFILE])
def moveServo(DEGREES, SERVOPIN):


    # This formula converts the number of degrees (0 - 180) that these
    # servo motors can rotate to a pulse width that will move the
    # aiming servo appropriately.

    # 2.5% of 20ms is .5ms or 500 microseconds.  This pulse width will
    # move the servo motor to 0 degrees.

    # 7.5% of 20ms is 1.5ms.  This pulse width will move the servo to 90 degrees.

    # 12.5% of 20ms is 2.5ms.  This pulse width will move the servo to 180 degrees.

    PULSEWIDTH = ((DEGREES/18) + 2.5)
    print DEGREES
    print " was converted to pulse width of %.2f milliseconds." % (20 * PULSEWIDTH / 100)



    GPIO.cleanup()

    #
    # The towerpro servo motor moves based on duration of pulses sent to it.
    # This illustration shows how to rotate the motor at 90 degree increments.


    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)



    GPIO.setup(SERVOPIN,GPIO.OUT)



    p = GPIO.PWM(SERVOPIN,50)

    # Use 2.5% of 20ms as zero degrees
    # Use 12.5% of 20ms as 180 degrees
    START=2.5
    DELAY=.5
    p.start(START)

    #time.sleep(DELAY)
    p.ChangeDutyCycle(PULSEWIDTH)
    time.sleep(DELAY)

def fire():
    # The towerpro servo motor moves based on duration of pulses sent to it.
    # This illustration shows how to rotate the motor at 90 degree increments.
    # A 1.5ms pulse centers the servo; a .5ms pulse drags it to 0 degrees
    # A 2.5ms pulse brings it to 180 degrees.


    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)

    #Use Pin 15 as output to control the servo motor
    FIREPIN=32
    GPIO.setup(FIREPIN,GPIO.OUT)
    GPIO.output(FIREPIN,GPIO.LOW)



    # Use 2.5% of 20ms as zero degrees
    # Use 12.5% of 20ms as 180 degrees
    #Use the Pulse Width Modulation at 20ms (1/50)
    p = GPIO.PWM(FIREPIN,50)

    p.start(2.5)

    p.ChangeDutyCycle(7.5)
    time.sleep(.5)
    # Send 7.5% (of 20ms or 1.5ms) pulse to servo at pin FIREPIN
    # (rotate 90 degrees)
    p.ChangeDutyCycle(2.5)
    time.sleep(.5)
    # Send 2.5% (of 20ms or .5ms) pulse to servo at pin SERVOPIN
    # (rotate back to zero degrees)
    p.ChangeDutyCycle(7.5)

    time.sleep(.5)

    GPIO.output(FIREPIN,GPIO.LOW)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)



LEFTPIN = 8
RIGHTPIN = 10
UPPIN = 12
DOWNPIN = 16
BPIN = 18
APIN = 22
VERTICALSERVOPIN = 26
HORIZONTALSERVOPIN = 24
FIRESERVOPIN = 32

left = GPIO.input(LEFTPIN)
right = GPIO.input(RIGHTPIN)
up = GPIO.input(UPPIN)
down = GPIO.input(DOWNPIN)
b = GPIO.input(BPIN)
a = GPIO.input(APIN)

UDServo = 90
LRServo = 90
DEGREEINCREMENT = 15
MAXVERTICALANGLE = 180
MINVERTICALANGLE = 0
MAXHORIZONTALANGLE = 180
MINHORIZONTALANGLE = 0
CENTER = 90

while True:

	GPIO.setup(LEFTPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(RIGHTPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(UPPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(DOWNPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(APIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	left = GPIO.input(LEFTPIN)
	right = GPIO.input(RIGHTPIN)
	up = GPIO.input(UPPIN)
	down = GPIO.input(DOWNPIN)
	b = GPIO.input(BPIN)
	a = GPIO.input(APIN)
	if right == False:
        	print('left button pressed')
        	if LRServo > MINHORIZONTALANGLE:
            		LRServo = LRServo - DEGREEINCREMENT
            		moveServo(LRServo, HORIZONTALSERVOPIN)
	if left == False:
		print('right button pressed')
		if LRServo < MAXHORIZONTALANGLE:
        		LRServo = LRServo + DEGREEINCREMENT
        		moveServo(LRServo, HORIZONTALSERVOPIN)
	if up == False:
		print('up button pressed')
		if UDServo < MAXVERTICALANGLE:
    			UDServo = UDServo + DEGREEINCREMENT
    			moveServo(UDServo, VERTICALSERVOPIN)
	if down == False:
		print('down button pressed')
		if UDServo > MINVERTICALANGLE:
    			UDServo = UDServo - DEGREEINCREMENT
    			moveServo(UDServo, VERTICALSERVOPIN)
	if b == False:
		print('b button pressed')
		moveServo(CENTER, HORIZONTALSERVOPIN)
		moveServo(40, VERTICALSERVOPIN)
		if (UDServo != 40) and (LRServo != 90):
			UDServo = 40
			LRServo = 90
	if a == False:
		playSound('./test.sh')
		print('a button pressed')
		fire()
	time.sleep(.1)



