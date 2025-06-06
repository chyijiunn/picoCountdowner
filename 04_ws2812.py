import time
from machine import Pin
from neopixel import NeoPixel
# 腳位 16 & 9顆 LEDs
strip = NeoPixel(Pin(16), 9)

strip.fill((255,0,0))#R,G,B
strip.write()
time.sleep(0.5)

strip.fill((255,255,0))
strip.write()
time.sleep(0.5)


