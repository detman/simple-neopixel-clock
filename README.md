## clock.py
This is a simple clock app running on a AdaFruit LED Ring (12 LEDs), driven by raspberry/raspbian

This is a quick demonstration of the 12 Neopixel ring of adafruit.
I've written it to become familiar with the properties of the multicolor LEDs.

Seconds, minutes and hours are represented by colors.
  * hours: cooresonding led is blue
  * minutes: all leds up to current minute led is shown white, increasing intensity
  * seconds: corresponding led ist shown red; additional, every second a red led runs around the circle

To run it, type "sudo python clock.py"

led_0.py script just lights up LED 0 - to show up the orientation of the ring.
# caveat
With my wiring, the green and red colors are switched (Don't know how to fix it).

THIS SCRIPT COMES WITH NO WARRANTY

Copyright Detlef Hüttemann (c) 2016 http://www.detlef-huettemann.com
