#! /usr/bin/python

import epics
import time
import sys

from epics import caput, caget

round = 0
voltvalue = 1300

while 1:

    print ("This is lap %d" % round)

    if voltvalue > 1540:
        voltvalue = 1350
    else:
        voltvalue = voltvalue + 50
    
    print ("Starting voltage in this round is %d" % voltvalue)

    level = 0

    while level < 5:
        channel = 0
        while channel < 8:
           caput ("CB:HV:BOX:19:%s:%s:set_volt" % (level, channel), "%d" % voltvalue)
           print caget ("CB:HV:BOX:19:%s:%s:set_volt" % (level, channel))
           channel = channel + 1
           voltvalue = voltvalue + 1
        level = level + 1
    round = round + 1
    time.sleep(180)


