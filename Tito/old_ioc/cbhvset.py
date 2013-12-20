#! /usr/bin/python

import epics
import time
import sys

#f = open ("cbhvtestwerte.txt", "r")

#werte = f.readlines()

#f.close

level = 0
count = 0

if len(sys.argv) < 3:

	box = raw_input('Boxnumber: ')
	setvolt = raw_input('Spannung[V]: ')

else:

	box = sys.argv[1]
	setvolt = sys.argv[2]	

from epics import caput, caget

channel = 0	
		
while (level < 5):

	channel = 0	
	
	while (channel < 8):
		
		caput("CB:HV:Box:%s:set_voltage" % box, "%d %d %s" % (level, channel, setvolt)) 
		time.sleep(5)
	#	caput("CB:HV:Box:%s:read_voltage" % box, "%d %d" % (level, channel))
	#	time.sleep(1)
	#	realvolt = caget("CB:HV:Box:%s:read_voltage" % box)
	#	if realvolt==None:
	#		print "EPICS needs to be started first!"
	#		sys.exit(1)
	#	voltstring = "%s %d %d %s => %s" % (box, level, channel, setvolt, realvolt)
	#	print voltstring
		channel = channel + 1
		count = count +1

	level = level + 1
