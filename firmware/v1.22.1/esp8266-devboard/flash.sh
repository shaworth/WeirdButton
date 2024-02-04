#!/bin/bash

/usr/bin/python3 -u -m esptool --port /dev/ttyUSB0 --chip esp8266 --baud 115200 write_flash -e --flash_size=detect -fm dio 0 ESP8266_GENERIC-20240105-v1.22.1.bin
