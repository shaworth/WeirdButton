import os, machine, network
from machine import Pin

is_lcd = False

button = Pin(12, Pin.IN, Pin.PULL_UP)
normal_boot = button.value()

sta_if = network.WLAN(network.STA_IF)

def do_connect():
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('nerdhenge', '+virginia1234')
        while not sta_if.isconnected():
            pass
        if is_lcd:
            startup_screen()

def no_ap():
    ap = network.WLAN(network.AP_IF) # create access-point interface
    ap.active(False)         # activate the interface

# Proceed to boot normally based on the state of Pin 12
if normal_boot:
    exec(open("main2.py").read())
else:
    no_ap()
    do_connect()    
