import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(16), 9)

delay = 1/120
while True: 
    for i in range(1,255,1):# Fill
        strip.fill((i,0,0))
        strip.write()
        time.sleep(delay)

    for i in range(255,1,-1):# Fade
        strip.fill((i,0,0))
        strip.write()
        time.sleep(delay)
#若要顏色從綠變成紅應該怎麼改？