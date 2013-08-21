#! /usr/bin/python

import epics
import time

from epics import caput, caget

count = 0

while (count < 10 ):
    count = count +1    
#    caput("CB:HV:BOX:19:1:1:read_volt")
#    time.sleep(1)
    voltage11 = caget("CB:HV:BOX:19:1:1:read_volt")
    voltage12 = caget("CB:HV:BOX:19:1:2:read_volt")
    print "%s %s" % (voltage11, voltage12)
    time.sleep(1)
