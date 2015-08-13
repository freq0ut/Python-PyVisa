#!/usr/bin/env python
import visa
import time
import SDS1102 as osc
import SDG805 as wf
import DP832 as psu
import numpy as np
import matplotlib.pyplot as plot
import xlwt

#--------------------------GLOBAL VARIABLES------------------------------------------

delay = 0.01 #delay in seconds (50 ms)


#--------------------------GENERAL FUNCTIONS-----------------------------------------

def iteration(start, end, step):		#define a for loop function
	while start <= end:
		yield start
		start += step


#--------------------------------MAIN------------------------------------------------
time.sleep(1)

psu.setCurrent(3,0.5)
#psu.setOVP(3,5.1)
#psu.toggleOVP('OFF')
psu.setOCP(3,0.222)
psu.toggleOCP('ON')

psu.setVoltage(3,3.3)
psu.toggleOutput(3,'ON')
time.sleep(1)

for i in iteration(3.3,5,0.1):
	
	psu.setVoltage(3,i)
	time.sleep(1)
	power = round(psu.measPower(3)*1000,2)
	volt = round(psu.measVolt(3),1)
	current = round(psu.measCurrent(3),2)
	
	print("Power: " + str(power) + " mW" + "    Voltage: " + str(volt) + " V" + "    Current: " + str(current) + " A")
	
psu.toggleOutput(3,'OFF')

print("\n*** Script Completed! ***")