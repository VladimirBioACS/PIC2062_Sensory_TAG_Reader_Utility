# The PN532_reset.py utility is designed to enable the NFC field of the reader. 
# This utility is necessary for flashing the Tag, since a 13.56 MHz 
# reference clock source is required for flashing. 


import RPi.GPIO as GPIO     # RaspberryPi 3B+ GPIO interfacing library
from pn532 import *         # PN532 driver
from time import sleep
import sys

GPIO.setwarnings(False)

if __name__ == '__main__':
    try:

        pn532 = PN532_UART(debug=False, reset=20)

        ic, ver, rev, support = pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
        print("Field enabled")
        print("To exit press Ctrl^C")
        pn532.SAM_configuration()

        while True:
            try:
                uid = pn532.read_passive_target(timeout=500)
            except KeyboardInterrupt:
                GPIO.cleanup()
                sys.exit(" Exit")
                
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()