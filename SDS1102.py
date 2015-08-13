#add if no reading... return float of 0
import visa
import time
delay = 0.01 #delay in seconds (50 ms)

rm = visa.ResourceManager()
SCOPE = rm.open_resource('USB0::0xF4EC::0xEE3A::SDS00002140417::INSTR')

def measVpp(chan):
	cmd1 = 'C%s:PAVA? PKPK' %chan
	VppString = SCOPE.query(cmd1)
	time.sleep(delay)
	Vpp = float(VppString.split(",",1)[1].split("E",1)[0])
	VppExp = float(VppString.split(",",1)[1].split("E",1)[1].split("V",1)[0])
	Vpp = Vpp*pow(10,VppExp)
	return Vpp

def measRMS(chan):
	cmd1 = 'C%s:PAVA? RMS' %chan
	VrmsString = SCOPE.query(cmd1)
	time.sleep(delay)
	Vrms = float(VrmsString.split(",",1)[1].split("E",1)[0])
	VrmsExp = float(VrmsString.split(",",1)[1].split("E",1)[1].split("V",1)[0])
	Vrms = Vrms*pow(10,VrmsExp)
	return Vrms

def measVMax(chan):
	cmd1 = 'C%s:PAVA? MAX' %chan
	VmaxString = SCOPE.query(cmd1)
	time.sleep(delay)
	Vmax = float(VmaxString.split(",",1)[1].split("E",1)[0])
	VmaxExp = float(VmaxString.split(",",1)[1].split("E",1)[1].split("V",1)[0])
	Vmax = Vmax*pow(10,VmaxExp)
	return Vmax

def measFreq(chan):
	cmd1 = 'C%s:PAVA? FREQ' %chan
	freqString = SCOPE.query(cmd1)
	time.sleep(delay)
	freq = float(freqString.split(",",1)[1].split("E",1)[0])
	freqExp = float(freqString.split(",",1)[1].split("E",1)[1].split("H",1)[0])
	freq = freq*pow(10,freqExp)
	return freq

def measPeriod(chan):
	cmd1 = 'C%s:PAVA? PER' %chan
	periodString = SCOPE.query(cmd1)
	time.sleep(delay)
	period = float(periodString.split(",",1)[1].split("E",1)[0])
	periodExp = float(periodString.split(",",1)[1].split("E",1)[1].split("S",1)[0])
	period = period*pow(10,periodExp)
	return period

def setVoltDiv(chan,val):

	if(val/4 >= 5):
		voltDiv = '10V'
	elif(val/4 >= 2):
		voltDiv = '5V'
	elif(val/4 >= 1):
		voltDiv = '2V'
	elif(val/4 >= 0.5):
		voltDiv = '1V'
	elif(val/4 >= 0.2):
		voltDiv = '500MV'
	elif(val/4 >= 0.1):
		voltDiv = '200MV'
	elif(val/4 >= 0.05):
		voltDiv = '100MV'
	elif(val/4 >= 0.02):
		voltDiv = '50MV'
	elif(val/4 >= 0.01):
		voltDiv = '10MV'
	elif(val/4 >= 0.005):
		voltDiv = '5MV'
	else: #(val/4 > 0.002)
		voltDiv = '2MV'

	cmd1 = 'C%s:VDIV %s' %(chan,voltDiv)
	SCOPE.write(cmd1)

def setTimeDiv(chan,val):
	if(val >= 133.3333e+6):
		timediv = '2.5NS'
	elif(val >= 66.6667e+6):
		timediv = '5NS'
	elif(val >= 33.3333e+6):
		timediv = '10NS'
	elif(val >= 13.3333e+6):
		timediv = '25NS'
	elif(val >= 6.6667e+6):
		timediv = '50NS'
	elif(val >= 3.3333e+6):
		timediv = '100NS'
	elif(val >= 1.3333e+6):
		timediv = '250NS'
	elif(val >= 666.6667e+6):
		timediv = '500NS'

	elif(val >= 333.3333e+3):
		timediv = '1US'
	elif(val >= 133.3333e+3):
		timediv = '2.5US'
	elif(val >= 66.6667e+3):
		timediv = '5US'
	elif(val >= 33.3333e+3):
		timediv = '10US'
	elif(val >= 13.3333e+3):
		timediv = '25US'
	elif(val >= 6.6667e+3):
		timediv = '50US'
	elif(val >= 3.3333e+3):
		timediv = '100US'
	elif(val >= 1.3333e+3):
		timediv = '250US'
	elif(val >= 666.6667e+3):
		timediv = '500US'

	elif(val >= 333.3333e+0):
		timediv = '1MS'
	elif(val >= 133.3333e+0):
		timediv = '2.5MS'
	elif(val >= 66.6667e+0):
		timediv = '5MS'
	elif(val >= 33.3333e+0):
		timediv = '10MS'
	elif(val >= 13.3333e+0):
		timediv = '25MS'
	elif(val >= 6.6667e+0):
		timediv = '50MS'
	elif(val >= 3.3333e+0):
		timediv = '100MS'
	elif(val >= 1.3333e+0):
		timediv = '250MS'
	elif(val >= 666.6667e+0):
		timediv = '500MS'

	elif(val >= 333.3333e-3):
		timediv = '1S'
	elif(val >= 133.3333e-3):
		timediv = '2.5S'
	elif(val >= 66.6667e-3):
		timediv = '5S'
	elif(val >= 33.3333e-3):
		timediv = '10S'
	elif(val >= 13.3333e-3):
		timediv = '25S'
	else: #(val > 6.6667e-3):
		timediv = '50S'

	cmd1 = 'C%s:TDIV %s' %(chan,timediv)
	SCOPE.write(cmd1)
	
def getWaveform(chan):
	# cmd1 = 'GET_CSV DD,MAX,SAVE,ON'
	cmd1 = 'WFSU SP, 3, NP, 2500, FP, 0'
	cmd2 = 'C%s:WF TIME' %chan
	# cmd2 = 'C%s:WF DAT1' %chan
	SCOPE.write(cmd1)
	time = SCOPE.query(cmd2)
	# data = SCOPE.query(cmd2)
	time.sleep(1)

#scaled for at least 5 periods per display
	# 2.5 ns --> 133 Mhz
	# 5.0 ns
	# 10.0 ns
	# 25.0 ns
	# 50.0 ns
	# 100.0 ns
	# 250.0 ns
	# 500.0 ns

	# 1.0 us
	# 2.5 us
	# 5.0 us
	# 10.0 us
	# 25.0 us
	# 50.0 us
	# 100.0 us
	# 250.0 us
	# 500.0 us

	# 1.0 ms
	# 2.5 ms
	# 5.0 ms
	# 10.0 ms
	# 25.0 ms
	# 50.0 ms
	# 100.0 ms
	# 250.0 ms
	# 500.0 ms

	# 1.0 s
	# 2.5 s
	# 5.0 s
	# 10.0 s
	# 25.0 s
	# 50.0 s


# want voltage to be at least 4 divisions
	# 2 mV
	# 5 mV
	# 10 mV
	# 20 mV
	# 50 mV
	# 100 mV
	# 200 mV
	# 500 mV
	# 1 V
	# 2 V
	# 5 V
	# 10 V