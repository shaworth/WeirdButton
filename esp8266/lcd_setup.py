from lcd_i2c import LCD                                                                                                                           

print("running lcd_setup.py")

from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
devtree = i2c.scan()

# Check the I2C bus for LCD, EEPROM, and RTC
is_lcd = 39 in devtree
is_mem = 87 in devtree
is_rtc = 104 in devtree

if is_lcd:
    I2C_ADDR = 0x27     # DEC 39, HEX 0x27                                                                                                            
    NUM_ROWS = 4                                                                                                                                      
    NUM_COLS = 20  
    lcd = LCD(addr=I2C_ADDR, cols=NUM_COLS, rows=NUM_ROWS, i2c=i2c)
    lcd.begin()
    lcd.clear()
    lcd.set_backlight(False)

def saystatus(msg_status):
    if msg_status:
        return "[READY ]"
    else:
        return "[FAILED]"
