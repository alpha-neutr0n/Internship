#This code only reads the values from the RFID
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
finally:
        GPIO.cleanup()
