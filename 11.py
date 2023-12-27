from machine import Pin ,PWM ,Timer
from utime import sleep
servo = PWM(Pin(6))
buzzer = PWM(Pin(2))
servo.freq(50)

minset = 2
duty = 2000
motorend = 8000
tic = (motorend - duty) /minset /60 #每秒動多少

def beep():
    for j in range(4):
        for i in range(4):
            buzzer.freq(4000)
            buzzer.duty_u16(2000)
            sleep(0.15)
            buzzer.duty_u16(0)
            sleep(0.01)
        sleep(0.8)
    
def motor(tim):
    global duty 
    servo.duty_u16(int(duty))
    duty = duty + tic
    if duty >= motorend:
        duty = 2000
        beep()
    restime = (motorend-duty)/tic
    restmin = int(restime // 60)
    restsec = int(restime % 60)
    print(restmin,':',restsec)

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=motor)

