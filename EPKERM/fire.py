import RPi.GPIO as GPIO
import time
#
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

p.start(12.5)

#p.ChangeDutyCycle(12.5)
#time.sleep(.5)
# Send 7.5% (of 20ms or 1.5ms) pulse to servo at pin FIREPIN
# (rotate 90 degrees)
#p.ChangeDutyCycle(7.5)
#time.sleep(.5)
# Send 2.5% (of 20ms or .5ms) pulse to servo at pin SERVOPIN
# (rotate back to zero degrees)

#p.ChangeDutyCycle(2.5)

#time.sleep(.5)


#GPIO.output(FIREPIN,GPIO.LOW)
