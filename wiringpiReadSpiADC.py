import wiringpi
import time

class WpReadSpiAdc(object):

    def __init__ ( self ):

        self.PinCLK   = 11
        self.PinMISO  =  9
        self.PinMOSI  = 10
        self.PinCS    = [8,7]

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.PinCLK,  wiringpi.GPIO.OUTPUT)
        wiringpi.pinMode(self.PinMISO, wiringpi.GPIO.INPUT)
        wiringpi.pinMode(self.PinMOSI, wiringpi.GPIO.OUTPUT)
        wiringpi.pinMode(self.PinCS[0],wiringpi.GPIO.OUTPUT)
        wiringpi.pinMode(self.PinCS[1],wiringpi.GPIO.OUTPUT)

    def readDataSpiADC ( numSS, numCH ):
        #                  |      |
        # spi device number: 0-1  |
        # ADconverter chanel number: 0-7

        if numCH > 7 or numCH < 0:
            return -1
        wiringpi.digitalWrite(self.PinCS[numSS],1)
        wiringpi.digitalWrite(self.PinCLK,0)
        wiringpi.digitalWrite(self.PinCS[numSS],0)
        dataMOSI = numCH
        dataMOSI |= 0x18
        dataMOSI <<= 3
        for i in range(5):
            if dataMOSI & 0x80:
                wiringpi.digitalWrite(self.PinMOSI,1)
            else:
                wiringpi.digitalWrite(self.PinMOSI,0)
            dataMOSI <<= 1
            wiringpi.digitalWrite(self.PinCLK,1)
            wiringpi.digitalWrite(self.PinCLK,0)
        dataMISO = 0
        for i in range(13):
            wiringpi.digitalWrite(self.PinCLK,1)
            wiringpi.digitalWrite(self.PinCLK,0)
            dataMISO <<= 1
            if i>0 and wiringpi.digitalRead(self.PinMISO)==1:
                dataMISO |= 0x1
        wiringpi.digitalWrite(self.PinCS[numSS],1)
        time.sleep(0.001)
        return dataMISO
