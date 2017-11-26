#!/usr/bin/env python

import os
import time
import timer
import camera_interface
import car_interface
import unique_file_name
import subprocess


if __name__ == "__main__":
	time.sleep(10.0)	
	try:
		capture_state_params = [
		(5.0,"off"), #0 - Out 0, In 0 - highbeams off for a while
		(0.0,"on_edge"), #1 - Out 0, In 1 - highbeams just requested to turn on
		(0.0,"off_edge"), #2 - Out 1, In 0 - highbeams just requested to turn off
		(5.0,"on") #3 - Out 1, In 1 - highbeams on for a while
		]
		base_path = "/media/pi/highbeamUSB"
	
		if os.path.isdir(base_path):
			for _,rel_path in capture_state_params:
				path = os.path.join(base_path,rel_path)
				if not os.path.isdir(path):
					os.mkdir(path)

		with \
		camera_interface.CameraInterface() as cam, \
		car_interface.CarInterface() as car:

				highbeam_input = car.getHighbeamInput()
				highbeam_output = highbeam_input
				highbeam_delay_timer = timer.Timer()
				capture_delay_timer = timer.Timer()


				while True:
					if car.getShutdownInput():
						subprocess.call("sudo shutdown -h now", shell=True)
						print("shutdown")

					highbeam_input = car.getHighbeamInput()
					switch_input = car.getSwitchInput()

					#detect changes in the highbeam_input and reset the delay timer
					if highbeam_input == highbeam_output:
						highbeam_delay_timer.reset()

					#[off delay, on delay]
					if highbeam_delay_timer() > [3.0,5.0][highbeam_input]:
						highbeam_output = highbeam_input

					#Outputs
					car.setHighbeamOutput(highbeam_output)

					#there are 4 combinations of highbeam inputs and outputs.
	 				state = 2*highbeam_output + highbeam_input

					capture_delay_time,rel_path = capture_state_params[state]

					if capture_delay_timer() > capture_delay_time and switch_input:
						capture_delay_timer.reset()
						path = os.path.join(base_path,rel_path)
						fileName = unique_file_name.getUniqueFileName(path,"img_%05i.png")
						print(fileName)
						cam.capture(fileName)

					time.sleep(0.0333)

	except Exception as e:
		print(e)
