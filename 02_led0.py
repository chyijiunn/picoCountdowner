from machine import Pin
from utime import sleep

LED = Pin(1,Pin.OUT)

LED.value(1)
LED.value(0)#斷電就是 0