import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(16), 16)

for i in range(16):
    strip[i] = (10*i,10,12)
    strip.write()
    time.sleep(0.01)