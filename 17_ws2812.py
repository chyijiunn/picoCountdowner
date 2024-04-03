import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(17), 16)

strip.fill((72,209,204))
strip.write()
#time.sleep(0.01)



