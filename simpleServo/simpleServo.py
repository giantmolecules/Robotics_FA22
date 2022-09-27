# microbit-module: KitronikSimpleServo@1.0.0
# Copyright (c) Kitronik Ltd 2021. 
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

class simpleServo:
    #Simple Servo module is used with the 5673 - Simple Servo board
    #The servo connections to the BBC micro:bit on this product are pins 8 (servo1), 15 (servo2) and 16 (servo3)
    #initalise servo pin with frequency and time period
    def __init__(self, pin, freq=50, min_us=700, max_us=2300, angle=180):
        self.pin = pin
        self.freq = freq
        self.min_us = min_us
        self.max_us = max_us
        self.angle = angle
        self.us = 0
        self.analog_period = 0
        analog_period = round((1/self.freq) * 1000)
        self.pin.set_analog_period(analog_period)
        
    #write the frequency to the analog pin
    def write_us(self, us):
        self.us = min(self.max_us, max(self.min_us, us))
        analog_op = round(self.us * 1024 * self.freq // 1000000)
        self.pin.write_analog(analog_op)
        
    #call function to set the angle    
    def write_angle(self, degrees=0):
        degrees = degrees // 1
        pulse_range = self.max_us - self.min_us
        self.us = self.min_us + (pulse_range * degrees) // self.angle
        self.write_us(self.us)
        
    #call function to stop the servo beingdriven    
    def stop(self):
        self.pin.write_digital(0)

