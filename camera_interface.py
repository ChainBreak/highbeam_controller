#!/usr/bin/env python


import io
import time
import picamera
import picamera.array


class CameraInterface():
	def __init__(self):
		self.cam = None

	def __enter__(self):
		try:
			self.cam = picamera.PiCamera()
			self.cam.resolution = (320,240)
			self.cam.framerate = 30
		except:
			pass
		return self

	def __exit__(self,*args):
		try:
			self.cam.close()
		except:
			pass
		self.cam = None

	def capture(self,fileName):
		success = False
		if self.cam != None:
			try:
				self.cam.capture(fileName,format="png")
				success = True
			except Exception as e:
				print(e)
		return success


if __name__ == "__main__":
	with CameraInterface() as cam:
		for i in range(10):
			fn = "/media/pi/highbeamUSB/img%0i.png"%i
			success = cam.capture(fn)
			print(fn+" %i" % success)




# res = (320,240)
#
# try:
# 	with picamera.PiCamera() as camera:
# 		camera.resolution = res
#
# 		with picamera.array.PiRGBArray(camera) as output:
# 			for foo in camera.capture_continuous(output, 'rgb',use_video_port = True):
# 				print('Captured %dx%d image' % (output.array.shape[1], output.array.shape[0]))
# 				output.truncate(0)
# except:
# 	pass
#
#
# def fileName():
# 	for i in range(30):
# 		fn = "/media/pi/highbeamUSB/seqImg%0i.png"%i
# 		print(fn)
# 		yield fn
#
#
# try:
# 	with picamera.PiCamera() as camera:
# 		camera.resolution = res
# 		camera.framerate = 30
# 		camera.capture_sequence(fileName(),format="png")
#
#
# 		for i in range(31,60):
# 			fn = "/media/pi/highbeamUSB/seqImg%0i.png"%i
# 			print(fn)
# 			camera.capture(fn,format="png")
# except KeyboardInterrupt:
# 	pass
