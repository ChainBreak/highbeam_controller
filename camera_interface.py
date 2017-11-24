#!/usr/bin/env python3


import io
import time
import picamera
with picamera.PiCamera() as camera:
	camera.resolution = [320,240]
	camera.framerate = 5
	stream = io.BytesIO()
	count = 0
	for foo in camera.capture_continuous(stream, format='jpeg',use_video_port = False):
		stream.truncate()
		stream.seek(0)
		filename = "/media/pi/highbeamUSB/img%03i.jpg"%count
		with open(filename,'wb') as img:
			img.write(stream.read())
			#stream.readinto(img)
	
		count += 1
		print(filename)
