#! /bin/bash

log="/home/pi/BabyMonitor/logs/"

#run the client

python /home/pi/BabyMonitor/motion.py > motion.txt

OUTPUT=`cat motion.txt`

# Write values to the screen

MOTION=`echo "$OUTPUT"`

# Output data to a log file

echo "$(date +"%Y-%m-%d %T" ): ""$MOTION" >>"$log"motion.log