#!/usr/bin/env python3
import time
import serial

phone = serial.Serial("/dev/quectel0-data", 115200, timeout=5)
try:
    time.sleep(0.5)
    phone.write(b'AT\r')
    time.sleep(0.5)
    phone.write(b'AT+CFUN=1\r') # Turn the modem on
    time.sleep(10)
    phone.write(b'AT+VOLTESETTING=1\r') # Enable VoLTE
    time.sleep(0.5)
    phone.write(b'AT+CNV=/nv/item_files/modem/mmode/ue_usage_setting,0,01,1\r') # Enable VoLTE
    time.sleep(0.5)
    phone.write(b'AT+CNMP=2\r') # Set network technology to 'All'
finally:
    phone.close()
