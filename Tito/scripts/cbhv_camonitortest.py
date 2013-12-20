#! /usr/bin/python

import epics, sys, time

from epics import camonitor

while 1:

    camonitor ("CB:HV:BOX:19:0:0:set_volt.PACT")
