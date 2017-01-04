# clock.py
This is a simple clock app running aon a AdaFruit LED Ring (12 LEDS), driven by raspberry/raspbian

This is a quick demonstration of the 12 Neopixel ring of adafruit.
I've written it to become familiar with the properties of the multicolor LEDs.

Seconds, minutes and hours are represented by colors.
  * hours: cooresonding led is blue
  * minutes: all leds up to current minute led is shown white, increasing intensity
  * seconds: corresponding led ist shown red; additional, every second a red led runs around the circle

With my wiring, the green and red colors are switched (Don't know how to fix it).

THIS SCRIPT COMES WITH NO WARRANTY

Copyright Detlef Hüttemann (c) 2016 http://www.detlef-huettemann.com
