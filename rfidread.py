# sudo nano writetest.py 
# sudo pip3 install mfrc522
# sudo raspi-config
# Interfacing option -> enable the SPI and finish
# sudo nano read.py
# sudo python3 writetest.py 


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Place your card:")
    id, text = reader.read()
    print("ID:", id)
    print("Text:", text)
finally:
    GPIO.cleanup()
