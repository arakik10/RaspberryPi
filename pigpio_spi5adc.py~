import pigpio
import time

pi= pigpio.pi()

import readSpiADC as x

PinCLK   = 11
PinMISO  =  9
PinMOSI  = 10
PinCS    = [8,7]

pi.set_mode(PinCLK,  pigpio.OUTPUT)
pi.set_mode(PinMISO, pigpio.INPUT)
pi.set_mode(PinMOSI, pigpio.OUTPUT)
pi.set_mode(PinCS[0],pigpio.OUTPUT)
pi.set_mode(PinCS[1],pigpio.OUTPUT)

try:
    v=[]
    while True:
	for i in range(2):
            v=v+[[]]
            print '{0:1d}:'.format(i),
            if i == 1:
                print ' ',
            for j in range(8):
                v[i]= v[i] + [x.readSpiADC(0,PinCLK,PinMOSI,PinMISO,PinCS[i])]
                print " {0:4d}".format(v[i][j]),
            print "\n",
        time.sleep(0.2)

except KeyboardInterrupt:
    pi.stop()
