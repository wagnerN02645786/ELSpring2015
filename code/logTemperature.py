import sqlite3

import os
import time
import glob


# store the temperature in the database
def log_temperature(tempC, tempF):

    conn=sqlite3.connect("temperature.db")
    curs=conn.cursor()

    curs.execute("INSERT INTO TempData values(datetime('now'),"+str(tempC)+" ,"+str(tempF)+" )")


    # commit the changes
    conn.commit()

    conn.close()






# main function
# This is where the program starts 
def main():

    # enable kernel modules
    os.system('sudo modprobe w1-gpio')
    os.system('sudo modprobe w1-therm')

    
    # get the temperature from the device file
    tempfile = open("/sys/bus/w1/devices/28-00000698f2db/w1_slave")
    tempfile_text = tempfile.read()
    currentTime=time.strftime('%x %X %Z')
    tempfile.close()
    tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
    tempF=tempC*9.0/5.0+32.0
    temperature =tempF 
    if temperature != None:
        print "Current Temperature is="+str(temperature)+" F  or "+str(tempC)+"C"
   
    # Store the temperature in the database
    log_temperature(tempC, tempF)
    print "Temperature logged"


    
    


      

if __name__=="__main__":
    main()

