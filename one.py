#!/usr/bin/python

import time, sys
import datetime

from neopixel import *

LED_COUNT      = 12      # Number of LED pixels.
LED_CHANNEL    = 0       # PWM Channel (set to 1 when LED_PIN is 13 or 19, else 0)
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

## main

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()


strip.setPixelColor(0,Color(255,255,255))
strip.show()

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, 0)
    strip.show()
    sys.exit()
