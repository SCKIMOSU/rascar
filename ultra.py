import RPi.GPIO as GPIO
import time  
from time import sleep

def ultra():

    GPIO.setmode(GPIO.BOARD)

    trig=33
    echo=31

    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)
    GPIO.setwarnings(False)

    try:
        while True:
            GPIO.output(trig,False)
            time.sleep(0.5)
            GPIO.output(trig,True)
            time.sleep(0.00001)
            GPIO.output(trig,False)
            while GPIO.input(echo)==0:
                pulse_start=time.time()
            while GPIO.input(echo)==1:
                pulse_end=time.time()
            pulse_duration=pulse_end-pulse_start
            distance=pulse_duration*17000
             
            print(distance)
      
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    ultra()



