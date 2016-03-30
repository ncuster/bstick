#!/usr/local/bin/python
# takes two args: max led to light up, and the color to use
# it will turn off all leds > max led to light up
# specify color of "off" to turn off the LEDs
#
# this is super-simple and just very basic, but still some have
# some basic error checking added at some point.   right now i
# just use it to tell me how many IMs i have unread by putting
# in a simple trigger on IM signal.

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
    
