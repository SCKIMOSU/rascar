######################################################################
### Date: 2017/10/1
### Purpose: this code has been generated for the three-wheeled moving
###         object to go forward and backward
### this code is used for the student only
######################################################################

# import GPIO  library
import RPi.GPIO as GPIO 
from time import sleep

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)


# set GPIO warnings as false
GPIO.setwarnings(False)

# =======================================================================
# REVERSE function to control the direction of motor in reverse
def REVERSE(x):
   if x == 'True':
      return 'False'
   elif x == 'False':
      return 'True'
# =======================================================================

# =======================================================================
# Set the motor's true / false value to go forward.  
forward0 = 'True'
forward1 = 'False'
# =======================================================================

# ======================================================================= 
#Set the motor's true / false value to the opposite.
backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)
# =======================================================================

# =======================================================================
# declare the pins of 12, 11, 35 in the Raspberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled

# (this codes includes
# the initialization the connection between left motor and Raspberry Pi)
# (this codes includes
# the connection between left motor and Raspberry Pi by software)
# =======================================================================
MotorLeft_A = 12 
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Raspberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled

# (this codes includes
# the initialization the connection between right motor and Raspberry Pi
# (this codes includes
# the connection between right motor and Raspberry Pi by software
# =======================================================================

MotorRight_A = 15 
MotorRight_B = 13
MotorRight_PWM = 37


# ===========================================================================
# Control the DC motor to make it rotate clockwise, so the car will 
# move forward.
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH,in MotorLeft_A  
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# if you have different direction, you need to change HIGH to LOW
# or LOW to HIGH in MotorLeft_A 
# and LOW to HIGH or HIGH to LOW in MotorLeft_B
# ===========================================================================

def leftmotor(x):
	if x == 'True':
		GPIO.output(MotorLeft_A, GPIO.HIGH)
		GPIO.output(MotorLeft_B, GPIO.LOW)
	elif x == 'False':
		GPIO.output(MotorLeft_A, GPIO.LOW)
		GPIO.output(MotorLeft_B, GPIO.HIGH)
	else:
		print 'Config Error'

def rightmotor(x):
	if x == 'True':
		GPIO.output(MotorRight_A, GPIO.LOW)
		GPIO.output(MotorRight_B, GPIO.HIGH)
	elif x == 'False':
		GPIO.output(MotorRight_A, GPIO.HIGH)
		GPIO.output(MotorRight_B, GPIO.LOW)


# =======================================================================
# because the connections between motors (left motor) and Raspberry Pi will be
# established, the being connected GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================
GPIO.setup(MotorLeft_A,GPIO.OUT)
GPIO.setup(MotorLeft_B,GPIO.OUT)
GPIO.setup(MotorLeft_PWM,GPIO.OUT)

# =======================================================================
# because the connections between motors (right motor) and Raspberry Pi will be
# established, the being connected GPIO pins of Raspberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================
GPIO.setup(MotorRight_A,GPIO.OUT)
GPIO.setup(MotorRight_B,GPIO.OUT)
GPIO.setup(MotorRight_PWM,GPIO.OUT)

# =======================================================================
# create left pwm object to control the speed of left motor
# =======================================================================
LeftPwm=GPIO.PWM(MotorLeft_PWM,100)

# =======================================================================
# create right pwm object to control the speed of right motor
# =======================================================================
RightPwm=GPIO.PWM(MotorRight_PWM,100) 

# =======================================================================
# define the forward module
# forward has the parameters of speed and running_time 
def go_forward(speed, running_time):
    # set the left motor to go forward
    leftmotor(forward0)
    #GPIO.output(MotorLeft_A,GPIO.HIGH)
    #GPIO.output(MotorLeft_B,GPIO.LOW)

    #------------------------------------------------------------
    # if you have different direction, you need to change HIGH to LOW
    # in MotorLeft_A and MotorLeft_B 
    # or use leftmotor(forward1)
    #------------------------------------------------------------
    #leftmotor(forward1)


    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    
    # set the right motor to go forward
    rightmotor(forward0)
    #GPIO.output(MotorRight_A,GPIO.LOW)
    #GPIO.output(MotorRight_B,GPIO.HIGH)

    #------------------------------------------------------------
    # if you have different direction, you need to change HIGH to LOW
    # in MotorLeft_A and MotorLeft_B 
    # or use rightmotor(forward1)
    #------------------------------------------------------------
    #rightmotor(forward1)


    GPIO.output(MotorRight_PWM,GPIO.HIGH)
    # set the speed of the left motor to go forward
    LeftPwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to go forward
    RightPwm.ChangeDutyCycle(speed)
    # set the running time of the left motor to go forward
    sleep(running_time)
# =======================================================================

# =======================================================================
# define the backward module
# backward has the parameters of speed and delay (time)
def go_backward(speed, running_time):
    # set the right motor to go backward





# =======================================================================

# =======================================================================
# define the stop module
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM,GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
# =======================================================================

# =======================================================================
# mission has been started as below
try:
    # setup and initialize the left motor and right motor
    LeftPwm.start(0)
    RightPwm.start(0)
    # command for forwarding with speed of 40 and time 3 seconds
    go_forward(40, 3)
    sleep(1)
    go_backward(40, 3)
    sleep(1)
    # command for forwarding with speed of 60 and time 3 seconds



    # command for forwarding with speed of 80 and time 3 seconds

    
    # command for stop
    stop()

# when the Ctrl+C key has been pressed,
# the moving object will be stopped 
except KeyboardInterrupt:
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM,GPIO.LOW)
    # right motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
    # GPIO pin setup has been cleared
    GPIO.cleanup()
# =======================================================================
