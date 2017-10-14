#########################################################################
### Date: 2017/10/13
### file name: tracking.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction 
### 
#########################################################################

# =======================================================================
# import GPIO library and time module 
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false 
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)



# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Rapberry Pi
# as the control pins of 5-way trackinmg sensor in order to
# control direction
# 
#  leftmostled    leftlessled     centerled     rightlessled     rightmostled
#       16            18              22             40              32
#
# led turns on (1) : trackinmg sensor led detects white playground
# led turns off(0) : trackinmg sensor led detects black line

# leftmostled off : it means that moving object finds black line
#      lmled         at the position of leftmost                
#                   black line locates leftmost of the moving object
#
# leftlessled off : it means that moving object finds black line
#       llled             at the position of leftless
#                   black line locates leftless of the moving object
# 
# centerled off : it means that moving object finds black line
#        ctled           at the position of center
#                   black line locates center of the moving object
# 
# rightlessled off : it means that moving object finds black line
#       rlled            at the position of rightless
#                   black line locates rightless of the moving object
# 
# rightmostled off : it means that moving object finds black line
#        rmled           at the position of rightmost
#                   black line locates rightmost of the moving object
# =======================================================================

lmled=16  # leftmostled
llled=18  # leftlessled
ctled=22  # centerled
rlled=40  # rightlessled
rmled=32  # rightmostled


# =======================================================================
# because the connetions between 5-way tracking sensor and Rapberry Pi has been 
# established, the GPIO pins of Rapberry Pi
# such as leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared as input
# 
# =======================================================================

GPIO.setup(lmled, GPIO.IN)
GPIO.setup(llled, GPIO.IN)
GPIO.setup(ctled, GPIO.IN)
GPIO.setup(rlled, GPIO.IN)
GPIO.setup(rmled, GPIO.IN)



# =======================================================================
# GPIO.input(leftmostled) method gives the data obtained from leftmostled
# lmledv : value of lmled
# leftmostled returns (1) : leftmostled detects white playground
# leftmostled returns (0) : leftmostled detects black line
#
#
# GPIO.input(leftlessled) method gives the data obtained from leftlessled
# llledv : value of lled
# leftlessled returns (1) : leftlessled detects white playground
# leftlessled returns (0) : leftlessled detects black line
#
# GPIO.input(centerled) method gives the data obtained from centerled
# ctledv : value of ctled
# centerled returns (1) : centerled detects white playground
# centerled returns (0) : centerled detects black line
#
# GPIO.input(rightlessled) method gives the data obtained from rightlessled
# rlledv : value of rlled
# rightlessled returns (1) : rightlessled detects white playground
# rightlessled returns (0) : rightlessled detects black line
#
# GPIO.input(rightmostled) method gives the data obtained from rightmostled
# rmledv : value of rmled
# rightmostled returns (1) : rightmostled detects white playground
# rightmostled returns (0) : rightmostled detects black line
#
# =======================================================================

# lmledv : value of lmled
# llledv : value of lled
# ctledv : value of ctled
# rlledv : value of rlled
# rmledv : value of rmled

lmledv=str(GPIO.input(lmled))
llledv=str(GPIO.input(llled))
ctledv=str(GPIO.input(ctled))
rlledv=str(GPIO.input(rlled))
rmledv=str(GPIO.input(rmled))


try:
    while True:
       print("lmled llledv ctled rlled rmled: " + "[" + lmledv+llledv+ctledv+rlledv+rmledv +"]")
       if lmledv == "0":
          print("lmled: black line(0)")
       else: 
          print("lmled: white ground(1)")

       if llledv == "0":
          print("llledv: black line(0)")
       else: 
          print("llledv: white ground(1)")

       if ctledv == "0":
          print("ctled: black line(0)")
       else: 
          print("ctled: white ground(1)")

       if rlledv == "0":
          print("rlled: black line(0)")
       else: 
          print("rlled: white ground(1)")

       if rmledv == "0":
          print("rmled: black line(0)")
       else: 
          print("rmled: white ground(1)")
          
       #print("leftlessled  detects black line(0) or white ground(1): " + llledv)
       #print("centerled    detects black line(0) or white ground(1): " + ctledv)
       #print("rightlessled detects black line(0) or white ground(1): " + rlledv)
       #print("rightmostled detects black line(0) or white ground(1): " + rmledv)
       sleep(1)
               
except KeyboardInterrupt:
    GPIO.cleanup()


