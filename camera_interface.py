#!/usr/bin/env python3


import io
import time
import picamera
with picamera.PiCamera() as camera:
	camera.resolution = [320,240]
    camera.framerate = 30

    stream = io.BytesIO()
	count = 0
    for foo in camera.capture_continuous(stream, format='png',use_video_port = True):

		with open("img%03i.png"%count,'w') as img:
			img.write(stream)

        # Truncate the stream to the current position (in case
        # prior iterations output a longer image)
        stream.truncate()
        stream.seek(0)
