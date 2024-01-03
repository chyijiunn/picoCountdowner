from machine import Pin ,PWM
from utime import sleep
servo = PWM(Pin(0))
buzzer = PWM(Pin(14))
LED = Pin(1,Pin.OUT)#控制LED
LED.value(1)

servo.freq(50)
servo.duty_u16(8500)
buzzer.freq(2000)
buzzer.duty_u16(0)

