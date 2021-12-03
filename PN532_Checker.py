# The PN532_reset.py utility is designed to test the reader for operability. After launching the utility, 
# the reader will initialize and wait for the Tag to be read. 
# after successful reading, the utility will display the UID of the tag being read 

import RPi.GPIO as GPIO     # RaspberryPi 3B+ GPIO interfacing library
from pn532 import *         # PN532 driver
from pn532 import *
from time import sleep
import sys

GPIO.setwarnings(False)

if __name__ == '__main__':
    try:
        try:
            print('Waiting for RFID/NFC card...')
            i = 0
            while True:
                pn532 = PN532_UART(debug=False, reset=20)
                pn532.SAM_configuration()
                uid = pn532.read_passive_target(timeout=1)
                if uid is not None:
                    try:
                        i = i + 1
                        print('Found card with UID:', [hex(i) for i in uid], "read counter: ", i)
                        if(uid is None):
                            break
                    except nfc.PN532Error as e:
                        print(e)
            
                sleep(0.1)
                    
        except Exception as e:
            print(e)
        finally:
            GPIO.cleanup()
    
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(" Exit")
