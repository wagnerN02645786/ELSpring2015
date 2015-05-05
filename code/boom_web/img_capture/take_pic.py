#!/usr/bin/python
import picamera
import time
import os
from subprocess import check_output
pictureNumber = str(len([name for name in os.listdir("/var/www/ELSpring2015/code/boom_web/img_capture")])) #counts the number of files in the given directory

os.system("sudo service motion stop") #stops serving the MJPEG to allow camera to take picture
with picamera.PiCamera() as camera:
	camera.capture('/var/www/ELSpring2015/code/boom_web/img_capture/' + 'img_' + pictureNumber + '.jpg') #take picture and name it based on number of pictures in directory
	os.system("sudo service motion start") #restart the MJPEG server
	
