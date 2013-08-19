#! /usr/bin/python

import epics
import time
import sys

#f = open ("cbhvtestwerte.txt", "r")

#werte = f.readlines()

#f.close


if len(sys.argv) < 3:

	box = raw_input('Boxnumber: ')
	setvolt = raw_input('Spannung[V]: ')

else:

	box = sys.argv[1]
	setvolt = sys.argv[2]

count = 0	

from epics import caput, caget

level = 0

while (level < 5):

	channel = 0	
	
	while (channel < 8):
		
		caput("CB:HV:Box:%s:set_voltage" % box, "%d %d %s" % (level, channel, setvolt)) 
		print setvolt
		time.sleep(5)
		caput("CB:HV:Box:%s:read_voltage" % box, "%d %d" % (level, channel))
		time.sleep(1)
		realvolt = caget("CB:HV:Box:%s:read_voltage" % box)
		if realvolt==None:
			print "EPICS needs to be started first!"
			sys.exit(1)
		voltstring = "%s %d %d %s => %s" % (box, level, channel, setvolt, realvolt)
		print voltstring
		channel = channel + 1

	level = level + 1
# with open("count.txt", "a") as myfile:
#		myfile.write("round %d using %s Volt completed\n" % (count, setvolt))
