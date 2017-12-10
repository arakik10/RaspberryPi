import time

from wiringpiReadSpiADC import WpReadSpiAdc
wpRSA= WpReadSpiAdc()

try:
    v=[]
    while True:
	for i in range(2):
            v=v+[[]]
            print '{0:1d}:'.format(i),
            if i == 1:
                print ' ',
            for j in range(8):
                v[i]= v[i] + [wpRSA.readDataSpiADC(i,j)]
                print " {0:4d}".format(v[i][j]),
            print "\n",
        time.sleep(0.2)

except KeyboardInterrupt:
    pi.stop()
