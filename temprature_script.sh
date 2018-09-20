#! /bin/bash

log="/home/pi/BabyMonitor/logs"

#run the client

"/home/pi/dht" > temperature.txt

OUTPUT=`cat temperature.txt`

# Write values to the screen

TEMPERATURE=`echo "$OUTPUT"`

# Output data to a log file

echo "$(date +"%Y-%m-%d %T" ) ""$TEMPERATURE" >>"$log"temperature.log