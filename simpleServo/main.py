# simpleServo example

from microbit import *
from simpleServo import *

#set a variable for each servo pin    
servo1 = simpleServo(pin0)
servo2 = simpleServo(pin15)
servo3 = simpleServo(pin16)

#loop the servos moving from one end stop to the other,
#followed by the servos returning to the centre
#then switch the servos off
while True:    
  servo1.write_angle(180)    
  servo2.write_angle(0)    
  servo3.write_angle(180)    
  sleep(1000)    
  servo1.write_angle(0)    
  servo2.write_angle(180)    
  servo3.write_angle(0)    
  sleep(1000)    
  servo1.write_angle(90)    
  servo2.write_angle(90)    
  servo3.write_angle(90)    
  sleep(1000)    
  servo1.stop()    
  servo2.stop()    
  servo3.stop()    
  sleep(1000)