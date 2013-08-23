#! /usr/bin/python

import epics
import time
import sys

from epics import caput, caget

while 1:
    string = []
    level = 0
    while level < 5:
        voltage = []
        channel = 0
        while channel < 8:
           singlevoltage = caget ("CB:HV:BOX:19:%s:%s:read_volt.VAL" % (level, channel))
           voltage.append(singlevoltage)
           channel = channel + 1
        string.append("%i  | 0 %s | 1 %s | 2 %s | 3 %s | 4 %s | 5 %s | 6 %s | 7 %s |" % (level, voltage[0], voltage[1], voltage[2], voltage[3], voltage[4], voltage[5], voltage[6], voltage[7]))
        level = level + 1
    output = "%s\n%s\n%s\n%s\n%s" % (string[0], string[1], string[2], string[3], string[4])
    print output
