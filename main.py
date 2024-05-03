from machine import Pin ,PWM ,Timer
from utime import sleep
from neopixel import NeoPixel

servo = PWM(Pin(0))
buzzer = PWM(Pin(14))
strip = NeoPixel(Pin(16), 9)
servo.freq(50)

minset = 0.12
duty = 1900
dutyini = 1900
motorend = 8450
tic = (motorend - duty) /minset /60 #每秒動多少
strip.fill(0,0,0)
strip.write()
def lampstripe():
    red = 255,0,0
    green = 0,255,0
    blue= 0,0,255
    colors = [red, green, blue]
    mydelay = 0.1
    while True:
        for j in colors:
            for i in range(8,0,-1):
                strip[i] = (j)
                sleep(mydelay)
                strip.write()
                
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
        beep()
        duty = dutyini
        servo.duty_u16(dutyini)
        lampstripe()

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=motor)