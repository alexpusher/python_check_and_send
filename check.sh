#!/bin/sh

while [ 1 ]; do
	ifconfig wlan0 | grep status #wlan0 - interface
	sleep 1
done
