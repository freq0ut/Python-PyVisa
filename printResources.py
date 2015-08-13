#!/usr/bin/env python
import visa

rm = visa.ResourceManager()
numEle = len(rm.list_resources())

def iteration(start, end, step):		#define a for loop function
	while start <= end:
		yield start
		start += step

for i in iteration(0, numEle-1, 1):
	print(rm.list_resources()[i])