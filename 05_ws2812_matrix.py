import time
from machine import Pin
from neopixel import NeoPixel
# 腳位 16 & 9顆 LEDs
strip = NeoPixel(Pin(16), 9)

colors = [
    (255, 0, 0),  # LED 1 - 紅色
    (0, 0, 0),    # LED 2 - 關閉
    (0, 255, 0),  # LED 3 - 綠色
    (0, 0, 0),    # LED 4 - 關閉
    (0, 0, 255),  # LED 5 - 藍色
    (0, 0, 0),    # LED 6 - 關閉
    (255, 255, 0),# LED 7 - 黃色
    (0, 0, 0),    # LED 8 - 關閉
    (0, 0, 0)     # LED 9 - 關閉
]
for i in range(9):
    strip[i] = colors[i]
strip.write()




