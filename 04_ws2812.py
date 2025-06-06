import time
from machine import Pin
from neopixel import NeoPixel
# pin (16) and LEDs (9)
strip = NeoPixel(Pin(16), 9)

strip.fill((255,0,0))
strip.write()
time.sleep(0.5)

strip.fill((255,255,0))
strip.write()
time.sleep(0.5)


