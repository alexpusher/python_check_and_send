#!/bin/sh
while [ 1 ]; do
	ifconfig wlan0 | grep status
	sleep 1
done
