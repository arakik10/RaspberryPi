import pigpio
import time

pi= pigpio.pi()

def readSpiADC ( numCH, pinCLK, pinMOSI, pinMISO, pinCS ):
    if numCH > 7 or numCH < 0:
        return -1
    pi.write(pinCS,pigpio.HIGH)
    pi.write(pinCLK,0)
    pi.write(pinCS,0)
    dataMOSI = numCH
    dataMOSI |= 0x18
    dataMOSI <<= 3
    for i in range(5):
        if dataMOSI & 0x80:
            pi.write(pinMOSI,1)
        else:
            pi.write(pinMOSI,0)
        dataMOSI <<= 1
        pi.write(pinCLK,1)
        pi.write(pinCLK,0)
    dataMISO = 0
    for i in range(13):
        pi.write(pinCLK,1)
        pi.write(pinCLK,0)
        dataMISO <<= 1
        if i>0 and pi.read(pinMISO)==pigpio.HIGH:
            dataMISO |= 0x1
    pi.write(pinCS,1)
    time.sleep(0.001)
    return dataMISO
