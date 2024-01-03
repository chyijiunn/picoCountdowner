from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(14))

for i in range(100,1000,100):
    buzzer.freq(i)
    buzzer.duty_u16(1000)
    sleep(0.5)
    buzzer.duty_u16(0)


