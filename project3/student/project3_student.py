######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

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
# import getDistance() method in the ultraModule 
# =======================================================================
from ultraModule import getDistance

# =======================================================================
# import rightSwingTurn() method in the swingTurnModule 
# =======================================================================
from swingTurnModule import rightSwingTurn
from swingTurnModule import leftSwingTurn 
# student assignment (1)
# student assignment (2)

# =======================================================================
# import rightPointTurn() method in the pointTurnModule 
# =======================================================================
from pointTurnModule import rightPointTurn 
# student assignment (3) 
# student assignment (4)
from pointTurnModule import leftPointTurn  
# student assignment (5)
 
# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),  
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any 
# =======================================================================
from go_any import go_forward_any  # student assignment (6) (7)
from go_any import go_backward_any # student assignment (8)
from go_any import go_forward      # student assignment (9)
from go_any import go_backward     # student assignment (10)
from go_any import stop
from go_any import LeftPwm 
from go_any import RightPwm
from go_any import pwm_setup  
from go_any import pwm_low


# =======================================================================    
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
dis= 20    # ??
obstacle=1

# when obstacle=1, the power and
# running time of the first turn 
SwingPr=90  # student assignment (11)
SwingTr=0.9 # student assignment (12)


try:
    while True:
        # ultra sensor replies the distance back  
        distance = getDistance()
        print('distance= ', distance)

        # when the distance is above the dis, moving object forwards
        if (distance > dis): 
            go_forward_any(50)
            print('obstacle=', obstacle)
            
        # when the distance is below the dis, moving object stops   
        else:
            # stop and wait 1 second
            stop()
            sleep(1)
            
            
            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (13)
            ########################################################
          

# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
    
