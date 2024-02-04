import os, machine, gc
from machine import Pin

print("Starting main2.py")

gc.collect()


no_ap()
do_connect()
