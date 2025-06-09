from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(14))
buzzer.freq(4000)

for j in range(3):
    for i in range(4):
        buzzer.duty_u16(1000)
        sleep(0.15)
        buzzer.duty_u16(0)#短暫的靜音
        sleep(0.01)
    sleep(0.8)

for j in range(3):
    for i in range(5):
        buzzer.freq(3000-i*500)#descending
        buzzer.duty_u16(10000)
        sleep(0.03)
        buzzer.duty_u16(0)
        sleep(0.02)
    for i in range(5):
        buzzer.freq(5000+i*1000)#ascending
        buzzer.duty_u16(20000)
        sleep(0.03)
        buzzer.duty_u16(0)
        sleep(0.02)
    sleep(0.02)
