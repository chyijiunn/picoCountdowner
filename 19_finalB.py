from machine import Pin ,PWM ,Timer
from utime import sleep
from neopixel import NeoPixel
import utime
servo = PWM(Pin(0))
buzzer = PWM(Pin(14))
strip = NeoPixel(Pin(16), 9)
servo.freq(50)

strip.fill((205,55,155))
strip.write()

minset = 1
duty = 2000
motorend = 8400

tic = int((motorend - duty) /minset /60) #每秒動多少
lightTic = (motorend - duty)/minset/60/255

def beep():
    for j in range(2):
        for i in range(4):
            buzzer.freq(4000)
            buzzer.duty_u16(20000)
            sleep(0.15)
            buzzer.duty_u16(0)
            sleep(0.01)
        sleep(0.8)

for i in range(duty , motorend , tic):
    servo.duty_u16(int(i))
    sleep(1)