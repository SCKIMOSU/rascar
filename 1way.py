import RPi.GPIO as GPIO # import GPIO librery
import time

GPIO.setmode(GPIO.BOARD)

Motor1A = 12 #모터 1은 각각 12, 11, 35번 핀에 연결되어있다.
Motor1B = 11
Motor1E = 35

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

#initial motor forward setting 
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)


pwm=GPIO.PWM(Motor1E,100) 

cnt=0;

try:
    while True:
        # starting it with 40% dutycycle
        pwm.start(40) 

except KeyboardInterrupt:
    GPIO.output(Motor1E,GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    GPIO.cleanup()


