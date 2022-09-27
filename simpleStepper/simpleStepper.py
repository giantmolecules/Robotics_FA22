# microbit-module: simpleStepper@1.0
# Copyright (c) Brett Ian Balogh 2022. 
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import microbit
import utime

class simpleStepper:
    pins=[microbit.pin0, 
          microbit.pin1, 
          microbit.pin2, 
          microbit.pin3, 
          microbit.pin4, 
          microbit.pin5, 
          microbit.pin6, 
          microbit.pin7, 
          microbit.pin8, 
          microbit.pin9, 
          microbit.pin10, 
          microbit.pin11, 
          microbit.pin12, 
          microbit.pin13, 
          microbit.pin14, 
          microbit.pin15, 
          microbit.pin16]
    
    patterns = [[0,1,0,1],
                [0,1,1,0],
                [1,0,1,0],
                [1,0,0,1]]
    
    
    def __init__(self,pinA=0,pinB=1,pinC=2,pinD=3):
        import utime
        #display.off()
        self.pinA =  pinA
        self.pinB =  pinB
        self.pinC =  pinC
        self.pinD =  pinD
        self.direction = "fwd"
        self.counter = 0
        self.steps = 0

    def step(self, num, direction, speed=100):
        speed = 100-speed+5
        if direction == "fwd" or direction == 0:
            self.steps=0
            while self.steps <= num:
                print(self.counter,':',self.patterns[self.counter][0],self.patterns[self.counter][1],self.patterns[self.counter][2],self.patterns[self.counter][3])
                self.pins[self.pinA].write_digital(self.patterns[self.counter][0])
                self.pins[self.pinB].write_digital(self.patterns[self.counter][1])
                self.pins[self.pinC].write_digital(self.patterns[self.counter][2])
                self.pins[self.pinD].write_digital(self.patterns[self.counter][3])
                self.steps = self.steps+1
                self.counter = self.counter+1
                if self.counter > 3:
                    self.counter = 0
                utime.sleep_ms(speed)
                
        if direction == "rev" or direction == 1:
            self.steps=0
            while self.steps <= num:
                print(self.counter,':',self.patterns[self.counter][0],self.patterns[self.counter][1],self.patterns[self.counter][2],self.patterns[self.counter][3])
                self.pins[self.pinA].write_digital(self.patterns[self.counter][3])
                self.pins[self.pinB].write_digital(self.patterns[self.counter][2])
                self.pins[self.pinC].write_digital(self.patterns[self.counter][1])
                self.pins[self.pinD].write_digital(self.patterns[self.counter][0])
                self.steps = self.steps+1
                self.counter = self.counter+1
                if self.counter > 3:
                    self.counter = 0
                utime.sleep_ms(speed)