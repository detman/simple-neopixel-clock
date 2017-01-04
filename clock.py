#!/usr/bin/python

import time, sys
import datetime

from neopixel import *

LED_COUNT      = 12      # Number of LED pixels.
LED_CHANNEL    = 0       # PWM Channel (set to 1 when LED_PIN is 13 or 19, else 0)
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

## main

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

class ClockColor:

    def __init__(self,r=0,g=0,b=0):
        self.val = [r,g,b]
 
    def neopixelColor(self):
        return Color(self.val[0],self.val[1],self.val[2])

    def dim(self,frac):
        c = ClockColor()
        c.val = [int(i*frac) for i in self.val]
        return c

    def set(self,n):
        self.val = list(n.val)

    def addTo(self,n):
        self.val = [max(n.val[i],self.val[i]) for i in range(len(self.val))]

black = ClockColor(0,0,0)    # initial color of all leds in strip
col_s = ClockColor(0,255,0)  # color of second
col_m = ClockColor(64,0,64) # color of minute
col_h = ClockColor(255,0,0)  # color of hour

# debugging
#
# to specify hour and minute from cmd line, set debug_readdata to True
debug_readdate = False
#
# to speed up the clock, set rundelta to 1. This will increase the minute every loop.
debug_rundelta = 0

s_fac = 0
now = datetime.datetime.now()
try:
    while True:

        # set all leds to black

        pins = [ClockColor(0,0,0) for i in range(12)]
        
        if debug_rundelta == 0:
            now = datetime.datetime.now()
        else:
            now = now + datetime.timedelta(minutes=debug_rundelta)
        
        # set pin numbers for current second, minute, hour
        pin_s = now.second / 5  # 60 minutes / 12 leds = 5
        pin_m = now.minute / 5  # 60 minutes / 12 leds = 5
        pin_h = now.hour   % 12 # dont distinguish between 24 / 12 hour 
        
        if debug_readdate:
            pin_h,pin_m = raw_input('h m:').split()
            pin_h = int(pin_h)
            pin_m = int(pin_m)
            pin_m = pin_m / 5  # 60 minutes / 12 leds = 5
            pin_h = pin_h % 12 # dont distinguish between 24 / 12 hour 

        frac = ((now.second % 5) + now.microsecond / 1000000.0)/5.0
        s2 = (pin_s + 1) % 12

        # minute
        #
        # paint all leds up to pin_m with col_m, increasing intensity
        for i in range(pin_m):
            pins[i].set( col_m.dim(i/float(pin_m)) )
        pins[pin_m].set( col_m )

        # hour
        #
        # set pin_h led to col_h
        pins[pin_h].set(col_h)

        # second spinner
        #
        # set pin_h led to col_h
        # let a quick second wheel turn around; 1 cycle a second
        s3 = int(now.microsecond/1000000.0 * 12)
        pins[s3].addTo(col_s.dim(0.5))

        # second
        #
        # every time the quick wheel hits the second led, let it glow ... and dim down
        if s3 == pin_s:
            s_fac = 1.0
        elif s_fac > 0.1:
            s_fac = s_fac - 0.1
        # add col_s color for second led
        pins[pin_s].addTo( col_s.dim(s_fac) )

        for i in range(12):
            strip.setPixelColor(i,pins[i].neopixelColor())

        strip.show()
        time.sleep(0.05)


except KeyboardInterrupt:

    # clean up on ctrl-C
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()
    sys.exit()
