import os, machine
from machine import Pin

def blink(pinid):
    import time
    led = machine.Pin(pinid, machine.Pin.OUT)
    for i in range(2):
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        time.sleep(0.1)
    led.value(1)

def blink_onboard():
    blink(2)
    blink(2)
