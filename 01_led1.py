from machine import Pin

LED = Pin(25,Pin.OUT)# 控制 LED  = GP1
LED.value(1)#通電就是 1