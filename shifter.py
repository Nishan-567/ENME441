import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Shifter:
  #Def for various pins
  def _init_(self, serialPin, latchPin, clockPin):
    self.serialPin = serialPin
    self.latchPin = latchPin
    self.clockPin = clockPin

    GPIO.setup(self.serialPin, GPIO.OUT)
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)
  #ping method
  def ping(self, pin):
    GPIO.output(pin, 1)
    time.sleep(0)
    GPIO.output(pin, 0)
  #shift method
  def shiftByte(self, b):
    for i in range(8):
      GPIO.output(self.serialPin, b & (1 << i))
      self.ping(self.clockPin)
    self.ping(self.latchPin)

#use class
shift = Shifter(23, 24, 25)

try:
  while 1:
    for i in range(2**8):
      shift.shiftByte(i)
      time.sleep(0.5)
except:
  GPIO.cleanup()