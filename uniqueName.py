#!/usr/bin/env python


import time
import os


pathCounterDict = {}

def getUniqueFileName(path,nameFormat):
	startFileName = os.path.join(path,nameFormat % 0)
	fileName = startFileName
	if os.path.isdir(path):
		i = 0

		if startFileName in pathCounterDict:
			i = pathCounterDict[startFileName]

		fileName = os.path.join(path,nameFormat % i)
		while os.path.isfile(fileName):
			i+=1
			fileName = os.path.join(path,nameFormat % i)
			print("try " + fileName)
		pathCounterDict[startFileName] = i
	return fileName


if __name__ == "__main__":
	for i in range(4):
		path = getUniqueFileName("/home/tom/pathTest","test%0i.txt")
		print(path)
		with open(path,"w") as f:
			f.write("hello")

	print(pathCounterDict)
