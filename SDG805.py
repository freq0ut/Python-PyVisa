#add if no reading... return float of 0
import visa
import time
delay = 0.01 #delay in seconds (50 ms)

rm = visa.ResourceManager()
WF = rm.open_resource('USB0::0xF4ED::0xEE3A::SDG00003140724::INSTR')

def toggleOutput(chan,state):
	cmd1 = 'C%s:OUTP %s' %(chan, state)
	WF.write(cmd1)
	time.sleep(1)

def sine(chan,amp,freq):
	if(amp>5):
		print('ERR (amp too large)')
	else:
		cmd1 = 'C%s:BSWV WVTP,SINE,AMP,%s,FRQ,%s' %(chan,amp,freq)
		WF.write(cmd1)
		time.sleep(delay)