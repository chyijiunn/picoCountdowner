from machine import Pin
LED = Pin(25,Pin.OUT)

LED.value(1)
LED.value(0)#斷電就是 0