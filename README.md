# PIC2062 Sensory TAG Reader Utility

This utility is designed to work with a PIC2062 NFC TAG device manufactured by Polaric Semiconductor © using an NFC PN532 reader. 

Before using this utility, you first need to update the system using the following commands:

 - sudo apt update
 - sudo apt upgrade

Next, you need to install the necessary modules. This can be done using the command:

 - sudo bash install_module.sh

**Utility structure:**

 - PIC2062_TAG_reader.py - script for reading and storing the data in log file from PIC2062 Sensory TAG and convert it into ADC and Voltage values.
 - PN532_Checker.py - script for TAG and reader checking
 - PN532_Field_Enable.py - script for NFC Field enabling (should be used while programing procedure)
 - PN532_Reset.py - script for PN532 reader reset

Additional description is present in .py files

The Polaric_TAG_reader utility is designed to establish communication between the NFC TAG pic2062 and the NFC reader PN532.
pic2062 works on the NFC-A type-2 protocol.
pic2062 is a TAG sensor with 10 bit ADC support.
ADC data is stored in memory blocks under the index [6] and [7] of the device.
Reading occurs instantly after the NFC communication is established between the TAG and the reader.
This utility dumps the TAG memory and formats its output into a decimal code, which corresponds to the read voltage by channel 7 of the ADC.

**ADC parameters:**

The TAG uses an external 10-bit ADC (MCP3008) with a fixed reference voltage of 1.8 volts. 
Data sampling occurs on the 7th channel of the ADC and the calculated voltage is calculated according to the following formula:
(adc_val * adc_vref) / adc_resolution - adc _vref = 1.8; adc_resolution = 1024 

**WIRING DIAGRAM:**

                                    -----------------------            -------------------------
                                    |                     |            |                       |
                                    |                  TxD| ---------> |RxD                    |
                                    | RaspberryPi 3B+  RxD| <--------- |RxD  PN532 NFC Reader  |
                                    |                  GND| ---------- |GND                    |
                                    |                  3V3| ---------> |3V3                    |
                                    |                     |            |                       |
                                    -----------------------            -------------------------

**PN532 INTERFACE SWITCH MODE:**

                                                             -------
                                                       SCK   | OFF |
                                                       MISO  | OFF |  
                                                       MOSI  | OFF |  SPI
                                                       NSS   | OFF |  
                                                       SCL   | OFF |  I2C
                                                       SDA   | OFF |
                                                       RX    | ON  |  UART
                                                       TX    | ON  |
                                                             -------

**PN532 JUMPERS MODE:**

                                       -----------------      ---------------
                                       |bus |  H  | I0 |      |Signal| Short|
                                       -----------------      ---------------
                                       |UART|  L  | H  |      |RSTPDN| D16  |
                                       -----------------      ---------------
                                                              |INT0  | D20  |
                                                              ---------------
