#! /usr/bin/python

import epics
import time
import urllib2

from epics import caget

NN = 42

while 1:
    XX = caget("CB:HV:BOX:19:1:1:read_volt")
    YY = caget("CB:HV:BOX:19:1:2:read_volt")
    ZZ = caget("CB:HV:BOX:19:1:3:read_volt")
    print XX + " " + YY + " " + ZZ
    URL = "http://a2onlinedatabase.office.a2.kph/intern/sc/insert.php?/Node=%s&Value1=%s&Value2=%s&Value3=%s" % (NN, XX, YY, ZZ)
    urllib2.urlopen("%s" % URL)    
    time.sleep(5)
