from machine import Pin ,PWM
from utime import sleep

servo = PWM(Pin(6))
servo.freq(50)
servo.duty_u16(5000)

