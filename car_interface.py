#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT) #highbeam output. 1 turn on high beams
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)# switch state
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_UP)# high beam state. 0 high beams on. 1 high beams off


highbeams_out = False
last_time = time.time()

for i in range(3):
	GPIO.output(11,1)
	time.sleep(0.3)
	GPIO.output(11,0)
	time.sleep(0.3)

while True:
        switch = GPIO.input(13)
        highbeams_in = GPIO.input(15)
        if highbeams_in == True:
		last_time = time.time()

	highbeams_out = (time.time() - last_time) > 1.5
		
        GPIO.output(11,highbeams_out)
        print("Switch %i, Highbeams In %i, Highbeams Out %i" % (switch,highbeams_in,highbeams_out))
        time.sleep(0.03)

