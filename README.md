# Python PyVisa
###### Author: Zack Goyetche
### Basic functions for controlling test equipment with PyVisa

#### These scripts support the following instrutments:
* Digital MultiMeter:             Siglent SDM3055
* Digital Oscillopscope:          Siglent SDS1102CNL
* Arbitrary Waveform Generator:   Siglent SDG805
* Programmable Power Supply:      Rigol DP832


# PSU Commands:
### *Rigol DP832*

**psu.selOutput(chan)**
```
argument: chan: (1, 2, or 3)
description: moves selection to specified channel.
```

**psu.toggleOutput(chan,state)**
```
argument: chan: (1, 2, or 3) & state: ‘ON’ or ‘OFF’
description: turn the output on/off.
```

**psu.setVoltage(chan,val)**
```
argument: chan: (1, 2, or 3) & val: (float)
description: set voltage output for specified channel.
```

**psu.setCurrent(chan,val)**
```
argument: chan: (1, 2, or 3) & val: (float)
description: set current output for specified channel.
```

**psu.setOVP(chan,val)**
```
argument: chan: (1, 2, or 3) & val: (float)
description: set the value for OVP on specified channel.
```

**psu.setOCP(chan,val)**
```
argument: chan: (1, 2, or 3) & val: (float)
description: set the value for OCP on specified channel.
```

**psu.toggleOVP(state)**
```
argument: state: (‘ON’ or ‘OFF’)
description: toggles over voltage protection on/off.
```

**psu.toggleOCP(state)**
```
argument: state: (‘ON’ or ‘OFF’)
description: toggles over current protection on/off.
```

**psu.measVolt(chan)**
```
argument: chan: (1, 2, or 3)
description: measure output voltage for specified channel (returned as float).
```

**psu.measCurrent(chan)**
```
argument: chan: (1, 2, or 3)
description: measure output current for specified channel (returned as float).
```

**psu.measPower(chan)**
```
argument: chan: (1, 2, or 3)
description: measure output power for specified channel (returned as float).
```

# Oscope Commands:
### *Siglent SDS1102CNL*

**osc.measVpp(chan)**
```
argument: chan: (1 or 2)
description: measure peak to peak voltage for specified channel (returned as float).
```

**osc.measRMS(chan)**
```
argument: chan: (1 or 2)
description: measure RMS voltage for specified channel (returned as float).
```

**osc.measVMax(chan)**
```
argument: chan: (1 or 2)
description: measure max voltage for specified channel (returned as float).
```

**osc.measFreq(chan)**
```
argument: chan: (1 or 2)
description: measure frequency for specified channel (returned as float).
```

**osc.measPeriod(chan)**
```
argument: chan: (1 or 2)
description: measure period for specified channel (returned as float).
```

# DMM Commands:
### *Siglent SDM3055*

**wf.measV(acdc)**
```
argument: acdc: (‘AC’ or ‘DC)
description: measure AC or DC voltage. Scaling defaults to ‘auto’.
```

**wf.measI(acdc)**
```
argument: acdc: (‘AC’ or ‘DC)
description: measure AC or DC current. Scaling defaults to ‘auto’.
```

# WF Gen Commands:
### *Siglent SDG805*

**wf.toggleOutput(chan,state)**
```
argument: chan: (1) & state: (‘ON’ or ‘OFF’)
description: turn the output on/off.
```

**wf.sine(chan,freq)**
```
argument: chan: (1) & freq: (float)
description: sets the frequency for the specified output channel.
```
