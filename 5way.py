import RPi.GPIO as GPIO # import GPIO librery
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)
        
OTD = 16
OTB = 18
OTA = 22
OTC = 40 
OTE = 32

GPIO.setup(OTD, GPIO.IN)
GPIO.setup(OTB, GPIO.IN)
GPIO.setup(OTA, GPIO.IN)
GPIO.setup(OTC, GPIO.IN)
GPIO.setup(OTE, GPIO.IN)

try:
    while True:
       print("OTD: " + str(GPIO.input(OTD)))
       print("OTB: " + str(GPIO.input(OTB)))
       print("OTA: " + str(GPIO.input(OTA)))
       print("OTC: " + str(GPIO.input(OTC)))
       print("OTE: " + str(GPIO.input(OTE)))
       sleep(2)
               
except KeyboardInterrupt:
    GPIO.cleanup()


