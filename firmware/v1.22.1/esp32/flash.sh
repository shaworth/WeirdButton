#!/bin/bash

/usr/bin/python3 -u -m esptool --port /dev/ttyUSB0 --chip esp32 --baud 460800 write_flash -e --flash_size=detect -fm qio 0 ESP32_GENERIC-20240105-v1.22.1.bin

