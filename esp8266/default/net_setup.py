import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('nerdhenge', '+virginia1234')
sta_if.ifconfig()

import mip

os.mkdir("/lib")
mip.install("github:brainelectronics/micropython-i2c-lcd/")

import webrepl_setup
