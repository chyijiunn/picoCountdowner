import time
from machine import Pin
from neopixel import NeoPixel
# 腳位 16 & 9顆 LEDs
strip = NeoPixel(Pin(16), 9)

colors = [
    (80, 0, 255),   # 偏藍紫
    (100, 0, 220),
    (120, 0, 190),
    (140, 0, 160),
    (160, 0, 130),  # 純紫中間值
    (180, 0, 100),
    (200, 0, 70),
    (220, 0, 40),
    (240, 0, 20),   # 偏紅紫
]
for i in range(9):
    strip[i] = colors[i]
strip.write()