#!/usr/local/bin/python
# takes two args: 
#   argv[1]:  max LED to light up in the strip of LEDs
#   argv[2]:  color to use to light the LEDs, "off" to turn them off
#
# This is just a super-simple script to allow other monitoring types
# of apps to use this and indicate things for me on the blinkstick.
# See http://www.blinkstick.com
#
# The blinkstick has a very small amount of storage (something like 32 bytes)
# so we'll store how many LEDs are lit in this block, so we don't have to
# do too much LED manipulation on LEDs that are already off.  I'm not sure
# how much this saves us, I just wanted to play w/ the onboard storage.

import sys
import time
from blinkstick import blinkstick

MAX_NUM_LEDS = 32
bstick = blinkstick.find_first()

def usage():
    print "Usage:  simpleled.py max_leds_to_light color"
    print "where color is any named color like red, blue, etc., off to turn them off"

def lightLEDs(ledsToLight, maxLEDs, color):
    try:
        for x in range(0, maxLEDs):
            if x < ledsToLight:
                bstick.set_color(channel=0, index=x, name=color)
                #bstick.blink(channel=0, index=x, name=color, repeats=100000000)
            else:
                bstick.set_color(channel=0, index=x, name='#000000')

            time.sleep(.001)  # it seems if we don't have a minimal sleep blinkstick goes missing

        bstick.set_info_block1(str(ledsToLight));
        #print "Stored " + str(ledsToLight) + " in on-strip memory"
    except KeyboardInterrupt:
        #bstick.off()
        return




def main():
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    highestLEDToLight = int(sys.argv[1])
    ledColor = str(sys.argv[2])
    storedLEDsLit = int(bstick.get_info_block1())

    if highestLEDToLight < storedLEDsLit:
        lightLEDs(highestLEDToLight, storedLEDsLit, ledColor)
    else:
        lightLEDs(highestLEDToLight, highestLEDToLight, ledColor)

if __name__ == "__main__":
    sys.exit(main())
