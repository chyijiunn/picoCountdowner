# add beep function
from machine import Pin ,PWM ,Timer
from utime import sleep
servo = PWM(Pin(0))
buzzer = PWM(Pin(14))

servo.freq(50)
tic = 100
duty = 1600

def beep():
    for j in range(4):
        for i in range(4):
            buzzer.freq(4000)
            buzzer.duty_u16(1000)
            sleep(0.15)
            buzzer.duty_u16(0)
            sleep(0.01)
        sleep(0.8)
    
def motor(tim):
    global duty 
    servo.duty_u16(duty)
    duty = duty + tic
    if duty == 8200:
        duty = 1600
        beep()
    print(duty)

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=motor)