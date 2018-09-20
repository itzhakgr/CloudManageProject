import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #PIR

now = datetime.datetime.now()

try:
	time.sleep(1) # to stabilize sensor
	if GPIO.input(23):       
        	print now.strftime("%H:%M:%S %d-%m-%Y") + " NO_HeartBit"
	else:
		print now.strftime("%H:%M:%S %d-%m-%Y") + " Pulse_Detected"
except:
    GPIO.cleanup()