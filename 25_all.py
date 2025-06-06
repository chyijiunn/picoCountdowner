# teacherVersion 加入燈條於 motor function 下
from machine import Pin ,PWM ,Timer
from utime import sleep
from neopixel import NeoPixel
import _thread
servo = PWM(Pin(0))
buzzer = PWM(Pin(14))
strip = NeoPixel(Pin(16), 9)
servo.freq(50)
strip.fill((0,0,255))
strip.write()

minset = 1 #改這裡就好，1 = 一分鐘倒數，60 = 倒數一小時，若要八小時呢？ 
duty = 1600
motorend = 8200
duration = 1 #每多少秒動一次
tic = ((motorend - duty) /minset /60 )*duration

def beep():
    for j in range(8):
        for i in range(5):
            buzzer.freq(3000-i*500)
            buzzer.duty_u16(10000)
            sleep(0.03)
            buzzer.duty_u16(0)
            sleep(0.02)
        for i in range(5):
            buzzer.freq(5000+i*1000)
            buzzer.duty_u16(20000)
            sleep(0.03)
            buzzer.duty_u16(0)
            sleep(0.02)
        sleep(0.02)

def motor(tim):
    global duty
    servo.duty_u16(int(duty))
    duty = duty + tic
    ledshift = int(duty/33)
    strip.fill((ledshift,0,255-ledshift))
    strip.write()
    if duty >= motorend:
        servo.duty_u16(1600)
        duty = 1600
        beep()

tim = Timer(-1)
tim.init(period=int(duration*1000), mode=Timer.PERIODIC, callback=motor)
