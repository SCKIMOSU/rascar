import RPi.GPIO as GPIO # import GPIO librery
import time

GPIO.setmode(GPIO.BOARD)

Motor1A = 12 #모터 1은 각각 12, 11, 35번 핀에 연결되어있다.
Motor1B = 11
Motor1E = 35

Motor2A = 15 
Motor2B = 13
Motor2E = 37

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

#initial motor forward setting 
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)


pwm=GPIO.PWM(Motor1E,100) 
pwm2=GPIO.PWM(Motor2E,100)

# starting it with 40% dutycycle


cnt=0;

try:
    while True:
        pwm.start(40) 
        pwm2.start(40)


except KeyboardInterrupt:
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    pwm.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    GPIO.cleanup()


