from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
devtree = i2c.scan()

# Check the I2C bus for LCD, EEPROM, and RTC
is_lcd = 39 in devtree
is_mem = 87 in devtree
is_rtc = 104 in devtree

