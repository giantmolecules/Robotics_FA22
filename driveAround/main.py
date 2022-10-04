from microbit import *
from simpleServo import *

def fwd(speed):
    wheelLeft.write_angle(speed)
    wheelRight.write_angle(-speed)

def rev(speed):
        wheelLeft.write_angle(-speed)
        wheelRight.write_angle(speed)

def right(speed):
        wheelLeft.write_angle(speed)
        wheelRight.write_angle(speed)

def left(speed):
    wheelLeft.write_angle(-speed)
    wheelRight.write_angle(-speed)   

def stop():
        wheelLeft.stop()
        wheelRight.stop()
    

wheelLeft = simpleServo(pin15,min_us=1000,max_us=2500)
wheelRight = simpleServo(pin16,min_us=1000,max_us=2500)

while True:

    fwd(100)
    sleep(3000)
    stop()
    sleep(1000)
    right(100)
    sleep(3000)
    stop()
    sleep(1000)
    rev(100)
    sleep(3000)
    stop()
    sleep(1000)
    right(100)
    sleep(3000)
    stop()
    sleep(1000)
