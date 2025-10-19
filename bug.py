import Rpi.GPIO as GPIO
import time
from bugClass import Bug

GPIO.setmode(GPIO.BCM)

#3 GPIO pins
s1,s2,s3 = 2,3,4

GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(s3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# initial bug with default parameters
bug = Bug()

#track s2 val(wraping)
s2Previous = GPIO.inpu(s2)

#bug initially stopped
bugOn = False

try:
  while 1:
    s1_state = GPIO.input(s1)
    s2_state = GPIO.input(s2)
    s3_state = GPIO.input(s3)
    
    #check s1 to see if On and bug was stopped
    if s1_state and not bugOn:
      bugOn = True
      print("Bug started")
      bug.start()
    #check if s1 off and bug was on
    elif not s1_state and bugOn:
      bugOn = False
      print("Bug Stopped")
      bug.stop()

    #check is s2_state changed
    if s2_state != s2Previous:
      bug.isWrapOn = not bug.isWarpOn #flip between true and false
      print(f"Wrap mode: {bug.isWrapOn}")
    s2Previous = s2_state

    #check s3 and increase speed
    if s3_state:
      bug.timeStep = .1/3
    else:
      bug.timeStep = .1

except KeyboardInterrupt:
  pass


