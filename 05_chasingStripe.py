import time
from machine import Pin, ADC
from neopixel import NeoPixel

strip = NeoPixel(Pin(16), 9)
potentiometer = ADC(Pin(26))
# Color
red = 255,0,0
green = 0,255,0
blue= 0,0,255
colors = [red, green, blue]
mydelay = 0.1
while True:
    for j in colors:
        for i in range(8,0,-1):
            strip[i] = (j)
            time.sleep(mydelay)
            strip.write()
