from machine import Pin
from utime import sleep

LED = Pin(25,Pin.OUT)

LED.value(1)
sleep(1)#睡了一秒鐘，那你會亮暗亮暗嗎？
LED.value(0)


