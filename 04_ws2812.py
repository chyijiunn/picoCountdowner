import time
from machine import Pin
from neopixel import NeoPixel
# pin (16) and LEDs (9)
strip = NeoPixel(Pin(16), 9)

strip.fill((72,209,204))
strip.write()
#time.sleep(0.01)



