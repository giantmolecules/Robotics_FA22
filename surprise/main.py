# simple robot

from microbit import *
from simpleServo import *

armLeft = simpleServo(pin2,min_us=1000,max_us=2500)
armRight = simpleServo(pin8,min_us=1000,max_us=2500)

wheelLeft = simpleServo(pin15,min_us=1000,max_us=2500)
wheelRight = simpleServo(pin16,min_us=1000,max_us=2500)

armLeft.write_angle(180)
armRight.write_angle(0)

wheelLeft.write_angle(90)
wheelRight.write_angle(90)

display.show(Image.ASLEEP)

while True:
    eye0 = pin0.read_analog()
    eye1 = pin1.read_analog()
    print(eye0,eye1)
    if microphone.current_event()==SoundEvent.LOUD:
        display.show(Image.HAPPY)
        audio.play(Sound.GIGGLE)
        for x in range(10):
            armLeft.write_angle(100) 
            sleep(100)
            armRight.write_angle(80)  
            sleep(100)
            armLeft.write_angle(80)    
            sleep(100)
            armRight.write_angle(100)    
            sleep(100)
    else:
        display.show(Image.ASLEEP)
        armLeft.write_angle(180)
        armRight.write_angle(0)
        print(eye0,eye1)