from machine import Pin, PWM#PWM裡有個 類比 轉換概念
from utime import sleep

buzzer = PWM(Pin(14))#GP14
buzzer.freq(500)

buzzer.duty_u16(100)#喇叭的音量 100
sleep(0.5)

buzzer.duty_u16(200)#喇叭的音量 200
sleep(0.5)

buzzer.duty_u16(300)#喇叭的音量 300
sleep(0.5)

buzzer.duty_u16(400)
sleep(0.5)

buzzer.duty_u16(500)
sleep(0.5)

buzzer.duty_u16(0)