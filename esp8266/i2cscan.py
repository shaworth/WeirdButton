import os, machine
from machine import I2C, Pin
from lcd_i2c import LCD                                                                                                                           

I2C_ADDR = 0x27     # DEC 39, HEX 0x27                                                                                                            
NUM_ROWS = 4                                                                                                                                      
NUM_COLS = 20  

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
lcd.begin()
lcd.set_backlight(False)


def doi2cscan():
    i2c.scan()
    
def startup_screen():
    lcd.clear()
    lcd.print('WeirdButton')
    lcd.set_cursor(0,1)
    lcd.print('Copyright (c) 2024')
    lcd.set_cursor(0,2)
    lcd.print('By Shannon Haworth')
    lcd.set_cursor(0,3)
    lcd.print('All rights reserved')
    lcd.set_backlight(True)
    
def blank_screen():
    lcd.clear()
    lcd.set_backlight(False)

def debug_mode():
    
