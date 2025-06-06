import time
from machine import Pin
from neopixel import NeoPixel
strip = NeoPixel(Pin(16), 9)# 腳位 16 & 9顆 LEDs

strip[4] = (80, 0, 255)#為 list 格式， [0]代表第 1 個 , [1]代表第 2 個
strip.write()