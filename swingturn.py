import RPi.GPIO as GPIO # import GPIO librery
import time

GPIO.setmode(GPIO.BOARD)


MotorLeft_A = 12 
MotorLeft_B = 11
MotorLeft_PWM = 35

GPIO.setup(MotorLeft_A,GPIO.OUT)
GPIO.setup(MotorLeft_B,GPIO.OUT)
GPIO.setup(MotorLeft_PWM,GPIO.OUT)

#initial motor forward setting 
GPIO.output(MotorLeft_A,GPIO.HIGH)
GPIO.output(MotorLeft_B,GPIO.LOW)
GPIO.output(MotorLeft_PWM,GPIO.HIGH)

# create pwmLeft object
pwmLeft=GPIO.PWM(MotorLeft_PWM,100) 


try:
    while True:
        # starting left motor with 100% dutycycle
        pwmLeft.start(100)
        # chane dutycylce of left motor into 0%
        pwmLeft.ChangeDutyCycle(0)
        # contine 0.1 sec with 0% dutycylce 
        time.sleep(0.1)
        # trun left motor on again with 100% dutycycle 
        pwmLeft.start(100)
        # contine 0.1 sec with 100% dutycylce 
        time.sleep(0.1)
        

except KeyboardInterrupt: # when Ctrl+C is pressed
    #set the MotorLeft_PWM as LOW
    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    # chane dutycylce to 0%
    pwmLeft.ChangeDutyCycle(0)
    GPIO.cleanup()


