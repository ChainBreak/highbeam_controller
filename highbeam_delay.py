#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess

try:
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT) #highbeam output. 1 turn on high beams
	GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)# switch state
	GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_UP)# high beam state. 0 high beams on. 1 high beams off


	highbeams_out = False
	last_time = time.time()
	last_switch = False
	last_switch_time = time.time()
	switch_count = 0
	for i in range(3):
		GPIO.output(11,1)
		time.sleep(0.3)
		GPIO.output(11,0)
		time.sleep(0.3)
	
	while True:
	        switch = GPIO.input(13)
	        highbeams_in = not GPIO.input(15)
	        if highbeams_in == highbeams_out:
			last_time = time.time()
	
		if (time.time() - last_time) > 1.5:
			highbeams_out = highbeams_in
			
	        GPIO.output(11,highbeams_out)
	        print("Switch %i, Highbeams In %i, Highbeams Out %i" % (switch,highbeams_in,highbeams_out))

		if switch != last_switch:
			switch_count += 1
			last_switch_time = time.time()
			last_switch = switch
		
		if time.time() - last_switch_time > 1:
			switch_count = 0

		if switch_count >= 6:
			print("shutdown")
			for i in range(3):
				GPIO.output(11,1)
				time.sleep(0.3)
				GPIO.output(11,0)
				time.sleep(0.3)		
			subprocess.call("sudo shutdown -h now", shell=True)
			break

        	time.sleep(0.03)
	

except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
	print("Closed")
