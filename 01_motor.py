from machine import Pin ,PWM
from utime import sleep

servo = PWM(Pin(6))
servo.freq(50)

while True:
    servo.duty_u16(4000)
    sleep(0.4)
    servo.duty_u16(5000)
    sleep(0.4)
