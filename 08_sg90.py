from machine import Pin ,PWM
from utime import sleep
servo = PWM(Pin(0))
servo.freq(50)

servo.duty_u16(2000)#測試最小值
sleep(0.5)

servo.duty_u16(8340)#測試最大值
sleep(0.5)
