#!/usr/bin/env python3
import time
import serial

print('Modem init... opening serial port.')

phone = serial.Serial("/dev/quectel0-data", 115200, timeout=5)
try:
    time.sleep(0.5)
    phone.write(b'AT\r')
    time.sleep(0.5)
    print('Enabling modem...')
    phone.write(b'AT+CFUN=1\r') # Turn the modem on
    time.sleep(10)
    print('Enabling VoLTE...')
    phone.write(b'AT+VOLTESETTING=1\r') # Enable VoLTE
    time.sleep(0.5)
    phone.write(b'AT+CNV=/nv/item_files/modem/mmode/ue_usage_setting,0,01,1\r') # Enable VoLTE
    time.sleep(0.5)
    print('Setting RATs...')
    phone.write(b'AT+CNMP=2\r') # Set network technology to 'All'
    time.sleep(0.5)
    print(Setting mic and out gain...)
    phone.write(b'AT+CMICGAIN=1\r') # Set mic gain
    time.sleep(0.5)
    phone.write(b'AT+COUTGAIN=1\r') # Set out gain
finally:
    time.sleep(0.5)
    phone.close()
