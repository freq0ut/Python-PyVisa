#!/usr/bin/env python
import visa
import time
delay = 0.01 #delay in seconds (50 ms)

rm = visa.ResourceManager()
DMM = rm.open_resource('USB0::0xF4EC::0xEE38::SDM305C2150033::INSTR')

def measV(acdc):
	cmd1 = 'MEAS:VOLT:%s? AUTO' %acdc
	time.sleep(delay)

	# take in value as a string
	resultString = str(DMM.query(cmd1))

	# check if first character is a '+' or a '-'
	if(resultString[0] == '+'):
		boolSign = True
	elif(resultString[0] == '-'):
		boolSign = False

	# extract whole number with decimals
	if(boolSign == True):
		result = float(resultString.split("+",1)[1].split("E",1)[0])
	elif(boolSign == False):
		result = float(resultString.split("-",1)[1].split("E",1)[0])

	# determine exponent
	resultExp = float(resultString.split("E",1)[1])

	# apply power to whole number, store this number in a variable
	result = result*pow(10,resultExp)

	# if '+' then value = value
	# if '-' then value = -value
	if(boolSign == True):
		result = result
	elif(boolSign == False):
		result = -result

	# return value
	print(str(result) + ' V')
	return result


def measI(acdc):
	cmd1 = 'MEAS:CURR:%s? AUTO' %acdc
	time.sleep(delay)
	# take in value as a string
	resultString = str(DMM.query(cmd1))

	# check if first character is a '+' or a '-'
	if(resultString[0] == '+'):
		boolSign = True
	elif(resultString[0] == '-'):
		boolSign = False

	# extract whole number with decimals
	if(boolSign == True):
		result = float(resultString.split("+",1)[1].split("E",1)[0])
	elif(boolSign == False):
		result = float(resultString.split("-",1)[1].split("E",1)[0])

	# determine exponent
	resultExp = float(resultString.split("E",1)[1])

	# apply power to whole number, store this number in a variable
	result = result*pow(10,resultExp)

	# if '+' then value = value
	# if '-' then value = -value
	if(boolSign == True):
		result = result
	elif(boolSign == False):
		result = -result

	# return value
	print(str(result) + ' A')
	return result

#def measOhm():