import time
from machine import Pin, ADC
from neopixel import NeoPixel

strip = NeoPixel(Pin(16), 9)
potentiometer = ADC(Pin(26))
# Color
c1 = 255,0,0
c2 = 0,255,255
c3 = 255,255,255
colors = [c1, c2, c3]
mydelay = 0.1
while True:
    for j in colors:
        for i in range(8):
            strip[i] = (j)
            time.sleep(mydelay)
            strip.write()

