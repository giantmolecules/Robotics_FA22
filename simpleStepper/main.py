# simpleStepper example

from microbit import *
from simpleStepper import *

stepper = simpleStepper(0,1,2,8)

while True:
    stepper.step(2048,0)
    sleep(1000)
    stepper.step(2048,1)
    sleep(1000)
