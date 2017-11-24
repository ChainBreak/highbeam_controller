#!/usr/bin/env python


import time

class Timer():
	def __init__(self):
		self.reset()

	def reset(self):
		self.startTime = time.time()

	def __call__(self):
		return time.time() - self.startTime

if __name__ == "__main__":
	t = Timer()
	print(t())
	time.sleep(1)

	print(t())
