######################################################################
### Date: 2017/10/5
### file name: swingTurnModule.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform swing turn
### this code is used for the student only
######################################################################

# import GPIO librery
import RPi.GPIO as GPIO 
from time import sleep

# set up GPIO mode as BOARD
GPIO.setmode(GPIO.BOARD)

# set GPIO warnings as flase
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
#Set the motor's true / false value to go opposite.
backward0 = REVERSE(forward0)
backward1 = REVERSE(forward1)
# =======================================================================

# =======================================================================
# declare the pins of 12, 11, 35 in the Rapberry Pi
# as the left motor control pins in order to control left motor
# left motor needs three pins to be controlled
# =======================================================================
MotorLeft_A = 12 
MotorLeft_B = 11
MotorLeft_PWM = 35

# =======================================================================
# declare the pins of 15, 13, 37 in the Rapberry Pi
# as the right motor control pins in order to control right motor
# right motor needs three pins to be controlled
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
		GPIO.output(MotorLeft_A, GPIO.LOW)
		GPIO.output(MotorLeft_B, GPIO.HIGH)
	elif x == 'False':
		GPIO.output(MotorLeft_A, GPIO.HIGH)
		GPIO.output(MotorLeft_B, GPIO.LOW)
	else:
		print 'Config Error'

def rightmotor(x):
# student assignment (3)
		
# =======================================================================
# because the connetions between motors (left motor) and Rapberry Pi has been 
# established, the GPIO pins of Rapberry Pi
# such as MotorLeft_A, MotorLeft_B, and MotorLeft_PWM
# should be clearly declared whether their roles of pins
# are output pin or input pin
# =======================================================================

GPIO.setup(MotorLeft_A,GPIO.OUT)
GPIO.setup(MotorLeft_B,GPIO.OUT)
GPIO.setup(MotorLeft_PWM,GPIO.OUT)

# =======================================================================
# because the connetions between motors (right motor) and Rapberry Pi has been 
# established, the GPIO pins of Rapberry Pi
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
# perform right point turn of 90 degree  # student assignment (4)
# ======================================================================
 
def rightPointTurn(speed, running_time):



# =======================================================================
# perform left point turn of 90 degree   # student assignment (5)
# ======================================================================
 
def leftPointTurn(speed, running_time):



