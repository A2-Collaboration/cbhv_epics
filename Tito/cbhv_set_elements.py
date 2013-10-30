#! /usr/bin/python
import epics
import time
import sys

# Check for filename

if len(sys.argv) < 2:

    readfile = raw_input('Filename: ')

else:

    readfile = sys.argv[1]


# read file

f = open ("%s" % readfile, "r")

werte = f.readlines()

f.close

from epics import caput

count = 0

while (count < len(werte)):

        zeilenwerte = werte[count].split()
        if (len(zeilenwerte)==2):
            caput ("CB:HV:ELEMENT:%s:set_volt" % zeilenwerte[0], "%s" % zeilenwerte[1])
        count = count + 1
            
        else: 

            print "Missing or to many values in line %d (index starts at zero)!" % count

        count = count + 1

        
    
    
