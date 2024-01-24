from machine import Pin ,PWM
from utime import sleep

servo = PWM(Pin(0))
servo.freq(50)

while True:
    servo.duty_u16(1800)
    sleep(2)
    
    for i in range(64):# for 迴圈 執行
        servo.duty_u16(1800+100*i)#每次都會增加 100，做 64 次
        sleep(0.1)
        
    servo.duty_u16(8200)
    sleep(0.6)
