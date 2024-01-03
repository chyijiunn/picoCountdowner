from machine import Pin ,PWM
from utime import sleep

servo = PWM(Pin(0))
servo.freq(50)

while True:
    servo.duty_u16(1800)
    sleep(2)
    for i in range(64):
        servo.duty_u16(1800+100*i)
        sleep(0.1)
    servo.duty_u16(8200)
    sleep(0.6)
