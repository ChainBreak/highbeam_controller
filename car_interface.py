#!/usr/bin/env python

#import RPi.GPIO as GPIO
import time
import threading
import timer


class CarInterface():
	HEADLIGHT_OUT_PIN = 11
	SWITCH_PIN = 13
	HEADLIGHT_IN_PIN = 15

	def __init__(self):
		self.loopThread = threading.Thread(target=self.loop)
		self.loopThread.daemon = True
		self.loopThread.start()

		self.highbeam_out = False
		self.highbeam_in = False
		self.switch = False
		self.shutdown = False


		#set mode to board which means use the pysical pin numbering
		GPIO.setmode(GPIO.BOARD)
		#highbeam output. 1 turn on high beams
		GPIO.setup(HEADLIGHT_OUT_PIN,GPIO.OUT)
		# switch state
		GPIO.setup(SWITCH_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
		# high beam state. 0 high beams on. 1 high beams off
		GPIO.setup(HEADLIGHT_IN_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)


	def getHighbeamInput(self):
		return self.highbeam_in

	def getSwitchInput(self):
		return self.switch

	def getShutdownInput(self):
		return self.shutdown

	def setHighbeamOutput(self,state):
		self.highbeam_out = state

	def loop(self):
		shutdown_toggle_count = 0
		last_switch = False
		shutdown_count_timer = timer.Timer()
		while True:
			#read and write to IO
			try:
				GPIO.output(HEADLIGHT_OUT_PIN,self.highbeam_out)
				self.switch = GPIO.input(SWITCH_PIN)
				self.highbeam_in = GPIO.input(HEADLIGHT_IN_PIN)
			except Exception as e:
				print(e)

			#If the switch is toggled multiple times in a short period
			#turn on the shutdown output
			if self.switch != last_switch:
				last_switch = self.switch
				shutdown_count_timer.reset()
				shutdown_toggle_count += 1

			if shutdown_count_timer() > 1.5:
				shutdown_toggle_count = 0

			self.shutdown = shutdown_toggle_count > 6

			#loop at about 30 hz
			time.sleep(0.03)


	def __del__(self):
		GPIO.cleanup()
		print("Closed")


if __name__ == "__main__":
	car = CarInterface()

	while True:
		time.sleep(0.1)
		print("h in: %i, switch: %i, shutdown %i", (car.getHighbeamInput(), car.getSwitchInput(), car.getShutdownInput()))
