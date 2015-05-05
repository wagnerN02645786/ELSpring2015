#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys

#import math
# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 150  # Max pulse length out of 4096

# Start is the program to move motors of a arm board in any axis (X, Y, Z)
# input --> Motor 1 (X-axis)
# input-->Motor 2 (Y-axis)
# input-->Motor 3 (Z-axis)
# get input--> Move X-axis-->Move Y-axis-->Move Z-axis

def Start(input, input1, input2):

#Motor 1 X-axis
 if(input<0):	#take absolute value if less then 0
  y=1
  input=abs(input)
 else:
  y=0

 if(input<=90):#if the destination to move is less than 90degrees
  if(y==1):#going around in the clockwise direction may need to be higher
   input=int(round(input*.8))
  else:
   input= int (round(input*.71))
 if((input>90) and (input<180)):#destination to move < 180 degrees
  input= int (round(input*.82))
 if((input>=180) and (input<=200)):
  input= int (round(input*.9))
 if((input>200) and (input<=275)):
  input= int (round(input*.99))
 else:
  input= int (round(input*1.05))

 pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
 x=0

 if(y==0):
  for x in range(0,input):
   pwm.setPWM(0, 0, servoMin)
   pwm.setPWM(0,0,0)

 if(y==1):
  x=0
  for x in range(0, input):
   pwm.setPWM(0,servoMax,0)
   pwm.setPWM(0,0,0)

#----------------------------------------------------------------------------------------
#Motor 2 Y-axis
 if(input1<0):
  y=1
  input1=abs(input1)
 else:
  y=0
 if(input1<=90):
  input1= int (round(input1*.70))
 if((input>90) and (input1<180)):
  input1= int (round(input1*.80))
 if((input1>=180) and (input1<=200)):
  input1= int (round(input1*.88))
 if((input1>200) and (input1<=275)):
  input1= int (round(input1*.97))
 else:
  input1= int (round(input1*1.02))

 pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
 x=0

 if(y==0):
  for x in range(0,input1):
   pwm.setPWM(1, 0, servoMin)
   pwm.setPWM(1,0,0)

 if(y==1):
  x=0
  for x in range(0, input1):
   pwm.setPWM(1,servoMax,0)
   pwm.setPWM(1,0,0)

#------------------------------------------------------------------------------------------
#Motor 3 Z-axis
 if(input2<0):
  y=1
  input2=abs(input2)
 else:
  y=0
 if(input2<=90):
  input2= int (round(input2*.71))
 if((input2>90) and (input2<180)):
  input2= int (round(input2*.81))
 if((input2>=180) and (input2<=200)):
  input2= int (round(input2*.88))
 if((input2>200) and (input2<=275)):
  input2= int (round(input2*.97))
 else:
  input2= int (round(input2*1.02))

 pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
 x=0

 if(y==0):
  for x in range(0,input2):
   pwm.setPWM(2, 0, servoMin)
   pwm.setPWM(2,0,0)

 if(y==1):
  x=0
  for x in range(0, input2):
   pwm.setPWM(2,servoMax,0)
   pwm.setPWM(2,0,0)


#--------------------------------------------------------------------------------------------
#Main method that is initially called when running
if __name__ == '__main__':
#The location of the motors are allways saved in a Locaction_Motor file
#The file has only 3 numbers for each motors location
 loc= open('./Adafruit_PWM_Servo_Driver/Location_Motor','r')
#Grab each present motor's location
 loc1=loc.readline()			#Motor 1 X-axis
 loc2=loc.readline()			#Motor 2 Y-axis
 loc3=loc.readline()			#Motor 3 Z-axis
 
#input the desired inputs that are sent to the program (where you want to go)
 input=int (sys.argv[1])
 input1=int (sys.argv[2])
 input2=int (sys.argv[3])
 #copy the inputs values
 I1=input
 I2=input1
 I3=input2

 loc1 = int (float(loc1))
 loc2 = int (float(loc2))
 loc3 = int (float(loc3))
 
#If the user inputs 555 to any of the inputs that Reserved number will make the motor not move
#this is done by saving the current location the the input value of the motor
 if(input==555):
  input=loc1
  I1=loc1
 if(input1==555):
  input1=loc2
  I2=loc2
 if(input2==555):
  input2=loc3
  I3=loc3

 I1=input
 I2=input1
 I3=input2

#The location that you want to move needs to be subtracted to check if you are out of the range 
 input=input-loc1
 input1=input1-loc2
 input2=input2-loc3
  
 #Close the location of the file you opened Location_Motor
 loc.close()
#The checking of each motors location to be between 360 and -360 degrees
 if(((I1<=360) and (I2<=360) and (I3<=360)) and ((I1>=-360) and (I2>=-360) and (I3>=-360)) ):
  #If the location to move is okay then save the new location in the file Location_Motor
  loc = open('./Adafruit_PWM_Servo_Driver/Location_Motor','w')
  loc.write(str(I1)+'\n')
  loc.write(str(I2)+'\n')
  loc.write(str(I3)+'\n')

  loc.close()
  #Send only the distance that is needed to get to the desired location
  Start(input, input1, input2)

 else:
 # loc=open('Location_Motor', 'w')
 # loc.write(str(loc1)+'\n')
 # loc.write(str(loc2)+'\n')
 # loc.write(str(loc3)+'\n')

 # loc.close()
  print "Bad Input....Please Enter Again"
