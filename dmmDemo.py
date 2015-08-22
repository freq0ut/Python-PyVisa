#!/usr/bin/env python
import visa
import time
import math as m
#import SDS1102 as osc
#import SDG805 as wf
import DP832 as psu
import SDM3055 as dmm
import numpy as np
import matplotlib.pyplot as plot
import openpyxl as xl

#--------------------------GLOBAL VARIABLES------------------------------------------

delay = 0.01 		#delay in seconds (50 ms)
voltArray = [0] 	#list for storing magnitude readings in dB
currArray = [0] 	#list for storing frequency

#--------------------------CREATE EXCEL SPREADSHEET----------------------------------
XL_title = 'DMMdataOutput'
wb = xl.Workbook() 				#create workbook object named wb

sheet = wb.get_active_sheet() 	#get active sheet
sheet.title = 'Data' 			#change name of active sheet to 'Data'

sheet['A1'] = 'Voltage' 		#label A1 'Voltage'
sheet['B1'] = 'Current' 		#label B1 'Current'


#--------------------------GENERAL FUNCTIONS-----------------------------------------

def iteration(start, end, step):		#define a for loop function
	while start <= end:
		yield start
		start += step


#--------------------------------MAIN------------------------------------------------
time.sleep(1)							#delay
psu.toggleOutput(3,'ON')				# turn PSU channel 3 output ON

i = 0;									# initialize voltage coutner variable

while(i <= 1):							# while voltage is less than euqal to 5V
	psu.setVoltage(3, i) 				# set PSU output voltage
	time.sleep(0.5)						# delay
	voltReading = dmm.measV('DC')		# measure voltage (DMM)
	voltArray.append(voltReading)

	time.sleep(0.5)						# delay
	currReading = dmm.measI('DC')		# measure current (DMM)
	currArray.append(currReading)

	time.sleep(0.5)						# delay
	i = i+0.1							# increment counter for voltage

psu.toggleOutput(3,'OFF')				# turn PSU channel 3 output OFF

voltLength = len(voltArray)				#find length of voltage vector for transfer to excel spreadsheet
currLength = len(currArray)				#find length of magnitude vector for transfer to excel spreadsheet


#--------------------------EXPORT TO EXCEL & SAVE----------------------------------
for i in range(0,voltLength,1):
	sheet['A' + str(i+2)] = voltArray[i]	#fill column A with frequency points
for i in range(0,currLength,1):
	sheet['B' + str(i+2)] = currArray[i]	#fill column B with magnitude points

wb.save(XL_title + '.xlsx')
print("\n*** Script Completed! ***")