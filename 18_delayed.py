from machine import Pin ,PWM ,Timer
from utime import sleep
from neopixel import NeoPixel
import utime
servo = PWM(Pin(0))
buzzer = PWM(Pin(14))
strip = NeoPixel(Pin(16), 9)
servo.freq(50)

strip.fill((255,255,255))
strip.write()

minset = 1
duty = 1600
motorend = 8200

tic = int((motorend - duty) /minset /60) #每秒動多少

def beep():
    for j in range(2):
        for i in range(4):
            buzzer.freq(4000)
            buzzer.duty_u16(20000)
            sleep(0.15)
            buzzer.duty_u16(0)
            sleep(0.01)
        sleep(0.8)

while 1:
    for i in range(duty , motorend , tic):
        servo.duty_u16(int(i))
        strip.fill((255,int(255-(i/33)),int(255-(i/33))))
        strip.write()
        sleep(1)#這 delay 造成時間上不準
    beep()