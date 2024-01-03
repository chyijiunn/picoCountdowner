from machine import Pin ,PWM ,Timer
from utime import sleep
servo = PWM(Pin(0))
buzzer = PWM(Pin(14))
LED = Pin(1,Pin.OUT)#控制LED
servo.freq(50)
LED.value(1)

minset = 1
duty = 2000
motorend = 8000
tic = (motorend - duty) /minset /60 #每秒動多少

def beep():
    for j in range(2):
        for i in range(4):
            buzzer.freq(4000)
            buzzer.duty_u16(20000)
            sleep(0.15)
            buzzer.duty_u16(0)
            sleep(0.01)
        sleep(0.8)

def motor(tim):
    global duty
    servo.duty_u16(int(duty))
    duty = duty + tic
    if duty >= motorend:
        
        servo.duty_u16(2000)
        duty = 2000
        beep()
        
    restime = (motorend-duty)/tic
    restmin = int(restime // 60)
    restsec = int(restime % 60)
    print(restmin,':',restsec,duty)

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=motor)

