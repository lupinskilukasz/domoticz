#!/usr/bin/python



import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(32, GPIO.OUT)

GPIO.output(32,0)

time.sleep(0.2)

GPIO.cleanup()
