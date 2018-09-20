import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    with open("motion_detect.log",'r') as f:
	    while True:
	        if GPIO.input(23):       
			ts = time.time();
			f.write("{}:motion deteceted".format(ts))
			time.sleep(5)	            
except:
    GPIO.cleanup()