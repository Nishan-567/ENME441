#import 
import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#import shifter
from shifter import Shifter

#instantiate a Shifter object
shift = Shifter(serialPin=23, latchPin=24, clockPin=25)

#start at random position
position = random.randint(0,7)

#create bit that coresponds to "position" led
led = 1 << position #for position = 3, returns 0b00001000 which ligths the 3rd led

try:
	while 1:
		#light current LED
		shift.shiftByte(led)
		time.sleep(.05)

		#move "bug"
		increment = random.choice([-1, 1])
		position += increment

		#keep bug on the 8 LEDs
		position = max(0, min(7, position))
		led = 1 << position
except:

	GPIO.cleanup()


