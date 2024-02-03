import os, machine, gc
from machine import Pin

print("Starting main2.py")

gc.collect()

def blink(pinid):
    import time
    led = machine.Pin(pinid, machine.Pin.OUT)
    for i in range(2):
        led.value(1)
        time.sleep(0.1)
        led.value(0)
        time.sleep(0.1)
    led.value(1)

blink(2)
blink(2)

no_ap()
do_connect()

blink(2)
blink(2)

exec(open('lcd_setup.py').read())

if is_lcd:
    lcd.clear()
    if sta_if.isconnected():
        lcd.print(sta_if.ifconfig()[0] + ":8266")
    else:
        lcd.print('BUTTON      ' + saystatus(True))
    lcd.set_cursor(0,1)
    lcd.print('LCD         ' + saystatus(is_lcd))
    lcd.set_cursor(0,2)
    lcd.print('EEPROM      ' + saystatus(is_mem))
    lcd.set_cursor(0,3)
    lcd.print('RTC         ' + saystatus(is_rtc))
    lcd.set_backlight(True)

enable_pin = machine.Pin(9, machine.Pin.Out)
enable_pin.value(0)
gc.collect()