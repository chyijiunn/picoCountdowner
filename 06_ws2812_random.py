import time , random
from machine import Pin
from neopixel import NeoPixel
# 腳位 16 & 9顆 LEDs
strip = NeoPixel(Pin(16), 9)

strip.fill((255,0,0))#R,G,B
strip.write()
time.sleep(0.5)

strip.fill((0,0,0))
strip.write()
time.sleep(0.5)

a = []

for j in range(8):
    a.clear()
    for i in range(3):
        a.append(random.randint(0,255))

    strip[8] = a
    strip.write()
    time.sleep(0.5)
    print(a)
