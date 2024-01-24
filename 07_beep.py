from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(14))
buzzer.freq(4000)

for j in range(4):
    for i in range(4):
        buzzer.duty_u16(1000)
        sleep(0.15)
        buzzer.duty_u16(0)#短暫的靜音
        sleep(0.01)
    sleep(0.8)