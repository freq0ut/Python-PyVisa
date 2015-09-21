#!/usr/bin/env python
import visa
import time
import math as m
import SDS1102 as osc
import SDG805 as wf
import DP832 as psu
import numpy as np
import matplotlib.pyplot as plot
import openpyxl as xl

#--------------------------GLOBAL VARIABLES------------------------------------------

delay = 0.01 #delay in seconds (50 ms)
outputSig = 0.401 	#initialization for chan 1 oscope scaling
inputSig = 0.004 	#initialization for chan 2 oscope scaling
magnitude = [0] 	#list for storing magnitude readings in dB
frequency = [0] 	#list for storing frequency

freqStep = 100 			#set increment of frequency sweep
maxFreq = 1000000 		#end frequency
PDF_title = 'LM318FreqResponse'
XL_title = 'dataOutput'


#--------------------------CREATE EXCEL SPREADSHEET----------------------------------
wb = xl.Workbook() 				#create workbook object named wb

sheet = wb.get_active_sheet() 	#get active sheet
sheet.title = 'Data' 			#change name of active sheet to 'Data'

sheet['A1'] = 'Frequency' 		#label A1 'Frequency'
sheet['B1'] = 'Gain' 			#label B1 'Gain'

#--------------------------GENERAL FUNCTIONS-----------------------------------------

def iteration(start, end, step):		#define a for loop function
	while start <= end:
		yield start
		start += step


#--------------------------------MAIN------------------------------------------------
time.sleep(1)

#Initialize PSU (set CH1: 12V / 0.2A OCP and CH2: 12V / 0.2A OCP)
psu.setVoltage(1,12)
psu.setOCP(1,0.2)
psu.toggleOCP('ON')
psu.setVoltage(2,12)
psu.setOCP(2,0.2)
psu.toggleOCP('ON')
psu.toggleOutput(1,'ON')
psu.toggleOutput(2,'ON')
time.sleep(1)

#Initialize Function Generator
wf.sine(1,0.004,1)
wf.toggleOutput(1,'ON')
time.sleep(1)

#Begin test iteration
for i in iteration(freqStep,maxFreq,freqStep):
	wf.sine(1,0.004,i) #increment sine wave frequency

	#set the proper time and magnitude scaling for oscope
	osc.setVoltDiv(1,outputSig)
	osc.setVoltDiv(2,inputSig)
	osc.setTimeDiv(1,i)
	osc.setTimeDiv(2,i)

	#delay for measurement
	time.sleep(3) 
	outputSig = osc.measVpp(1)
	inputSig = osc.measVpp(2)
	print(str(i) + " Hz")
	#conversions and storage:
	magnitude.append(20*m.log10(outputSig/inputSig)) #convert to dB and append to magntiude list
	print(str(20*m.log10(outputSig/inputSig)) + ' dB')
	frequency.append(i) #log frequency for given magnitude reading

#plot and save:
plot.plot(frequency, magnitude)
plot.title("LM318 Frequency Response")
plot.ylabel("Magnitude (dB)")
plot.xlabel("Frequency (Hz)")
plot.savefig(PDF_title + '.pdf')
time.sleep(1)
wf.toggleOutput(1,'OFF')
time.sleep(1)
psu.toggleOutput(1,'OFF')
psu.toggleOutput(2,'OFF')

magLength = len(magnitude)		#find length of magnitude vector for transfer to excel spreadsheet
freqLength = len(frequency)		#find length of frequency vector for transfer to excel spreadsheet

for i in range(0,freqLength,1):
	sheet['A' + str(i+2)] = frequency[i]	#fill column A with frequency points
for i in range(0,magLength,1):
	sheet['B' + str(i+2)] = magnitude[i]	#fill column B with magnitude points

wb.save(XL_title + '.xlsx')
print("\n*** Script Completed! ***")