# The Polaric_TAG_reader utility is designed to establish communication between the NFC TAG pic2062 and the NFC reader PN532.
# pic2062 works on the NFC-A type-2 protocol.
# pic2062 is a TAG sensor with 10 bit ADC support.
# ADC data is stored in memory blocks under the index [6] and [7] of the device.
# Reading occurs instantly after the NFC communication is established between the TAG and the reader.
# This utility dumps the TAG memory and formats its output into a decimal code, which corresponds to the read voltage by channel 7 of the ADC.

import RPi.GPIO as GPIO         # RaspberryPi 3B+ GPIO interfacing library
import pn532.pn532 as nfc       # PN532 interfacing library
from pn532 import *             # PN532 driver
import datetime
from time import sleep
from termcolor import colored
import os
import sys

# Config
nfc_read_delay = 0.1

# ADC parameters
adc_resolution = 1023
adc_vref_config = 1.8

# Log file path
log_file = open('log/log.log', 'a')

# PN532 & GPIO setup
GPIO.setwarnings(False)

# Write data to LOG file
def append_to_log(prefix, sample, date):
    try:
        log_file.write("[" + date + "][" + prefix + "]: " + str(sample) + "\n")
    except Exception as e:
        print(colored(e.errmsg,"red"))

# Converts ADC sample into voltage
def sample_to_voltage(adc_val):
     return (adc_val * adc_vref_config)/adc_resolution

# Read TAG device, dump TAG memory and convert it into ADC decimal code
def nfc_read():
    try:
        # PN532 driver setup
        pn532 = PN532_UART(debug=False, reset=20)
        pn532.SAM_configuration()
        uid = pn532.read_passive_target(timeout=nfc_read_delay)

        if uid is not None:

            print(colored("TAG detected","green"))
            tag_UID = [hex(i) for i in uid]
            print(colored('Found TAG with UID:'+ str(tag_UID) + "\n", "green"))

            while True:
                uid = pn532.read_passive_target(timeout=nfc_read_delay)
                
                first_block_sample_store = 0
                second_block_sample_store = 0

                first_block_sample_store = ''.join(['%02x' % x for x in pn532.ntag2xx_read_block(6)])
                second_block_sample_store  = ''.join(['%02x' % x for x in pn532.ntag2xx_read_block(7)])
                        
                block = first_block_sample_store + second_block_sample_store

                try:
                    ph_sample = int(block[3:-10], 16)
                    ph_voltage = sample_to_voltage(ph_sample)

                    print("Sensor ADC sample: ", ph_sample)
                    print("Sensor voltage: ", round(ph_voltage, 2), "V\n")

                    append_to_log("ADC voltage: ", round(ph_voltage, 2), str(datetime.datetime.now()))
                    append_to_log("ADC sample: ", ph_sample, str(datetime.datetime.now()))

                except nfc.PN532Error as e:
                    print(colored(e.errmsg,"red"))
                    log_file.close()
                    GPIO.cleanup()
                    sys.exit(e)
                
        sleep(0.1)

    except Exception as e:
        print(colored(e,"red"))

# Main function
if __name__ == "__main__":

    os.system("clear")
    os.system("figlet Polaric Semi")

    print(colored("Testbench v2.0\n","green"))

    print("Polaric NFC sensory TAG reader v1.0")
    print("To exit press Ctrl^C\n")
    print('Waiting for TAG...')
    
    try:
        while True:
            nfc_read()

    except KeyboardInterrupt:
        append_to_log("INFO: ","EXIT", str(datetime.datetime.now()))
        log_file.close()
        GPIO.cleanup()
        sys.exit(" Exit")