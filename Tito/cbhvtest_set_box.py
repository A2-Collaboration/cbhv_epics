#! /usr/bin/python

import epics
import time
import sys

# read file

f = open ("cbhv_elements.txt", "r")

werte = f.readlines()

f.close

if len(sys.argv) < 3:

	box = raw_input('Boxnumber: ')
	setvolt = raw_input('Spannung[V]: ')

else:

	box = sys.argv[1]
	setvolt = sys.argv[2]

count = 1	

from epics import caput, caget

level = 0

while (count < len(werte)):

	zeilenwerte = werte[count].split()

	if (len(zeilenwerte) == 4 and zeilenwerte[1] == box):
		
		caput("CB:HV:BOX:%s:%s:%s:set_volt" % (box, zeilenwerte[2], zeilenwerte[3]), "%s" % (setvolt)) 
		count = count + 1

	else:

	        count = count + 1
