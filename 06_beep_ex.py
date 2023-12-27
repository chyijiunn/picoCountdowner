import machine
import time

buzzer_pin = machine.Pin(2, machine.Pin.OUT)

buzzer_state = False
timer = machine.Timer()

def beep(timer):
    global buzzer_state
    buzzer_state = not buzzer_state  
    buzzer_pin.value(buzzer_state)

timer.init(period=1000, mode=machine.Timer.PERIODIC, callback=beep)