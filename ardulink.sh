#!/bin/bash
ln -s /dev/ttyACM0 /dev/ttyS80
java -jar /home/pi/ardulink/lib/ardulink-mqtt-0.6.1.jar -a 0 -brokerHost localhost
