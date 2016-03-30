#!/usr/local/bin/python
# takes two args: max led to light up, and the color to use
# it will turn off all leds > max led to light up
# specify color of "off" to turn off the LEDs

import sys
import time
from blinkstick import blinkstick

MAX_NUM_LEDS = 32

bstick = blinkstick.find_first()
highestLEDToLight = int(sys.argv[1])
ledColor = str(sys.argv[2])

for x in range(0, MAX_NUM_LEDS):
    if x < highestLEDToLight:  
        bstick.set_color(channel=0, index=x, name=ledColor)
    else:
        bstick.set_color(channel=0, index=x, name='#000000')

    time.sleep(.001)  # it seems if we don't have a minimal sleep blinkstick goes missing
    
