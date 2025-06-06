from machine import Pin ,PWM
from utime import sleep
servo = PWM(Pin(0))
servo.freq(50)

servo.duty_u16(1600)#測試最小值
sleep(1)


