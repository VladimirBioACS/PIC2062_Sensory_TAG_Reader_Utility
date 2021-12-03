# The PN532_reset.py utility is designed to reboot the reader device 

import RPi.GPIO as GPIO     # RaspberryPi 3B+ GPIO interfacing library
from pn532 import *         # PN532 driver
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(rst_pin, GPIO.OUT)

def rst():
    GPIO.output(rst_pin, GPIO.LOW)
    sleep(0.10)
    GPIO.cleanup(rst_pin)


if __name__ == '__main__':
    try:
        pn532 = PN532_UART(debug=False, reset=20)
        ic, ver, rev, support = pn532.get_firmware_version()
        pn532.SAM_configuration()

        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
        print("Reset")

        rst()

    except Exception as e:
        print(e)
    
    finally:
        GPIO.cleanup()
