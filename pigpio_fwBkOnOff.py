import pigpio
import time

pi= pigpio.pi()

pinFW= 16
pinBK= 20
pi.set_mode(pinFW,pigpio.OUTPUT)
pi.set_mode(pinBK,pigpio.OUTPUT)

pi.write(pinFW,1)
pi.write(pinBK,0)
time.sleep(3)
pi.write(pinFW,0)
time.sleep(1)
pi.write(pinBK,1)
time.sleep(3)
pi.write(pinBK,0)

pi.stop()

