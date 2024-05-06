from machine import Pin ,PWM
from utime import sleep

servo = PWM(Pin(0))
servo.freq(50)

while 1: #當 1 出現時，重複進行此段落
    servo.duty_u16(1900)
    sleep(0.5)

    servo.duty_u16(8200)
    sleep(0.5)

