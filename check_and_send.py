#!/usr/bin/env python
#coding=utf8

import subprocess
import time
import smtplib
import sys


def myrun(cmd):
	""" Method for input information from cmd
	it's file which checke interface
	if interfaces is down we use method mail
	"""
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout = []
	while True:
		line = p.stdout.readline()
		stdout.append(line)
		#print line
		ph1 = line[9:19]
		#print (ph1)
		if ph1 == 'no carrier':
			mail("NOT WORKING")
			time.sleep(60)
		
def mail(txtparam):
	"""
	fromaddr - send address
	toaddr - receiver address
	username - your email
	pass - your pass from email
	msg_txt - input error message from first method
	"""
	fromaddr = 'Mr. Robot <vederkonavoza@gmail.com>'
	toaddr = 'Administrator <alexpusher1@yandex.ru>'
	subj = 'Notification from system'
	msg_txt = txtparam
	msg = "From: %s\nTo: %s\nSubject: %s\n\n%s"  % ( fromaddr, toaddr, subj, msg_txt)
	username = 'example@example.com'
	password = 'pass from example@example.com'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.set_debuglevel(1);
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddr, msg)
	server.quit()

myrun("/data/check/check.sh")
