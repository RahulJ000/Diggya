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
