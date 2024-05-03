from machine import Pin ,PWM ,Timer
from utime import sleep
servo = PWM(Pin(0))
servo.freq(50)
tic = 100
duty = 2000

def motor(tim):
    global duty 
    servo.duty_u16(duty)
    duty = duty + tic
    if duty == 8500: duty = 2000
    print(duty)

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=motor)#每 1 秒 , 呼喚 motor 一次