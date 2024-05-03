from machine import Pin ,PWM ,Timer
from utime import sleep
import _thread
servo = PWM(Pin(0))
buzzer = PWM(Pin(17))
LED = Pin(1,Pin.OUT)
servo.freq(50)
LED.value(1)

minset = 0.3#改這裡就好，1 = 一分鐘倒數，60 = 倒數一小時，若要八小時呢？ 
duty = 2000
motorend = 8000
duration = 2#每 2 秒動一次
tic = ((motorend - duty) /minset /60 )*duration

def beep():
    for j in range(2):
        for i in range(4):
            buzzer.freq(4000+i*100)
            buzzer.duty_u16(20000)
            sleep(0.03)
            buzzer.duty_u16(0)
            sleep(0.005)
        sleep(0.05)

def motor(tim):
    global duty
    servo.duty_u16(int(duty))
    duty = duty + tic
    if duty >= motorend:
        servo.duty_u16(2000)
        duty = 2000
        beep()

tim = Timer(-1)
tim.init(period=duration*1000, mode=Timer.PERIODIC, callback=motor)