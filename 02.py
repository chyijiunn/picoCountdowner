from machine import Pin ,PWM
from utime import sleep

servo = PWM(Pin(0))
servo.freq(50)


servo.duty_u16(2000)
sleep(0.4)
servo.duty_u16(3000)
sleep(0.4)
servo.duty_u16(4000)
sleep(0.4)
servo.duty_u16(5000)
sleep(0.4)
servo.duty_u16(6000)
sleep(0.4)
servo.duty_u16(7000)
sleep(0.4)
servo.duty_u16(8000)
sleep(0.4)



