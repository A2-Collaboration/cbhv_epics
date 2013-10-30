#! /usr/bin/python

import epics
import time
import sys

from epics import caput, caget, PV

# Check for filename

if len(sys.argv) < 2:

    box = raw_input('Boxnumber: ')

else:

    box = sys.argv[1]

sys.stdout.write("\x1b]2;Box %s\x07" % box)


# read file

f = open ("cbhv_elements.txt", "r")

werte = f.readlines()

channellist = []

matrix = [[0 for x in xrange(8)] for x in xrange(5)]

while 1:

    count = 1
    
    while (count < len(werte)):

        zeilenwerte = werte[count].split()
#        print zeilenwerte

        if (len(zeilenwerte) == 4 and zeilenwerte[1] == box):

            matrix[int(zeilenwerte[2])][int(zeilenwerte[3])] = caget ("CB:HV:BOX:%s:%s:%s:read_volt" % (zeilenwerte[1], zeilenwerte[2], zeilenwerte[3]))
           # print voltvalue
           # channellist.append("%s %s - %s" % (zeilenwerte[2], zeilenwerte[3], voltvalue))
            count = count + 1
            
        else:

            count = count + 1

    i = 0

    while (i<5):
        
        print matrix[i]

        i = i + 1

    time.sleep(2)
            
            
#while 1:
#    string = []
#    level = 0
#    while level < 5:
#        voltage = []
#        channel = 0
#        while channel < 8:
#           singlevoltage = caget ("CB:HV:BOX:18:%s:%s:read_volt" % (level, channel))
#           voltage.append(singlevoltage)
#           channel = channel + 1
#        string.append("%i  | 0 %s | 1 %s | 2 %s | 3 %s | 4 %s | 5 %s | 6 %s | 7 %s |" % (level, voltage[0], voltage[1], voltage[2], voltage[3], voltage[4], voltage[5], voltage[6], voltage[7]))
#        level = level + 1
#    output = "%s\n%s\n%s\n%s\n%s" % (string[0], string[1], string[2], string[3], string[4])
#    print output
#    time.sleep(2)

#def onChanges(CB":"HV\:BOX\:19\:0\:0\:read_volt = None, value = None, **kw):
#    print CB\:HV\:BOX\:19\:0\:0\:read_volt, value

#B19L0C0 = epics.PV("CB:HV:BOX:19:0:0:read_volt")
#B19L0C0.add_callback(onChanges)

#while 1:
#    time.sleep(1)
