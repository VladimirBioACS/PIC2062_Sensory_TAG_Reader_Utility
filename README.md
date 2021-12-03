# PIC2062 Sensory TAG_ReaderUtility

This utility is designed to work with a PIC2062 NFC TAG device manufactured by Polaric Semiconductor © using an NFC PN532 reader. 

Before using this utility, you first need to update the system using the following commands:

 - sudo apt update
 - sudo apt upgrade

Next, you need to install the necessary modules. This can be done using the command:

 - sudo bash install_module.sh

Utility structure:

 - PIC2062_TAG_reader.py - script for reading and storing the data in log file from PIC2062 Sensory TAG and convert it into ADC and Voltage values.
 - PN532_Checker.py - script for TAG and reader checking
 - PN532_Field_Enable.py - script for NFC Field enabling (should be used while programing procedure)
 - PN532_Reset.py - script for PN532 reader reset

Additional description is present in .py files
