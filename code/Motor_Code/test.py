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


def Start(input, input1, input2):
 if(input<0):
  y=1
  input=abs(input)
 else:
  y=0
 if(input<=90):
  input= int (round(input*.70))
 if((input>90) and (input<180)):
  input= int (round(input*.80))
 if((input>=180) and (input<=200)):
  input= int (round(input*.88))
 if((input>200) and (input<=275)):
  input= int (round(input*.97))
 else:
  input= int (round(input*1.02))

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

 if(input2<0):
  y=1
  input2=abs(input2)
 else:
  y=0
 if(input2<=90):
  input2= int (round(input2*.70))
 if((input2>90) and (input2<180)):
  input2= int (round(input2*.80))
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




if __name__ == '__main__':
 input=int (sys.argv[1])
 input1=int (sys.argv[2])
 input2=int (sys.argv[3])

 Start(input, input1, input2)
